from __future__ import absolute_import, print_function, division, unicode_literals

import os
from glob import glob
import shutil
import h5py

from boltons.fileutils import mkdir_p
from boltons.iterutils import chunked
import numpy as np
from scipy.misc import logsumexp

from executor import execute
from tqdm import tqdm

from .external_models import ExternalModelMixin, download_extract_patch
from .models import GeneralModel
from .datasets import Stimuli, Fixations


def evaluate_scanpaths_hdf5(data, directory, scene_walker_directory, execute=execute, variables=None,
                            params=None, verbose=False, model='dynamic_model'):
    """evaluate log likelihood of scanpath on empirical_density given fixation data and size in degree

    data has to an array of {'saliency': saliency, deg_size: deg_size 'scanpaths': list of {'fixations', 'times'}}

    variables indicates which variables out of [fixations, likelihood, mapsA, mapsI, us] to return
    """

    if os.path.isdir(directory):
        for subdirectory in glob(os.path.join(directory, 'data')):
            print("Warning! Deleting subdirectory", subdirectory)
            shutil.rmtree(subdirectory)

        for subdirectory in glob(os.path.join(directory, 'image'+'[0-9]'*8)):
            print("Warning! Deleting subdirectory", subdirectory)
            shutil.rmtree(subdirectory)
        for hdf5file in glob(os.path.join(directory, '*.hdf5')):
            print("Warning! Deleting file", hdf5file)
            os.remove(hdf5file)

    mkdir_p(directory)

    if variables is None:
        variables = ['fixations', 'likelihood', 'mapsA', 'mapsI', 'us']

    if params:
        pars = np.array([
            params['omega'],
            params['rho'],
            params['sigmaAttention'],
            params['sigmaInhib'],
            params['gamma'],
            params['lambda'],
            params['inhibStrength'],
            params['zeta'],
        ])
    else:
        pars = np.array([])

    #print("Writing data")
    with h5py.File(os.path.join(directory, 'data.hdf5'), 'w') as hdf5file:
        hdf5file.create_dataset('image_count', data=len(data))
        for k, image_data in enumerate(tqdm(data, disable=not verbose)):

            image_group = hdf5file.create_group('image{k:08d}'.format(k=k))
            image_group.create_dataset('scanpath_count', data=len(image_data['scanpaths']))
            image_group.create_dataset('saliency', data=image_data['saliency'].astype(float).T)
            image_group.create_dataset('im_size', data=np.array(image_data['saliency'].shape).astype(float)[np.newaxis, :].T)
            image_group.create_dataset('deg_size', data=np.array(image_data['deg_size']).astype(float)[np.newaxis, :].T)
            image_group.create_dataset('pars', data=np.array(pars).astype(float))

            for i, scanpath_data in enumerate(image_data['scanpaths']):
                scanpath_group = image_group.create_group('scanpath{i:08d}'.format(i=i))

                scanpath_group.create_dataset('fixations', data=np.asarray(scanpath_data['fixations'], float).T)
                scanpath_group.create_dataset('times', data=np.asarray(scanpath_data['times'], float)[np.newaxis, :])

    full_scene_walker_directory = os.path.join(os.getcwd(), scene_walker_directory)

    save_cmds = []
    for variable_name in variables:

        source = variable_name

        if variable_name == 'last_us':
            source = 'us(:, :, end-1)'

        save_cmds.append("type_id = H5T.copy('H5T_IEEE_F64LE');")
        save_cmds.append("dims = fliplr(size({source}));".format(source=source))
        save_cmds.append("space_id = H5S.create_simple(length(dims), dims, dims);")
        save_cmds.append("dataset_id = H5D.create(output_scanpath_group, '{variable_name}', type_id, space_id, 'H5P_DEFAULT');".format(variable_name=variable_name))
        save_cmds.append("H5D.write(dataset_id, 'H5ML_DEFAULT', 'H5S_ALL', 'H5S_ALL', plist, {source});".format(source=source))

        save_cmds.append("H5S.close(space_id);")
        save_cmds.append("H5T.close(type_id);")
        save_cmds.append("H5D.close(dataset_id);")

    save_cmd = '\n                '.join(save_cmds)

    with open(os.path.join(directory, 'run.m'), 'w') as f:
        f.write("""
        addpath('{full_scene_walker_directory}');

        input_file_id = H5F.open('data.hdf5');
        output_file_id = H5F.create('results.hdf5');

        plist = 'H5P_DEFAULT';

        d_id = H5D.open(input_file_id, 'image_count');
        image_count = H5D.read(d_id);
        H5D.close(d_id);

        for image_no = 1 : image_count

            input_image_group = H5G.open(input_file_id, sprintf('/image%08d', image_no-1));
            output_image_group = H5G.create(output_file_id, sprintf('/image%08d', image_no-1), plist, plist, plist);

            d_id = H5D.open(input_image_group, 'im_size');
            im_size = H5D.read(d_id);
            H5D.close(d_id);

            d_id = H5D.open(input_image_group, 'deg_size');
            deg_size = H5D.read(d_id);
            H5D.close(d_id);

            d_id = H5D.open(input_image_group, 'saliency');
            saliency = H5D.read(d_id);
            H5D.close(d_id);

            d_id = H5D.open(input_image_group, 'pars');
            pars = H5D.read(d_id);
            H5D.close(d_id);

            d_id = H5D.open(input_image_group, 'scanpath_count');
            scanpath_count = H5D.read(d_id);
            H5D.close(d_id);

            fprintf('       ');

            for scanpath_no = 1 : scanpath_count


                input_scanpath_group = H5G.open(input_image_group, sprintf('/image%08d/scanpath%08d', image_no - 1, scanpath_no - 1));
                output_scanpath_group = H5G.create(output_image_group, sprintf('/image%08d/scanpath%08d', image_no - 1, scanpath_no - 1), plist, plist, plist);

                fprintf('\\rimage %d/%d scanpath %d/%d', image_no, image_count, scanpath_no, scanpath_count);

                d_id = H5D.open(input_scanpath_group, 'fixations');
                fixations = H5D.read(d_id);
                H5D.close(d_id);

                d_id = H5D.open(input_scanpath_group, 'times');
                times = H5D.read(d_id);
                H5D.close(d_id);

                [fixations, likelihood, mapsA, mapsI, us] = {model}(im_size, deg_size, saliency, fixations(1, :), times, fixations(2:end, :), pars);

                {save_cmd}

            end

            H5G.close(input_image_group);
            H5G.close(output_image_group);


        end

        fprintf('\\rDone.                                             \\n');

        H5F.close(input_file_id);
        H5F.close(output_file_id);

        """.format(
            full_scene_walker_directory=full_scene_walker_directory,
            save_cmd=save_cmd,
            model=model)
        )

    full_directory = os.path.join(os.getcwd(), directory)
    execute('matlab -nodesktop -r "try;run;catch exc;disp(getReport(exc));disp(\'__ERROR__\');exit(1);end;quit"',
            directory=full_directory)

    results = []

    #print("reading results")
    with h5py.File(os.path.join(directory, 'results.hdf5'), 'r') as results_file:
        for k, image_data in enumerate(tqdm(data, disable=not verbose)):
            results.append([])

            image_group = results_file['image{k:08d}'.format(k=k)]

            for i, scanpath_data in enumerate(image_data['scanpaths']):
                data = {}

                scanpath_group = image_group['scanpath{i:08d}'.format(i=i)]
                for variable in variables:
                    # matlab transposes the data before storing it in hdf5. We have to transpose it back.
                    data[variable] = scanpath_group[variable][...].T
                results[-1].append(data)

    for hdf5file in glob(os.path.join(directory, '*.hdf5')):
        os.remove(hdf5file)

    return results


