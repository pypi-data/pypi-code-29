# -*- coding: utf8 -*-

import base64
import copy
import datetime
import hashlib
import logging
import os
import platform
import random
import uuid
import warnings

import six

from .exceptions import ExperimentStopped
from .exceptions import MissingLinkException
from .logger_wrapper import LoggerWrapper
from .settings import EventTypes, HyperParamTypes
from .utilities import source_tracking
from .utilities.utils import export_exception

#

DISPATCH_INTERVAL = 5
MAX_BATCHES_PER_EPOCH = 1000
SAMPLING_SIZE = 1000
SEND_EPOCH_CANDIDATES = False
FIRST_ITERATION = 1

WEIGHTS_HASH_PREFIX = 'v1_'


class BaseCallback(object):
    @classmethod
    def _validate_auth_params(cls, owner_id, project_token):
        rm_env = cls._get_rm_env()
        owner_id = rm_env.get('ML_OWNER_ID', owner_id)
        project_token = rm_env.get('ML_PROJECT_TOKEN', project_token)

        if owner_id is None:
            raise ValueError('owner id is not provided and `ML_OWNER_ID` environment variable not present')

        if project_token is None:
            raise ValueError('project token is not provided and `ML_OWNER_ID` environment variable not present')

        return owner_id, project_token

    def __init__(self, owner_id=None, project_token=None, stopped_callback=None, host=None, framework='none', resume_token=None):
        from missinglink_kernel import get_version
        self.logger = LoggerWrapper()
        stoppable = True
        owner_id, project_token = self._validate_auth_params(owner_id=owner_id, project_token=project_token)
        self.experiment_args = {
            'owner_id': owner_id,
            'project_token': project_token,
            'host': host,
            'stoppable': stoppable,
        }

        if stopped_callback and not callable(stopped_callback):
            self.logger.warning('stopped_callback is not callable, will be ignored')
            stopped_callback = None

        self.stopped_callback = stopped_callback
        self.rm_properties = self._export_resource_manager()
        self.properties = {
            'env': {
                'framework': framework,
                'missinglink_version': get_version(),
                'node': platform.node(),
                'platform': platform.platform(),
                'processor': platform.processor(),
                'python_version': platform.python_version(),
            },
            'source_tracking': {
                'error': 'disabled'
            },
            'callback_tag': self.generate_tag(),
            'stoppable': stoppable,
        }

        self._update_properties = True

        if resume_token is not None:
            self.properties['resume_token'] = resume_token

        self.post_requests = None

        self.batches_queue = []
        self.points_candidate_indices = {}
        self.iteration = 0
        self._test_iteration = 0
        self.ts_start = 0
        self.epoch_addition = 0
        self.has_ended = False
        self.tests_counter = 0
        self.stopped = False
        self.dispatch_interval = DISPATCH_INTERVAL
        self._found_classes = None
        self._has_test_context = False
        self._test_iter = -1
        self._test_iteration_count = 0
        self._test_token = None
        self._class_mapping = None
        self._latest_metrics = {}

        if SEND_EPOCH_CANDIDATES:
            self.epoch_candidate_indices = {}

        warnings.filterwarnings("once", "was not able to get variable.*")
        warnings.filterwarnings("once", "skipped MissingLinkJsonEncoder because of TypeError")

    @property
    def rm_data_iterator_settings(self):
        rm_data = self.rm_properties.get('data', {})
        if rm_data.get('use_iterator', 'False') != 'True':
            return None

        return rm_data['volume'], rm_data['query']

    @property
    def rm_active(self):
        return self.rm_properties is not None and self.rm_properties.get('in_context', '').lower() == 'true'

    @classmethod
    def _get_rm_env(cls):
        return dict([x for x in os.environ.items() if x[0].startswith('ML_') or x[0] == 'ML'])

    __rm_root_mapping = {
        'ML': 'in_context',
        'ML_JOB_ID': 'job_id',
        'ML_ORG_ID': 'org_id',
        'ML_INVOCATION_ID': 'invocation_id',
        'ML_PROJECT_ID': 'project_id',
        'ML_CLUSTER_ID': 'resource_manager',
        'ML_CLUSTER_MANAGER': 'socket_server',
        'ML_OUTPUT_DATA_VOLUME': 'output_volume_id',
        'ML_OWNER_ID': 'owner_id',
        'ML_JOB_NAME': 'job_name',
        'ML_PROJECT_TOKEN': 'project_token',

    }
    __rm_data_mapping = {
        'ML_DATA_USE_ITERATOR': 'use_iterator',
        'ML_DATA_VOLUME': 'volume',
        'ML_DATA_QUERY': 'query'
    }

    @classmethod
    def _rm_map_value(cls, rm_data, k, v):
        if k in cls.__rm_root_mapping:
            rm_data[cls.__rm_root_mapping[k]] = v
            return

        if k in cls.__rm_data_mapping:
            rm_data['data'][cls.__rm_data_mapping[k]] = v
            return

        if k.startswith('ML_MOUNT_'):
            if not v.startswith('/'):
                v = '/%s' % v
            rm_data['volumes'].append(v)
            return

        k = k[len('ML_'):].lower()
        rm_data['other'][k] = v

    @classmethod
    def _rm_map_values(cls, mali_env):
        rm_data = {'data': {}, 'volumes': [], 'other': {}}
        for k, v in mali_env.items():
            cls._rm_map_value(rm_data, k, v)
        rm_data['volumes'] = list(sorted(rm_data['volumes']))
        return rm_data

    @classmethod
    def _export_resource_manager(cls):
        mali_env = cls._get_rm_env()

        if mali_env:
            return cls._rm_map_values(mali_env)

        return {}

    @classmethod
    def _export_repo_state(cls, repo_obj):
        src_data = {}
        try:
            src_data['branch'] = repo_obj.branch.name
            src_data['remote'] = repo_obj.remote_url
            src_data['sha_local'] = repo_obj.head_sha
            src_data['sha_local_url'] = repo_obj.head_sha_url
            src_data['is_dirty'] = not repo_obj.is_clean

            commit_data = None
            if repo_obj.has_head:
                commit_data = repo_obj.export_commit(repo_obj.repo.head.commit)

            if commit_data is not None:
                src_data.update(commit_data)

        # noinspection PyBroadException
        except Exception as ex:
            src_data['error'] = export_exception(ex)

        return src_data

    @classmethod
    def __remove_version_part(cls, query):
        from ..data_management.legit.scam import LuceneTreeTransformer, QueryParser, resolve_tree, FunctionVersion
        from ..data_management.legit.scam.luqum.tree import AndOperation, OrOperation

        # noinspection PyClassicStyleClass
        class RemoveVersionTransformer(LuceneTreeTransformer):
            def __init__(self):
                self.version = None

            def visit_operation(self, klass, node, parents):
                def enum_children():
                    for child in node.children:
                        if isinstance(child, FunctionVersion):
                            self.version = child.version
                            continue

                        yield child

                new_node = klass(*list(enum_children()))

                return new_node

            def visit_and_operation(self, node, parents=None):
                return self.visit_operation(AndOperation, node, parents)

            def visit_or_operation(self, node, parents=None):
                return self.visit_operation(OrOperation, node, parents)

            def __call__(self, tree):
                return self.visit(tree)

        transformer = RemoveVersionTransformer()
        tree = QueryParser().parse_query(query)
        resolved_tree = resolve_tree(tree)
        resolved_tree = transformer(resolved_tree)

        query_without_version = str(resolved_tree)

        return query_without_version, transformer.version

    def bind_data_generator(
            self, volume_id, query, data_callback,
            cache_directory=None, batch_size=32, use_threads=False, processes=-1, shuffle=True, cache_limit=None):

        cache_directory = cache_directory or os.environ.get('ML_CACHE_FOLDER', './ml_cache')
        cache_limit = cache_limit or os.environ.get('ML_CACHE_LIMIT')

        from ..data_management import MLDataGenerator

        def install_needed_dependencies():
            def is_s3_volume():
                from ..data_management.query_data_generator import QueryDataGenerator
                from ..data_management.legit.data_volume import with_repo_dynamic
                from ..data_management.legit.gcs_utils import s3_moniker

                ctx = QueryDataGenerator.build_context()

                with with_repo_dynamic(ctx, volume_id) as repo:
                    bucket_name = repo.data_volume_config.object_store_config.get('bucket_name', '')

                    return bucket_name.startswith(s3_moniker)

            from missinglink_kernel.data_management.dynamic_import import install_dependencies, COMMON_DEPENDENCIES, S3_DEPENDENCIES, GCS_DEPENDENCIES

            dependencies = COMMON_DEPENDENCIES[:]

            if is_s3_volume():
                dependencies.extend(S3_DEPENDENCIES)
            else:
                dependencies.extend(GCS_DEPENDENCIES)

            install_dependencies(dependencies)

        install_needed_dependencies()

        query_without_version, version = self.__remove_version_part(query)

        self.properties['data_management'] = {
            'volume_id': volume_id,
            'query': query_without_version,
            'version': version,
        }

        return MLDataGenerator(volume_id, query, data_callback, cache_directory, batch_size, use_threads, processes, shuffle, cache_limit)

    @classmethod
    def _source_tracking_data(cls):
        repo_obj = None
        src_data = {}
        try:
            repo_obj = source_tracking.get_repo()
            src_data = cls._export_repo_state(repo_obj)
        # noinspection PyBroadException
        except Exception as ex:
            src_data['error'] = export_exception(ex)

        return src_data, repo_obj

    def _sync_working_dir_if_needed(self, repo_obj):
        try:
            if self.rm_properties.get('in_context', False):
                logging.info('repository tracking not active: running in resource manager context.')
                return {'error': 'running in resource manager context. shadow tracking does not apply'}

            shadow_url = self.post_requests.get_shadow_repo(repo_obj)
            if shadow_url is None:
                return {'error': 'no tracking repository found.'}

            logging.info('There is repository tracking enabled. Tracking to repository: {}'.format(shadow_url))
            shadow_repo = source_tracking.GitRepoSyncer.clone_tracking_repo(shadow_url)
            commit_tag = source_tracking.GitRepoSyncer.merge_src_to_tracking_repository(repo_obj.repo, shadow_repo)
            shadow_repo_obj = source_tracking.get_repo(repo=shadow_repo)
            cur_br = shadow_repo.active_branch
            shadow_repo.git.checkout(commit_tag)
            shadow_repo_obj.refresh()
            src_data = self._export_repo_state(shadow_repo_obj)
            shadow_repo.git.checkout(cur_br)
            if 'error' not in src_data:
                logging.info('Tracking repository sync completed. This experiment source code is available here: {}'.format(src_data['sha_local_url']))
            else:
                logging.info('Tracking repository sync Failed. The Error was: {}'.format(src_data['error']))
            return src_data

        except Exception as ex:
            ex_txt = export_exception(ex)
            logging.error("Failed to init repository tracking. This experiment may not be tracked. Got: " + ex_txt)
            return {'error': ex_txt}

    @property
    def _is_first_iteration(self):
        return self.iteration == 1

    def _update_test_token(self):
        self._test_token = uuid.uuid4().hex

    def close(self):
        if self.post_requests is not None:
            self.post_requests.close()

        if self.logger is not None:
            self.logger.close()

    def set_properties(self, display_name=None, description=None, class_mapping=None, **kwargs):
        self._update_properties = True
        if display_name is not None:
            self.properties['display'] = display_name

        if description is not None:
            self.properties['description'] = description

        if class_mapping:
            if isinstance(class_mapping, list):
                class_mapping = {k: v for k, v in enumerate(class_mapping)}

            self._class_mapping = class_mapping

        if len(kwargs) > 0:
            self.set_hyperparams(**kwargs)
            self.logger.warning(
                'passing hyper parameters using the set_properties method is deprecated.'
                'please use the set_hyperparams method instead')

    def set_hyperparams(self, total_epochs=None, batch_size=None, epoch_size=None, max_iterations=None,
                        optimizer_algorithm=None, learning_rate=None, total_batches=None, learning_rate_decay=None,
                        samples_count=None, **kwargs):
        self._set_hyperparams(HyperParamTypes.RUN, total_epochs=total_epochs, batch_size=batch_size,
                              epoch_size=epoch_size, total_batches=total_batches, max_iterations=max_iterations,
                              samples_count=samples_count)

        self._set_hyperparams(HyperParamTypes.OPTIMIZER, algorithm=optimizer_algorithm,
                              learning_rate=learning_rate, learning_rate_decay=learning_rate_decay)

        self._set_hyperparams(HyperParamTypes.CUSTOM, **kwargs)

        self._update_properties = True

    def _set_hyperparams(self, hp_type, **kwargs):
        hyperparams = self.get_hyperparams()

        for key, val in kwargs.items():
            if val is None:
                continue

            hyperparams.setdefault(hp_type, {})[key] = val

        self.properties['hyperparams'] = hyperparams

    def get_hyperparams(self):
        return self.properties.get('hyperparams', {})

    def _create_remote_logger_if_needed(self, create_experiment_result):
        if os.environ.get('MISSINGLINKAI_DISABLE_REMOTE_LOGGER') is not None:
            return

        remote_logger = create_experiment_result.get('remote_logger')

        if remote_logger is not None:
            session_id = remote_logger['session_id']
            endpoint = remote_logger['endpoint']
            log_level = remote_logger.get('log_level', logging.INFO)
            log_filter = remote_logger.get('log_filter')
            terminate_endpoint = remote_logger.get('terminate_endpoint')

            self.logger.activate_remote_logging(session_id, endpoint, log_level, log_filter, terminate_endpoint)

    def _call_new_experiment(self, throw_exceptions=None):
        one_hour_seconds = int(datetime.timedelta(hours=1).total_seconds())

        keep_alive_interval = int(os.environ.get('ML_KEEP_ALIVE_INTERVAL', one_hour_seconds))
        res = self.post_requests.create_new_experiment(
            keep_alive_interval, throw_exceptions=throw_exceptions, resume_token=self.properties.get('resume_token'), resource_management=self.rm_properties)

        self._create_remote_logger_if_needed(res)
        if self.post_requests.allow_source_tracking:
            self.properties['source_tracking'], repo = self._source_tracking_data()
            self.properties['repository_tracking'] = self._sync_working_dir_if_needed(repo)
        self.properties['resource_management'] = self.rm_properties

    @property
    def has_experiment(self):
        return self.post_requests is not None

    def new_experiment(self, throw_exceptions=None):
        from .dispatchers.missinglink import post_requests_for_experiment

        self.post_requests = post_requests_for_experiment(**self.experiment_args)

        self._call_new_experiment(throw_exceptions=throw_exceptions)

        self.batches_queue = []
        self.points_candidate_indices = {}
        self.iteration = 0
        self._test_iteration = 0
        self.ts_start = 0
        self.epoch_addition = 0
        self.has_ended = False
        self.stopped = False

        if SEND_EPOCH_CANDIDATES:
            self.epoch_candidate_indices = {}

    @classmethod
    def _image_to_json(cls, img):
        # need to check for string types because we have keep_origin option
        if isinstance(img, six.string_types):
            if six.PY2:
                encoded = base64.b64encode(img)
            else:
                encoded = base64.b64encode(img.encode()).decode()
        else:
            encoded = base64.b64encode(img).decode()
        return encoded

    @classmethod
    def _get_toplevel_metadata(cls, test_token, algo, uri):
        meta = {
            "algo": algo,
            "test_token": test_token,
            "path": uri,
            "prediction_id": uuid.uuid4().hex,
        }
        return meta

    @classmethod
    def _prepare_images_payload(cls, image_objects, keep_origin, uri):
        first_entry = image_objects[0]
        if keep_origin:
            original_image = str(uri)
        else:
            original_image = first_entry["original_image"]
        heatmaps = []
        for i, img_obj in enumerate(image_objects):
            entry = {
                "number": i + 1,  # this should start from 1
                "heatmap_image": cls._image_to_json(img_obj["heatmap_image"]),
                "heatmap_image_key": img_obj["heatmap_image_key"],
                "meta": img_obj["meta"]
            }
            heatmaps.append(entry)

        images = {
            "original_image_key": first_entry["original_image_key"],
            "heatmaps": heatmaps,
            "original_image": cls._image_to_json(original_image)
        }

        return images

    def upload_images(self, model_hash, images, meta, description=None):
        from .dispatchers.missinglink import get_post_requests

        post_requests = get_post_requests(
            self.experiment_args['owner_id'], self.experiment_args['project_token'], host=self.experiment_args['host'])

        data = {
            'model_hash': model_hash,
            'images': images,
            'meta': meta,
            'description': description
        }

        post_requests.send_images(data)

    def send_chart(self, name, x_values, y_values, x_legend=None, y_legends=None, scope='test', type='line', experiment_id=None, model_weights_hash=None):
        """
        Send experiment external chart to an experiment. The experiment can be identified by its ID (experiment_id) or by model_weights_hash in the experiment. Exactly one of experiment_id or model_weights_hash must be provided
        :param name: The name of the chart. The name is used in order to identify the chart against different experiments and through the same experiment.
        :param x_values: Array of `m` Strings / Ints / Floats  -  X axis points.
        :param y_values: Array/Matrix of `m` Y axis points. Can be either array `m` of Integers/Floats or a matrix (having `n` Ints/Floats each), a full matrix describing the values of every y chart in every data point.
        :param x_legend: String, Legend for the X axis
        :param y_legends: String/Array of `n` Strings legend of the Y axis chart(s)
        :param scope: Scope type. Can be 'test', 'validation' or 'train', defaults to 'test'
        :param type: Chart type, currently only 'line' is supported.
        :param experiment_id: The id of the target experiment.
        :param model_weights_hash: a hexadecimal sha1 hash of the model's weights.
        :return:
        """
        from .dispatchers.missinglink import post_requests_for_experiment
        self.logger.activate_if_needed()

        post_r = post_requests_for_experiment(**self.experiment_args)
        post_r.send_chart(name, x_values, y_values, x_legend, y_legends, scope, type, experiment_id, model_weights_hash, throw_exceptions=True)

    def __post_requests_property_wrapper(self, name):
        if self.has_experiment:
            return getattr(self.post_requests, name)

        self.logger.warning('%s is only available after train_begin is called.', name)

        return None

    def update_metrics_per_iteration(self, metrics, model_weights_hash):
        """
        Send external metrics for a specific iteration.
        Using this option you can create a graph of the metrics for each iteration.
        The experiment and iterations are obtained from the weighted hash.
        :param metrics: Dictionary of metric_name => metric_value or (metric_name, metric_value) tuple. Metrics will be automatically prefixed with ex_ when it is not already present.
        :param model_weights_hash: a hexadecimal sha1 hash of the model's weights.
        :return:
        """
        from .dispatchers.missinglink import post_requests_for_experiment
        self.logger.activate_if_needed()

        post_r = post_requests_for_experiment(**self.experiment_args)

        post_r.update_metrics_per_iteration(metrics, model_weights_hash=model_weights_hash, throw_exceptions=True)

    def update_metrics(self, metrics, experiment_id=None, model_weights_hash=None):
        """
        Send external metrics in the experiment level.
        The experiment can be obtained either from the weighted hash or directly by providing the project_id and the experiment_id.
        :param metrics: Dictionary of metric_name => metric_value or (metric_name, metric_value) tuple. Metrics will be automatically prefixed with ex_ when it is not already present.
        :param experiment_id: The id of the target experiment.
        :param model_weights_hash: a hexadecimal sha1 hash of the model's weights.
        :return:
        """
        from .dispatchers.missinglink import post_requests_for_experiment
        self.logger.activate_if_needed()

        post_r = post_requests_for_experiment(**self.experiment_args)

        post_r.update_metrics(metrics, experiment_id=experiment_id, model_weights_hash=model_weights_hash, throw_exceptions=True)

    def __post_requests_property_wrapper(self, name):
        if self.has_experiment:
            return getattr(self.post_requests, name)

        self.logger.warning('%s is only available after train_begin is called.', name)

        return None

    @property
    def experiment_id(self):
        return self.__post_requests_property_wrapper('experiment_id')

    @property
    def experiment_token(self):
        return self.__post_requests_property_wrapper('experiment_token')

    @property
    def resume_token(self):
        experiment_id = self.experiment_id
        if experiment_id is None:
            return None

        return self.experiment_token

    def batch_command(self, event, data, flush=False):
        self.logger.activate_if_needed()

        if self.post_requests is None:
            self.logger.warning(
                'missinglink callback cannot send data before train_begin is called.\n'
                'please access the instruction page for proper use')
            return

        if self.stopped:
            self.logger.debug('experiment stopped, discarding data')
            return

        command = (event, data, datetime.datetime.utcnow().isoformat())

        if event == EventTypes.BATCH_END:
            if SEND_EPOCH_CANDIDATES and data.get('epoch_candidate') in self.epoch_candidate_indices:
                i = self.epoch_candidate_indices[data['epoch_candidate']]
            elif data.get('points_candidate') in self.points_candidate_indices:
                i = self.points_candidate_indices[data['points_candidate']]
            else:
                i = len(self.batches_queue)
                self.batches_queue.append(None)

            self.batches_queue[i] = command

            if SEND_EPOCH_CANDIDATES and 'epoch_candidate' in data:
                self.epoch_candidate_indices[data['epoch_candidate']] = i

            if 'points_candidate' in data:
                self.points_candidate_indices[data['points_candidate']] = i
        else:
            self.batches_queue.append(command)

        if SEND_EPOCH_CANDIDATES and event == EventTypes.EPOCH_END:
            self.epoch_candidate_indices = {}

        if len(self.batches_queue) == 1:
            self.ts_start = datetime.datetime.utcnow()

        ts_end = datetime.datetime.utcnow()
        queue_duration = ts_end - self.ts_start

        if queue_duration.total_seconds() > self.dispatch_interval or flush:
            response = self.post_requests.send_commands(self.batches_queue)
            self.batches_queue = []
            self.epoch_candidate_indices = {}
            self.points_candidate_indices = {}

            if response.get('stopped'):
                self._handle_stopped()

    def _handle_stopped(self):
        self.stopped = True
        if self.stopped_callback:
            self.stopped_callback()
        else:
            raise ExperimentStopped('Experiment was stopped.')

    def train_begin(self, params=None, throw_exceptions=None, **kwargs):
        self.logger.info('train begin params: %s, %s', params, kwargs)

        params = params or {}
        self.new_experiment(throw_exceptions=throw_exceptions)
        data = copy.copy(self.properties)
        data['resource_management'] = self.rm_properties
        data['params'] = params
        data.update(kwargs)
        self.batch_command(EventTypes.TRAIN_BEGIN, data, flush=True)

        self.properties = {}
        self._update_properties = False

    def _train_end(self, **kwargs):
        if not self.has_ended:
            self.logger.info('train end %s', kwargs)

            # Use `iterations` if it is passed. As we move forward, we want to reduce the
            # responsibility of this class. The experiment's state should be managed by another class
            # e.g. Experiment in TensorFlowProject.
            iterations = int(kwargs.get('iterations', self.iteration))

            data = {'iterations': iterations}
            data.update(kwargs)
            self.batch_command(EventTypes.TRAIN_END, data, flush=True)
            self.has_ended = True
            self._latest_metrics = {}

    def train_end(self, **kwargs):
        warnings.warn("This method is deprecated", DeprecationWarning)
        self._train_end(**kwargs)

    # noinspection PyUnusedLocal
    def epoch_begin(self, epoch, **kwargs):
        epoch = int(epoch)

        if epoch == 0:
            self.epoch_addition = 1

    def epoch_end(self, epoch, metric_data=None, **kwargs):
        self.logger.info('epoch %s ended %s', epoch, metric_data)

        epoch = int(epoch)

        if not metric_data:
            return

        data = {
            'epoch': epoch + self.epoch_addition,
            'results': metric_data,
        }

        data.update(kwargs)
        self.batch_command(EventTypes.EPOCH_END, data, flush=data['epoch'] == 1)

    def batch_begin(self, batch, epoch, **kwargs):
        self.iteration += 1

    def batch_end(self, batch, epoch, metric_data, update_hyperparams=False, **kwargs):
        batch = int(batch)
        epoch = int(epoch)
        is_test = kwargs.get('is_test', False)
        metric_data = copy.deepcopy(metric_data)

        # Use `iteration` if it is passed into `batch_end`. As we move forward, we want to reduce the
        # responsibility of this class. The experiment's state should be managed by another class
        # e.g. Experiment in TensorFlowProject.
        iteration = int(kwargs.get('iteration', self.iteration))

        data = {
            'batch': batch,
            'epoch': epoch,
            'iteration': iteration,
            'metricData': metric_data,
        }
        if update_hyperparams or self._update_properties:
            data['params'] = self.properties
            self.properties = {}
        self._update_properties = False
        self._latest_metrics = metric_data

        if is_test:
            self._test_iteration += 1

        starting_offset = SAMPLING_SIZE if is_test else 0
        iteration = self._test_iteration if is_test else iteration

        # Filter batch
        if iteration <= SAMPLING_SIZE:
            if SEND_EPOCH_CANDIDATES:
                data['epoch_candidate'] = batch

            data['points_candidate'] = starting_offset + iteration
        else:
            # Conserve initial location
            points_candidate = random.randint(FIRST_ITERATION + 1, iteration)
            if points_candidate <= SAMPLING_SIZE:
                data['points_candidate'] = starting_offset + points_candidate

            if SEND_EPOCH_CANDIDATES:
                if batch < MAX_BATCHES_PER_EPOCH:
                    data['epoch_candidate'] = batch
                else:
                    epoch_candidate = random.randint(0, batch - 1)
                    if epoch_candidate < MAX_BATCHES_PER_EPOCH:
                        data['epoch_candidate'] = epoch_candidate

        send = 'points_candidate' in data or 'epoch_candidate' in data

        if send:
            data.update(kwargs)
            self.batch_command(EventTypes.BATCH_END, data, flush=iteration == 1)

    def _test_begin(self, test_iter, weights_hash):
        if self._has_test_context:
            self.logger.warning('test begin called twice without calling end')
            return

        self._test_iteration_count = 0
        self._test_samples_count = 0
        self._has_test_context = True
        self._test_iter = test_iter
        self._update_test_token()
        self._found_classes = set()

        data = {
            'test_token': self._test_token,
            'test_data_size': self._test_iter,
        }

        if weights_hash is not None:
            data['weights_hash'] = weights_hash

        self.batch_command(EventTypes.TEST_BEGIN, data, flush=True)

    def _send_test_iteration_end(self, expected, predictions, probabilities, partial_class_mapping,
                                 partial_found_classes, is_finished, **kwargs):
        data = {
            'test_token': self._test_token,
            'predicted': predictions,
            'expected': expected,
            'probabilities': probabilities,
            'iteration': self._test_iteration_count,
            'partial_class_mapping': partial_class_mapping,
            'total_classes': len(self._found_classes),
            'partial_found_classes': partial_found_classes
        }

        data.update(kwargs)
        event = EventTypes.TEST_END if is_finished else EventTypes.TEST_ITERATION_END
        flush = is_finished
        self.batch_command(event, data, flush=flush)

    def _test_iteration_end(self, expected, predictions, probabilities, **kwargs):
        self._test_iteration_count += 1

        is_finished = self._test_iteration_count >= self._test_iter

        partial_class_mapping = {}
        partial_found_classes = []

        unique_ids = list(set(expected) | set(predictions))
        for class_id in unique_ids:
            if class_id not in self._found_classes:
                self._found_classes.add(class_id)
                partial_found_classes.append(class_id)
                if self._class_mapping:
                    if class_id in self._class_mapping:
                        partial_class_mapping[class_id] = self._class_mapping[class_id]
                    else:
                        self.logger.warning('no class mapping for class id %d', class_id)

        self._send_test_iteration_end(expected, predictions, probabilities, partial_class_mapping, partial_found_classes, is_finished=is_finished, **kwargs)

        if is_finished:
            self._test_end()

    def _test_end(self):
        self._has_test_context = False
        self._test_iteration_count = 0
        self._test_token = None

    @staticmethod
    def generate_tag(length=4):
        chars = '1234567890_-abcdefghijklmnopqrstuvwxyz'
        tag = ''
        for _ in range(length):
            tag += random.choice(chars)

        return tag

    def _extract_hyperparams(self, hp_type, obj, object_type_to_attrs, attr_to_hyperparam, object_type=None):
        if isinstance(obj, dict):
            def has_attr(name):
                return name in obj

            def get_attr(name):
                return obj.get(name)
        else:
            def has_attr(name):
                return hasattr(obj, name)

            def get_attr(name):
                return getattr(obj, name)

        object_type = object_type or obj.__class__.__name__
        hyperparams = {}
        attrs = object_type_to_attrs.get(object_type, [])

        for param_name in attrs:
            if has_attr(param_name):
                value = self.variable_to_value(get_attr(param_name))
                param_name = attr_to_hyperparam.get(param_name, param_name)
                hyperparams[param_name] = value
        self._set_hyperparams(hp_type, **hyperparams)

    @classmethod
    def variable_to_value(cls, variable):
        return variable

    @classmethod
    def _hash(cls, value):
        str_repr = str(value).encode("utf-8")
        h = hashlib.sha1(str_repr).hexdigest()
        return h


