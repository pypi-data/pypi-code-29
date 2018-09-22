import requests
from inspect import isclass
from itertools import chain
from threading import Thread
from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from requests.exceptions import RequestException


from .object import Sendable, Receivable, Schema
from .exception import SDKException, ParallelizerException, SequentializerException


class ActionFailedException(Exception):
    pass


class CouldNotSendRequest(Exception):
    pass


class UnexpectedOutcome(Exception):
    pass


class EventHook(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplemented


class Factory(object):
    @staticmethod
    @abstractmethod
    def get_actions():
        """
        :return: a dictionary of {'action name': action class}
        """
        raise NotImplemented

    def __init__(self, api_context, cache=None, presend_hooks=None, success_hooks=None, failure_hooks=None):
        self.api_context = api_context
        self.cache = cache
        self.presend_hooks = OrderedDict() if presend_hooks is None else presend_hooks
        self.success_hooks = OrderedDict() if success_hooks is None else success_hooks
        self.failure_hooks = OrderedDict() if failure_hooks is None else failure_hooks

    def make(self, action):
        result = self.__class__.get_actions()[action](self.api_context)
        result.presend_hooks = OrderedDict(chain(self.presend_hooks.items(),
                                                 result.__class__.get_presend_hooks().items()))
        result.success_hooks = OrderedDict(chain(self.success_hooks.items(),
                                                 result.__class__.get_success_hooks().items()))
        result.failure_hooks = OrderedDict(chain(self.failure_hooks.items(),
                                                 result.__class__.get_failure_hooks().items()))
        return result


class Request(object):
    def __init__(self, verb, url, query_params, body_params, headers):
        self.verb = verb
        self.url = url
        self.body_params = body_params
        self.query_params = query_params
        self.headers = headers

    def send(self):
        return getattr(requests, self.verb)(self.url,
                                            params=self.query_params,
                                            json=self.body_params,
                                            headers=self.headers)


class Action(metaclass=ABCMeta):

    disabled_hooks = set()  # this disables specific event hooks defined in the following methods
    overridden_presend_hooks = OrderedDict()  # this allows to override the hooks defined in the following methods
    overridden_success_hooks = OrderedDict()  # this allows to override the hooks defined in the following methods
    overridden_failure_hooks = OrderedDict()  # this allows to override the hooks defined in the following methods

    @staticmethod
    def get_presend_hooks():
        """
        :return: an ordered dictionary of named `EventHook`s to run in order before a request. These hooks can expect
        the following inputs:
        * request: Request,
        * action: Action,
        * api_context: ApiContext
        """
        return OrderedDict()

    @staticmethod
    def get_success_hooks():
        """
        :return: an ordered dictionary of named `EventHook`s to run in order in the case of a successful request.
        These hooks can expect the following inputs:
        * request: Request,
        * response: requests.Response
        * action: Action,
        * api_context: ApiContext
        """
        return OrderedDict()

    @staticmethod
    def get_failure_hooks():
        """
        :return: an ordered dictionary of named `EventHook`s to run in order in the case of a failed request.
        These hooks can expect the following inputs:
        * request: Request,
        * response: requests.Response
        * action: Action,
        * api_context: ApiContext
        """
        return OrderedDict()

    @staticmethod
    @abstractmethod
    def get_verb():
        """
        :return: the http verb, possible (case insensitive) values are: GET, POST, PATCH, PUT, DELETE
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_route():
        """
        :return: the route this action calls with potential variable parameters, example: /booking/{id}
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_url_schema():
        """
        :return: a dictionary {'param_name': Sendable}, where Sendable is either a subclass of object.Sendable
        or a function which validates the parameter.
        This dictionary should have as keys every key present in the get_route()'s return value as .../{param_name}/...
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_body_schema():
        """
        :return: a dictionary {'param_name': Sendable}, where Sendable is either a subclass of object.Sendable
        or a function which validates a primitive type.
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_query_schema():
        """
        :return: a dictionary {'param_name': Sendable}, where Sendable is either a subclass of object.Sendable
        or a function which validates a primitive type.
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_response_schema():
        """
        :return: a dictionary of {'param_name': Receivable} where Receivable is either a subclass of object.Receivable
        or a function which validates a json and returns the desired object
        """
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_status_exceptions():
        """
        :return: a dictionary of {'status_code': Exception} where Exception should be a class inheriting from python's
        default Exception and taking as constructor input a request.
        """
        raise NotImplemented

    @classmethod
    def json_to_object(cls, obj, schema=None):
        if schema is None:
            schema = cls.get_response_schema()

        if isclass(schema) and issubclass(schema, Receivable):
            schema.validate_dict(obj)
            return schema.from_json(obj)

        elif isinstance(schema, dict):
            result = {}
            for key, condition in schema.items():
                if isclass(condition) and issubclass(condition, Receivable):
                    condition.validate_dict(obj[key])
                    result[key] = condition.from_json(obj[key])
                elif hasattr(condition, '__call__'):
                    result[key] = condition(obj[key])
                elif isinstance(condition, list):
                    list_res = []
                    for el in obj[key]:
                        list_res.append(condition[0].from_json(el))
                    result[key] = list_res
                else:
                    raise ValueError('Dictionary value is neither callable nor Receivable')
            return result

        elif isinstance(schema, list) and schema:
            return [cls.json_to_object(el, schema[0]) for el in obj]

        elif hasattr(schema, '__call__'):
            return schema(obj)

        else:
            raise ValueError('Response schema type not in (Receivable, dict, list, callable)')

    @classmethod
    def validate(cls, obj, rule):
        if isinstance(rule, dict):
            for key, validator in rule.items():
                cls.validate(obj[key], validator)
        elif isclass(rule) and issubclass(rule, Sendable):
            if isinstance(obj, rule):
                obj.validate_obj()
            elif isinstance(obj, dict):
                rule.get_sending_schema()(obj)
            else:
                raise ValueError('Object is of type {}'.format(type(obj)))
        elif isclass(rule) and issubclass(rule, Receivable):
            rule.validate_dict(obj)
        elif isinstance(rule, list) and rule:
            for el in obj:
                cls.validate(el, rule[0])
        elif hasattr(rule, '__call__'):
            Schema(rule)(obj)
        else:
            raise ValueError('Validation rule type not in (dict, list, Sendable, Receivable, callable)')

    def __init__(self, api_context, cache=None):
        cls = self.__class__
        self.api_context = api_context
        self._url_param_names = set()
        self._url_params = {}
        self._body_params = {}
        self._query_params = {}
        self.headers = {}
        self.url = None
        self.compiled = False
        self.cache = cache
        self.presend_hooks = cls.get_presend_hooks()
        self.success_hooks = cls.get_success_hooks()
        self.failure_hooks = cls.get_failure_hooks()

        for chunk in self.__class__.get_route().split('/'):
            if len(chunk) >= 2 and chunk[0] == '{' and chunk[-1] == '}':
                self._url_param_names.add(chunk[1:-1])

        if self._url_param_names != self.__class__.get_url_schema().keys():
            raise ValueError('Provided URL params do not match template')

    @property
    def body_params(self):
        return self._body_params

    @body_params.setter
    def body_params(self, params):
        Action.validate(params, self.__class__.get_body_schema())
        if isinstance(params, dict):
            self._body_params = params
        elif isinstance(params, Sendable):
            self._body_params = params.to_json()
        elif isinstance(params, list):
            # assume list of sendables
            self._body_params = [obj.to_json() for obj in params]
        else:
            raise ValueError('Body params of type {}'.format(type(params)))

    @property
    def query_params(self):
        return self._query_params

    @query_params.setter
    def query_params(self, params):
        Action.validate(params, self.__class__.get_query_schema())
        if isinstance(params, dict):
            self._query_params = params
        else:
            raise ValueError('Must provide a dictionary for query params')

    @property
    def url_params(self):
        return self._url_params

    @url_params.setter
    def url_params(self, params):
        Action.validate(params, self.__class__.get_url_schema())
        self._url_params = params

    def set_headers(self, headers):
        self.headers = headers

    def compile(self):
        if self.compiled:
            raise ValueError('Action already compiled')

        route = self.__class__.get_route()
        for param_name in self._url_param_names:
            route = route.replace('{{{}}}'.format(param_name), self.url_params[param_name])

        host = '{}:{}'.format(self.api_context.hostname, self.api_context.port)

        self.url = self.api_context.url_template.format(hostname=host,
                                                        base_url=self.api_context.base_url,
                                                        version=self.api_context.version,
                                                        route=route)
        self.compiled = True

    def run(self):
        self.compile()

        cls = self.__class__
        verb = cls.get_verb().lower()

        request = Request(verb, self.url, self.query_params, self.body_params, self.headers)

        for name, hook in self.presend_hooks.items():
            if name not in self.__class__.disabled_hooks:
                try:
                    self.__class__.overridden_presend_hooks[name](request, api_context=self.api_context, action=self)
                except KeyError:
                    hook(request, api_context=self.api_context, action=self)

        try:
            response = request.send()
        except RequestException as exc:
            raise CouldNotSendRequest(str(exc))

        status = response.status_code
        if 200 <= status <= 299:

            for name, hook in self.success_hooks.items():
                if name not in self.__class__.disabled_hooks:
                    try:
                        self.__class__.overridden_success_hooks[name](request,
                                                                      response,
                                                                      api_context=self.api_context,
                                                                      action=self)
                    except KeyError:
                        hook(request, response, api_context=self.api_context, action=self)

        else:

            for name, hook in self.failure_hooks.items():
                if name not in self.__class__.disabled_hooks:
                    try:
                        self.__class__.overridden_failure_hooks[name](request,
                                                                      response,
                                                                      api_context=self.api_context,
                                                                      action=self)
                    except KeyError:
                        hook(request, response, api_context=self.api_context, action=self)

            try:
                raise cls.get_status_exceptions()[status](response)
            except KeyError:
                raise ValueError('Request returned unhandled status: {}'.format(status))

        if response.content.decode() == '':
            return None
        response_data = response.json()
        return self.__class__.json_to_object(response_data)

    def rerun(self):
        self.compiled = False
        return self.run()


class RollbackableAction(Action, metaclass=ABCMeta):
    def __init__(self, api_context):
        super().__init__(api_context)
        self.response = None

    def run(self):
        self.response = super().run()
        return self.response

    @abstractmethod
    def rollback(self):
        """
        Executes the operation needed to rollback a previous request. Can use self.response to get useful
        data to use for rollbacking
        :return: None
        """
        raise NotImplemented


class FailCheckThread(Thread):
    def run(self):
        try:
            Thread.run(self)
        except Exception as exc:
            self.err = exc
        else:
            self.err = None


class Summarizable(object):
    def __init__(self):
        self.summary = {'success': {'rollback': {}},
                        'failed': {'rollback': {}},
                        }

    def get_summary(self):
        return self.summary

    def report_action(self, action, index, outcome, result=None):
        if outcome == 'failed':
            self.summary[outcome][
                str(action.__class__.__name__) + '_' + str(index)] = result.__class__.__name__ + ':' + str(result)
        elif outcome == 'rollback_failed':
            self.summary['failed']['rollback'][
                str(action.__class__.__name__) + '_' + str(index)] = result.__class__.__name__ + ':' + str(result)
        elif outcome == 'rollback_success':
            self.summary['success']['rollback'] = str(action.__class__.__name__) + '_' + str(index)
        elif outcome == 'success':
            self.summary[outcome][str(action.__class__.__name__) + '_' + str(index)] = result
        else:
            raise UnexpectedOutcome('{} is not a valid outcome for report_action'.format(outcome))


class ActionParallelizer(Summarizable):
    def __init__(self, *actions):
        self.actions = actions
        super().__init__()

        def store(func, results, i):
            results[i] = func()

        self.results = [None] * len(actions)
        self.threads = [FailCheckThread(target=store, args=(action.run, self.results, i)) for i, action in
                        enumerate(self.actions)]
        self.started = False

    def run(self):
        if self.started:
            raise ValueError('Already started')

        self.started = True

        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()

        failed = {action for action, thread in zip(self.actions, self.threads) if thread.err is not None}
        for index, (action, thread) in enumerate(zip(self.actions, self.threads)):
            if thread.err is not None:
                self.report_action(action, index, 'failed', thread.err)
        for index, result in enumerate(self.results):
            if result is not None:
                self.report_action(self.actions[index], index, 'success', result)
        if failed:
            for index, action in enumerate([act for act in self.actions if act not in failed]):
                if isinstance(action, RollbackableAction):
                    try:
                        action.rollback()
                        self.report_action(action, index, 'rollback_success')
                    except SDKException as exc:
                        self.report_action(action, index, 'rollback_failed', exc)
            raise ParallelizerException(self.summary)

        return self.results


class ActionSequentializer(Summarizable):
    def __init__(self, actions, steps):
        self.init_action = actions[0]
        self.actions = actions[1:]
        self.steps = steps
        self.results = []
        self.started = False
        super().__init__()

    def run(self):
        if self.started:
            raise ValueError('Sequentializer Already Started')
        self.started = True
        try:
            result = self.init_action.run()
            self.results.append(result)
            self.report_action(self.init_action, 'init', 'success', result)
        except SDKException as exc_init:
            self.report_action(self.init_action, 'init', 'failed', exc_init)
            raise SequentializerException(self.summary)
        else:
            for index, (action, step) in enumerate(zip(self.actions, self.steps)):
                try:
                    result = step(result, action)
                    self.results.append(result)
                    self.report_action(action, index, 'success', result)

                except SDKException as exc:
                    self.report_action(action, index, 'failed', exc)

                    for rb_index, to_rollback in reversed(list(enumerate(self.actions[:index]))):
                        if isinstance(to_rollback, RollbackableAction):
                            try:
                                to_rollback.rollback()
                                self.report_action(action, rb_index, 'rollback_success')
                            except SDKException as exc_r:
                                self.report_action(to_rollback, rb_index, 'rollback_failed', exc_r)
                    if isinstance(self.init_action, RollbackableAction):
                        try:
                            self.init_action.rollback()
                            self.report_action(self.init_action, 'init', 'rollback_success')
                        except SDKException as exc_r:

                            self.report_action(self.init_action, 'init', 'rollback_failed', exc_r)
                    raise SequentializerException(self.summary)
            return self.results