class SceneWalker(ExternalModelMixin, GeneralModel):
    """The SceneWalker model

    .. seealso::
        TODO
    """

    __modelname__ = 'SceneWalker'

    def __init__(self,
                 base_model, pixel_per_dva, temporary_directory,
                 rho=1e30, omega=1.9298, gamma=44.780, lambda_=0.8115,
                 sigmaAttention = 5.9082*np.sqrt(0.8115),
                 sigmaInhib = 4.5531*np.sqrt(44.780),
                 inhibStrength = 0.3637,
                 zeta = 0.0722,
                 location=None,
                 execute=execute,
                 **kwargs):
        self.setup(location)
        super(SceneWalker, self).__init__(**kwargs)

        self.base_model = base_model
        self.pixel_per_dva = pixel_per_dva
        self.temporary_directory = temporary_directory
        self.execute = execute

        self.rho = rho
        self.omega = omega
        self.gamma = gamma
        self.lambda_ = lambda_
        self.sigmaAttention = sigmaAttention
        self.sigmaInhib = sigmaInhib
        self.inhibStrength = inhibStrength
        self.zeta = zeta

        self._model_function = 'dynamic_model'

    def _setup(self):
        mkdir_p(self.location)
        download_extract_patch('http://read.psych.uni-potsdam.de/attachments/article/174/PaperCode.zip',
                               'a5c6cf7f5b05281fced56a5841842f4c',
                               self.location,
                               location_in_archive=False,
                               patches=None)

    @property
    def params(self):
        return {
            'rho': self.rho,
            'omega': self.omega,
            'gamma': self.gamma,
            'lambda': self.lambda_,
            'sigmaAttention': self.sigmaAttention,
            'sigmaInhib': self.sigmaInhib,
            'inhibStrength': self.inhibStrength,
            'zeta': self.zeta
        }

    def _conditional_log_densities(self, stimuli, fixations, verbose=False):
        data = []
        data_locations = []
        stimulus_mapping = {}
        #print("preparing data")
        for i in tqdm(range(len(fixations.x)), disable=not verbose):

            n = fixations.n[i]
            if n not in stimulus_mapping:
                stimulus = stimuli[n]

                # SceneWalker expects the saliency map to be in "linear units", i.e. linear to probabilities
                saliency_map = np.exp(self.base_model.log_density(stimulus))

                size = np.array(stimulus.size, dtype=float)
                deg_size = size / self.pixel_per_dva

                data.append({
                    'saliency': saliency_map,
                    'deg_size': deg_size,
                    'scanpaths': []
                })
                stimulus_mapping[n] = len(data) - 1

            stimulus_data = data[stimulus_mapping[n]]

            length = fixations.lengths[i]
            x_hist = fixations.x_hist[i, :length]
            y_hist = fixations.y_hist[i, :length]
            t_hist = fixations.t_hist[i, :length]

            next_t = fixations.t[i]
            last_duration = next_t - t_hist[-1]

            _fixations = np.array([x_hist, y_hist]).T.astype(float)
            _fixations = np.vstack((_fixations, [0, 0]))  # we need to ask for another fixation to get the conditional probability
            _fixations /= self.pixel_per_dva

            times = np.array(t_hist)
            durations = np.diff(times)   # scene walker needs durations, not times
            durations = np.hstack((durations, [last_duration, 0.5]))  # we are missing the duration for the last fixation and need another fake fixation

            stimulus_data['scanpaths'].append({
                'fixations': _fixations,
                'times': durations
            })

            data_locations.append({'image_no': stimulus_mapping[n], 'scanpath_no': len(stimulus_data['scanpaths']) - 1})

        results = evaluate_scanpaths_hdf5(
            data = data,
            directory = self.temporary_directory,
            scene_walker_directory = os.path.join(self.location, 'paperCode'),
            execute = self.execute,
            variables = ['last_us'],
            params=self.params,
            verbose=verbose,
            model=self._model_function
        )

        conditional_log_densities = []

        #print("aggregating conditionial densities")
        for i in tqdm(range(len(fixations.x)), disable=not verbose):
            position = data_locations[i]
            conditional_density = results[position['image_no']][position['scanpath_no']]['last_us']  # [:, :, -2]
            conditional_log_density = np.log(conditional_density)
            conditional_log_density -= logsumexp(conditional_log_density)
            conditional_log_densities.append(conditional_log_density)

        return conditional_log_densities

    def conditional_log_density(self, stimulus, x_hist, y_hist, t_hist, out=None, durations=None, last_duration=0.3):
        stimuli = Stimuli([stimulus.stimulus_data])
        #fixations = Fixations(
        #    x=np.array([x_hist[-1]]),
        #    y=np.array([y_hist[-1]]),
        #    t=np.array([t_hist[-1]]),
        #    x_hist=np.array([x_hist[:-1]]),
        #    y_hist=np.array([y_hist[:-1]]),
        #    t_hist=np.array([t_hist[:-1]]),
        #    n=np.array([0], int),
        #    subjects=np.array([0], int),
        #)
        fixations = Fixations(
            x=np.zeros((1, )),
            y=np.zeros((1, )),
            t=np.zeros((1, ))+t_hist[-1]+last_duration,
            x_hist=np.array([x_hist]),
            y_hist=np.array([y_hist]),
            t_hist=np.array([t_hist]),
            n=np.array([0], int),
            subjects=np.array([0], int),
        )
        return self._conditional_log_densities(stimuli, fixations)[0]

    def log_likelihoods(self, stimuli, fixations, verbose=False):
        log_likelihoods = np.empty(len(fixations.x))
        inds = range(len(fixations.x))
        with tqdm(total=len(fixations.x), disable=not verbose) as t:
            for ind_chunk in chunked(inds, 1000):
                _f = fixations[ind_chunk]
                conditional_log_densities = self._conditional_log_densities(stimuli, _f)
                for k, i in enumerate(ind_chunk):
                    log_likelihoods[i] = conditional_log_densities[k][fixations.y_int[i], fixations.x_int[i]]
                t.update(len(ind_chunk))

        return log_likelihoods