class BaseContextValidator(object):
    """
        This class validates if we can enter or exit a context.
        """

    def __init__(self, logger):
        self._contexts = []
        self._logger = logger

    def enter(self, context):
        map_context_to_validator = {
            Context.EXPERIMENT: self._validate_experiment_context,
            Context.LOOP: self._validate_loop_context,
            Context.EPOCH_LOOP: self._validate_epoch_loop_context,
            Context.BATCH_LOOP: self._validate_batch_loop_context,
            Context.TRAIN: self._validate_train_context,
            Context.VALIDATION: self._validate_validation_context,
            Context.TEST: self._validate_test_context
        }
        try:
            map_context_to_validator[context]()
        except KeyError:
            # This should never happen unless we mess up
            raise MissingLinkException('Unknown scope %s' % context)

        self._contexts.append(context)

    def exit(self, context):
        last_context = self._contexts.pop()

        if last_context != context:
            # This should never happen unless we mess up
            raise MissingLinkException('Cannot exit %s scope because the current scope is %s' % (context, last_context))

    @property
    def last_context(self):
        try:
            return self._contexts[-1]
        except IndexError:
            raise MissingLinkException("Outside of experiment context. Please use the project to create an experiment.")

    def _validate_experiment_context(self):
        if self._contexts:
            raise MissingLinkException('Experiment context must be outermost')

    def _validate_loop_context(self):
        if not self._contexts or self.last_context != Context.EXPERIMENT:
            raise MissingLinkException('`loop` must be nested immediately in an `experiment` context.')

    def _validate_epoch_loop_context(self):
        if not self._contexts or self.last_context != Context.EXPERIMENT:
            raise MissingLinkException('`epoch_loop` must be nested immediately in an `experiment` context.')

    def _validate_batch_loop_context(self):
        if not self._contexts or self.last_context != Context.EPOCH_LOOP:
            raise MissingLinkException('`batch_loop` must be nested immediately in an `epoch_loop` generator.')

    def _validate_train_context(self):
        pass

    def _validate_validation_context(self):
        pass

    def _validate_test_context(self):
        pass


class Context(object):
    EXPERIMENT = 'experiment'
    LOOP = 'loop'
    EPOCH_LOOP = 'epoch_loop'
    BATCH_LOOP = 'batch_loop'
    TRAIN = 'train'
    TEST = 'test'
    VALIDATION = 'validation'
