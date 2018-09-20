#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:25:41 2018

@author: ghiles.reguig
"""

from sklearn.base import BaseEstimator, TransformerMixin
from nibabel.freesurfer import read_annot
import numpy as np
#from nipype import Node, Function
import nipype.interfaces.base.traits_extension as trait
from nipype.interfaces.base.core import LibraryBaseInterface,SimpleInterface
from nipype.interfaces.base import BaseInterfaceInputSpec, TraitedSpec
#from nilearn.surface import load_surf_data
from nilearn.surface import load_surf_data
from nilearn.signal import clean
import pandas as pd
import os
from os.path import join as opj


def extract_hemisphere_time_series(surf_data, mask_array):
    """
    Function for time-series extraction from a mask array
    """
    #remove 0 for gordon  roi_indices = np.unique(mask_array)[1:]
    roi_indices = np.unique(mask_array)
    masks_RoI = [mask_array == roi_num for roi_num in roi_indices]
    time_series= [[np.mean(frame*mask) for frame in surf_data.T]
                                            for mask in masks_RoI]
    return np.asarray(time_series)


class SurfaceMasker(BaseEstimator, TransformerMixin):

    """
    Class for time-series extraction from surface data
    """

    def __init__(self, annot_file):
        self.mask, _, self.names = read_annot(annot_file)

    def fit(self, X=None, y=None):
        return self

    def transform(self, X):
        return extract_hemisphere_time_series(X, self.mask)

    def get_names(self):
        return self.names


class NilearnBaseInterface(LibraryBaseInterface):
    _pkg = 'nilearn'

class ExtractTimeSeriesInputSpec(BaseInterfaceInputSpec):

    lh_surf = trait.traits.Str(mandatory=True, desc="Name of the file of the left hemisphere data")
    rh_surf = trait.traits.Str(mandatory=True, desc="Name of the file of the right hemisphere data")
    lh_annot = trait.traits.Str(mandatory=True, desc="Name of the file of the left hemisphere annotation")
    rh_annot = trait.traits.Str(mandatory=True, desc="Name of the file of the right hemisphere annotation")
    output_dir = trait.traits.Str(mandatory=True, desc="Name of the output directory")
    prefix = trait.traits.Str(mandatory=True, desc="Prefix of the while to write the time series in")
    confounds = trait.traits.Array(exists=True, mandatory=False, usedefault=None,
                           desc="Array containing fMRI confounds for signal cleaning")
    confoundsName = trait.traits.Str(mandatory=True, desc="Name of the set of confounds used")


class ExtractTimeSeriesOutputSpec(TraitedSpec):
    time_series = trait.traits.Array(desc="Array containing time series/RoI. Dimensions : (timestamps x RoI)")
    names = trait.traits.List(desc="List of labels associated with each RoI")
    confoundsName = trait.traits.Str(desc="Name of the set of confounds used for signal cleaning")


class ExtractTimeSeries(NilearnBaseInterface, SimpleInterface):
    input_spec = ExtractTimeSeriesInputSpec
    output_spec = ExtractTimeSeriesOutputSpec

    def _run_interface(self, runtime):
        lh_mask, _, lh_names = read_annot(self.inputs.lh_annot)
        rh_mask, _, rh_names = read_annot(self.inputs.rh_annot)
        lh_names, rh_names = lh_names[1:], rh_names[1:]
        lh_surf_data = load_surf_data(self.inputs.lh_surf)
        rh_surf_data = load_surf_data(self.inputs.rh_surf)
        #print("Extracting signal with confounds {} : {}".format(self.inputs.confoundsName, self.inputs.confounds))
        time_series_lh = extract_hemisphere_time_series(lh_surf_data, lh_mask)
        time_series_rh = extract_hemisphere_time_series(rh_surf_data, rh_mask)
        time_series = np.concatenate((time_series_lh, time_series_rh)).T
        to_delete = np.where(time_series.sum(axis=0)==0)
        #print("To delete: {}".format(to_delete))
        time_series = np.delete(time_series, to_delete, axis=1)
        #names = [n for i, n in enumerate(lh_names) if i not in to_delete[0]]
        names = np.concatenate((lh_names, rh_names))
        names = [n for i, n in enumerate(names) if i not in to_delete[0]][-time_series.shape[1]:]
        if isinstance(self.inputs.confounds, np.ndarray):
            time_series = clean(time_series, confounds=self.inputs.confounds)
        #Saving data
        time_seriesDF = pd.DataFrame(time_series, columns=names)
        #Name of the OutPutFile
        directory = opj(self.inputs.output_dir,"time_series")
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception:
                print("exception makedirs")
        outFile = os.path.join(directory, self.inputs.prefix+self.inputs.confoundsName+"TimeSeriesRoI.tsv")
        time_seriesDF.to_csv(outFile, sep="\t", index=False)
        self._results["time_series"] = time_seriesDF.values
        self._results["names"] = list(time_seriesDF.columns)
        self._results["confoundsName"] = self.inputs.confoundsName
        return runtime

"""
def get_time_series_extractor_node():

    return Node(Function(function=extract_time_series,
                         input_names=["lh_surf","rh_surf", "lh_annot","rh_annot", "output_dir","prefix", "confoundsName"],
                         output_names=["time_series", "roiLabels","confName"]), name="SurfaceTimeSeriesExtractor")
"""
####################### T E S T #############
"""
gordonLAnnot = ("/export/dataCENIR/users/ghiles.reguig/AtlasGordon/"
                "Gordon333_FSannot/lh.Gordon333.annot")
gordonRAnnot = ("/export/dataCENIR/users/ghiles.reguig/AtlasGordon/"
                "Gordon333_FSannot/rh.Gordon333.annot")

pBoldL = ("/export/dataCENIR/users/ghiles.reguig/testBIDSB0/derivatives/"
          "fmriprep/sub-10109PAR/ses-M0/func/"
          "sub-10109PAR_ses-M0_task-rest_bold_space-fsaverage.L.func.gii")


pBoldR = ("/export/dataCENIR/users/ghiles.reguig/testBIDSB0/derivatives/"
          "fmriprep/sub-10109PAR/ses-M0/func/"
          "sub-10109PAR_ses-M0_task-rest_bold_space-fsaverage.R.func.gii")

time_series, names, confs = extract_time_series(pBoldL, pBoldR, gordonLAnnot, gordonRAnnot, output_dir=".",prefix="", confounds=np.ones((250,1)))

boldFuncL = load_surf_data(pBoldL)
boldFuncR = load_surf_data(pBoldR)

surf_masker_l = SurfaceMasker(gordonLAnnot)
surf_masker_r = SurfaceMasker(gordonRAnnot)

surf_data_roi = np.concatenate((surf_masker_l.fit_transform(boldFuncL),
                                surf_masker_r.fit_transform(boldFuncR)))

n = get_time_series_extractor_node()
n.inputs.lh_surf = pBoldL
n.inputs.rh_surf = pBoldR
n.inputs.lh_annot = gordonLAnnot
n.inputs.rh_annot = gordonRAnnot
"""