class SceneWalkerEngbert(SceneWalker):
    """The SceneWalker model

    .. seealso::
        TODO
    """

    def __init__(self,
                 base_model, pixel_per_dva, temporary_directory,
                 omega=10**(-4.1722)*100,
                 rho=10**(-0.8343)*100,
                 sigmaAttention=6.1036,
                 sigmaInhib=2.1319,
                 gamma=.3,
                 lambda_=1,
                 inhibStrength=1,
                 zeta=0.04,
                 location=None,
                 execute=execute,
                 **kwargs):
        super(SceneWalkerEngbert, self).__init__(
            base_model,
            pixel_per_dva,
            temporary_directory,
            omega=omega,
            rho=rho,
            sigmaAttention=sigmaAttention,
            sigmaInhib=sigmaInhib,
            gamma=gamma,
            lambda_=lambda_,
            inhibStrength=inhibStrength,
            zeta=zeta,
            location=location,
            execute=execute,
            **kwargs
        )


class SceneWalkerDivisive(SceneWalker):
    """The SceneWalker model

    .. seealso::
        TODO
    """

    def __init__(self,
                 base_model, pixel_per_dva, temporary_directory,
                 omega=np.exp(0.1795),
                 rho=np.exp(6.7791),
                 sigmaAttention=np.exp(1.5225)*np.exp(0.4028),
                 sigmaInhib=np.exp(1.6466)*np.exp(2.3420),
                 gamma=np.exp(2.3420),
                 lambda_=np.exp(0.4028),
                 inhibStrength=np.exp(-9.8428),
                 zeta=np.exp(-3.0874),
                 location=None,
                 execute=execute,
                 **kwargs):
        super(SceneWalkerDivisive, self).__init__(
            base_model,
            pixel_per_dva,
            temporary_directory,
            omega=omega,
            rho=rho,
            sigmaAttention=sigmaAttention,
            sigmaInhib=sigmaInhib,
            gamma=gamma,
            lambda_=lambda_,
            inhibStrength=inhibStrength,
            zeta=zeta,
            location=location,
            execute=execute,
            **kwargs
        )
        self._model_function = 'dynamic_model_divisive'
