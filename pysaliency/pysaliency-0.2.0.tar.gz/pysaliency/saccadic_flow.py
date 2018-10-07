import os.path
from boltons.fileutils import mkdir_p
from tqdm import tqdm

import numpy as np
import pandas as pd
from scipy.misc import logsumexp

from executor import execute


def evalute_saccades(saccades, aspect_ratio, source_directory, tmp_directory, flow_model='tN', trained_on='ALL'):
    """
    saccades: dataframe with columns x1, x2, y1, y2 in relative coordinates x=(-1 .. 1), y=[-aspect_ratio .. aspect_ratio]
              and integer index
    """

    tmp_directory = os.path.abspath(tmp_directory)
    mkdir_p(tmp_directory)

    saccades = saccades[['x1', 'y1', 'x2', 'y2']]

    saccades_file = os.path.join(tmp_directory, 'saccades.csv')
    saccades[['x1', 'y1', 'x2', 'y2']].to_csv(os.path.join(tmp_directory, 'saccades.csv'), header=False)

    results_file = os.path.join(tmp_directory, 'results.csv')

    r_script = [
        "source('scripts/flowDistFunctions.R')",
        "print('reading data')",
        f"saccades = read.csv('{saccades_file}', header=FALSE)",
        "names(saccades) = c(\"n\", \"x1\", \"y1\", \"x2\", \"y2\")",
        "print('computing')",
        f"result = calcLLHofSaccades(saccades, '{flow_model}', '{trained_on}', {aspect_ratio})",
        "print('saving results')",
        f"write.csv(result, '{results_file}')",
        "print('done')",
    ]

    script_file = os.path.join(tmp_directory, 'run.R')

    with open(script_file, 'w') as f:
        f.write('\n'.join(r_script))
        f.write('\n')

    cmd = f'Rscript "{script_file}"'

    #print(cmd)

    execute(cmd, directory=source_directory)

    results = pd.read_csv(results_file, index_col=0)

    return results


class SaccadicFlow(pysaliency.GeneralModel):
    def conditional_log_density(self, stimulus, x_hist, y_hist, t_hist, out=None):
        shape = np.shape(stimulus)
        height, width = (shape[0], shape[1])

        aspect_ratio = height/width

        x1 = x_hist[-1]
        y1 = y_hist[-1]

        xs = np.linspace(-1, 1, num=width, endpoint=False)
        ys = np.linspace(-aspect_ratio, aspect_ratio, num=height, endpoint=False)

        x1 = (x_hist[-1] / 0.5/width) - 1.0
        y1 = ((y_hist[-1] / 0.5/height) - 1.0) * aspect_ratio
        X, Y = np.meshgrid(xs, ys)

        df = pd.DataFrame({'x2': X.flatten(), 'y2': Y.flatten()})
        df['x1'] = np.ones(len(df))*x1
        df['y1'] = np.ones(len(df))*y1
        df = df[['x1', 'y1', 'x2', 'y2']]

        results = evalute_saccades(df, aspect_ratio=aspect_ratio, source_directory='ThirdParty/flow', tmp_directory='tmp/flow')

        lls = np.array(results.llh).reshape((height, width))

        normed_lls = lls + np.log(2*2*aspect_ratio)
        pixel_lls = normed_lls - np.log(height*width)
        pixel_lls -= logsumexp(pixel_lls)

        return pixel_lls

    def log_likelihoods(self, stimuli, fixations, verbose=False):

        llhs = np.empty(len(fixations.x))

        dfs = {}

        for n in tqdm(list(range(len(stimuli)))):
            inds = fixations.n == n
            height = stimuli.sizes[n][0]
            width = stimuli.sizes[n][1]

            aspect_ratio = height / width

            xs2 = fixations.x[inds].copy()
            ys2 = fixations.y[inds].copy()

            xs1 = fixations.x_hist[inds][np.arange(inds.sum()), fixations.lengths[inds]-1].copy()
            ys1 = fixations.y_hist[inds][np.arange(inds.sum()), fixations.lengths[inds]-1].copy()

            xs1 = (xs1 / 0.5/width) - 1.0
            ys1 = ((ys1 / 0.5/height) - 1.0) * aspect_ratio

            xs2 = (xs2 / 0.5/width) - 1.0
            ys2 = ((ys2 * 2.0 / height) - 1.0) * aspect_ratio

            df = pd.DataFrame({'x1': xs1, 'y1': ys1, 'x2': xs2, 'y2': ys2}, columns=['x1', 'y1', 'x2', 'y2'])

            results = evalute_saccades(df, aspect_ratio=aspect_ratio, source_directory='ThirdParty/flow', tmp_directory='tmp/flow')

            lls = np.array(results.llh)

            normed_lls = lls + np.log(2*2*aspect_ratio)
            pixel_lls = normed_lls - np.log(height*width)

            llhs[inds] = pixel_lls

        return llhs
