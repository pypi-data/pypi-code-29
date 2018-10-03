#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Victor Calderon
# Created      : 2018-10-03
# Last Modified: 2018-10-03
from __future__ import absolute_import, division, print_function
__author__     = ['Victor Calderon']
__copyright__  = ["Copyright 2018 Victor Calderon"]
__email__      = ['victor.calderon@vanderbilt.edu']
__maintainer__ = ['Victor Calderon']
__all__        = [  "HOD"]

## Import modules
import numpy as np
import pandas as pd
from   scipy                         import special, stats
from   cosmo_utils.utils             import stats_funcs
from   cosmo_utils.utils             import file_utils as fd
from   cosmo_utils.custom_exceptions import LSSUtils_Error

## Functions and classes

## Calculations of HOD parametrs

class HOD(object):
    """
    Computes various statistics corresponding to a given set of HOD parameters.
    HOD stands for `Halo Occupation Distribution`
    [http://arxiv.org/abs/astro-ph/0109001].
    """
    def __init__(self, **kwargs):
        """
        Parameters
        -----------
        log_m0 : `float`
            Halo mass, below which there are no satellite galaxies.
        
        log_m1 : `float`
            Mass scale where haloes contain one satellite galaxy on average.

        log_Mmin : `float`
            Minimum halo mass that can host a `central` galaxy.

        sigma_logM : `float`
            Scatter around `Mmin`

        log_alpha : `float`
            Slope of the power-law occupation function at high masses.
        """
        super().__init__()
        # Assigning variables
        self.log_m0               = kwargs.get('log_m0', 12.25)
        self.log_m1               = kwargs.get('log_m1', 12.56)
        self.log_Mmin             = kwargs.get('log_Mmin',  11.36)
        self.sigma_logM           = kwargs.get('sigma_logM',  0.14)
        self.alpha                = kwargs.get('alpha',  0.90)
        self.m0                   = 10.**self.log_m0
        self.m1                   = 10.**self.log_m1
        self.Mmin                 = 10.**self.log_Mmin
        # Extra variables
        self.hod_params           = self._retrieve_hod_params_dict()
        self.mass_bin             = kwargs.get('mass_bin', 0.4)
        self.n_draws              = kwargs.get('n_draws', 1000)
        self.log_mhalo_min        = kwargs.get('log_mhalo_min', 10.)
        self.log_mhalo_max        = kwargs.get('log_mhalo_max', 15.)
        # Arrays
        self.log_mhalo_arr        = self._log_mhalo_arr_create()
        self.log_mhalo_bins       = self._log_mhalo_bins_create()
        self.log_mhalo_repeat_arr = self._log_mhalo_repeat_arr_create()
        self.rands_arr            = self._random_arr_create()

    # Average number of central galaxies as function of halo mass.
    def ncen_avg(self):
        """
        Computes the average number of `central` galaxies  as function of
        halo mass.

        Returns
        -----------
        ncen_avg_arr : `numpy.ndarray`
            Array of average number of central galaxies as function of
            halo mass.
        """
        # Special error function component
        erf_component = (self.log_mhalo_repeat_arr - self.log_Mmin)
        erf_component /= self.sigma_logM
        # Average number of centrals
        ncen_avg_arr = 0.5 * (1. + special.erf(erf_component))

        return ncen_avg_arr

    # Average number of satellite galaxies as function of halo mass.
    def nsat_avg(self):
        """
        Computes the average number of `central` galaxies  as function of
        halo mass.

        Returns
        -----------
        nsat_avg : `numpy.ndarray`
            Array of average number of central galaxies as function of
            halo mass.
        """
        # Array of halo masses
        mass_repeat_arr     = 10**self.log_mhalo_repeat_arr
        # Average number of centrals
        ncen_avg_arr = self.ncen_avg()
        # Average number of satellite galaxies
        nsat_component = ((mass_repeat_arr - self.m0)/self.m1)**(self.alpha)
        nsat_avg_arr   = ncen_avg_arr * nsat_component
        # Replacing NaN's with zeros
        nsat_avg_arr[np.isnan(nsat_avg_arr)] = 0.

        return nsat_avg_arr

    # Average number of galaxies (centrals and satellites) as function of halo
    # mass.
    def ngals_avg(self, arr_len=10, bin_statval='left',
        return_pd_dict=True):
        """
        Computes the average number of galaxies (centrals + satellites) as
        function of halo mass.

        Parameters
        -----------
        arr_len :   `init`, optional
            Minimum number of elements in each bin of `x`. This variable
            is set to `0` by default.

        return_pd_dict : `bool`
            If True, it returns a dictionary with `pd.DataFrames` for
            each of the statistics.

        Returns
        ---------
        ngals_dict : `dict`
            Dictionary containing information about the `mean`/`average`
            number of 1) central, 2) satellite, and 3) total number of galaxies
            based on a given set of HOD parameters. The keys of the resulting
            dicitonaries are:
            ['ncen_avg_data', 'nsat_avg_data', 'ncen_binned',
                'nsat_binned','ngal_binned']

        Notes
        -------
        Each of the data in `ngals_dict` consists of two columns, with the
        first element corresponding to logarithmic halo masses, and the second
        to the statistic observed.
        """
        # Average number of central galaxies
        ncen_avg_arr = self.ncen_avg()
        # Average number of satellite galaxies
        nsat_avg_arr = self.nsat_avg()
        # Total number of central galaxies
        n_cen_arr = (ncen_avg_arr / self.rands_arr).astype(int)
        n_cen_arr[np.nonzero(n_cen_arr)] = int(1)
        # Total number of satellite galaxies
        n_sat_arr = np.array([np.random.poisson(nsat_avg_arr[ii])
                        if ((ncen_avg_arr[ii] != 0) and (nsat_avg_arr[ii] > 0))
                        else 0 for ii in range(len(n_cen_arr))])
        # Total number of galaxies
        n_gal_arr = n_cen_arr + n_sat_arr
        # Average number of galaxies as function of halo mass - Binning
        (   log_mhalo_repeat_mean_ngals,
            n_gal_mean_binned,
            n_gal_std_binned,
            n_gal_std_err_binned) = stats_funcs.Stats_one_arr(
                                        self.log_mhalo_repeat_arr,
                                        n_gal_arr,
                                        base=self.mass_bin,
                                        arr_digit='n',
                                        arr_len=arr_len,
                                        bin_statval=bin_statval)
        # Binning average number of central galaxies
        (   log_mhalo_repeat_mean_ncen,
            ncen_mean_binned,
            ncen_std_binned,
            ncen_std_err_binned) = stats_funcs.Stats_one_arr(
                                        self.log_mhalo_repeat_arr,
                                        n_cen_arr,
                                        base=self.mass_bin,
                                        arr_digit='n',
                                        arr_len=arr_len,
                                        bin_statval=bin_statval)
        # Binning average number of satellite galaxies
        (   log_mhalo_repeat_mean_nsats,
            nsats_mean_binned,
            nsats_std_binned,
            nsats_std_err_binned) = stats_funcs.Stats_one_arr(
                                        self.log_mhalo_repeat_arr,
                                        n_sat_arr,
                                        base=self.mass_bin,
                                        arr_digit='n',
                                        arr_len=arr_len,
                                        bin_statval=bin_statval)
        # Constructing DataFrames
        if return_pd_dict:
            # Average number of central galaxies
            ncen_avg_data = pd.DataFrame({
                                    'log_mhalo':self.log_mhalo_repeat_arr,
                                    'ncen_avg': ncen_avg_arr})
            # Average number of satellite galaxies
            nsat_avg_data = pd.DataFrame({
                                    'log_mhalo':self.log_mhalo_repeat_arr,
                                    'nsat_avg': nsat_avg_arr})
            # Average number of galaxies (cens + sats)
            ngal_binned = pd.DataFrame({
                                    'log_mhalo':log_mhalo_repeat_mean_ngals,
                                    'ngal_avg': n_gal_mean_binned})
            # Binned central galaxies
            ncen_binned = pd.DataFrame({
                                    'log_mhalo':log_mhalo_repeat_mean_ncen,
                                    'ncen_binned': ncen_mean_binned})
            # Binned satellite galaxies
            nsat_binned = pd.DataFrame({
                                    'log_mhalo':log_mhalo_repeat_mean_nsats,
                                    'nsat_binned': nsats_mean_binned})
        else:
            # Averages
            ncen_avg_data = np.column_stack((   self.log_mhalo_repeat_arr,
                                                ncen_avg))
            nsat_avg_data = np.column_stack((   self.log_mhalo_repeat_arr,
                                                nsat_avg))
            # Binned data
            ncen_binned = np.column_stack((log_mhalo_repeat_mean_ncen,
                                            ncen_mean_binned))
            nsat_binned = np.column_stack((log_mhalo_repeat_mean_nsats,
                                            nsats_mean_binned))
            ngal_binned = np.column_stack((log_mhalo_repeat_mean_ngals,
                                            n_gal_mean_binned))
        #
        # Saving as dictionary
        ngals_dict = {}
        ngals_dict['ncen_avg_data'] = ncen_avg_data
        ngals_dict['nsat_avg_data'] = nsat_avg_data
        ngals_dict['ncen_binned'  ] = ncen_binned
        ngals_dict['nsat_binned'  ] = nsat_binned
        ngals_dict['ngal_binned'  ] = ngal_binned

        return ngals_dict

    # Creating random number of halo masses
    def _log_mhalo_bins_create(self):
        """
        Creates an array of fictitious halo masses.

        Returns
        --------
        log_mhalo_bins : `numpy.ndarray`
            Array of bin edges of logarithmic halo masses.
        """
        log_mhalo_bins = stats_funcs.Bins_array_create( [self.log_mhalo_min,
                                                        self.log_mhalo_max],
                                                        base=self.mass_bin)

        return log_mhalo_bins

    def _log_mhalo_arr_create(self):
        """
        Creates an array of fictitious halo masses.

        Returns
        --------
        log_mhalo_arr : `numpy.ndarray`
            Array of fictitious logarithmic halo masses.
        """
        # Constants
        log_mhalo_arr = np.random.uniform(  self.log_mhalo_min,
                                            self.log_mhalo_max,
                                            self.n_draws)

        return log_mhalo_arr

    def _log_mhalo_repeat_arr_create(self):
        """
        Creates a tiled version of `log_mhalo_arr` array.

        Returns
        ---------
        log_mhalo_repeat_arr : `numpy.ndarray`
            Tiled array of logarithmic halo masses
        """
        log_mhalo_repeat_arr = np.tile(self.log_mhalo_arr, self.n_draws)

        return log_mhalo_repeat_arr

    def _random_arr_create(self):
        """
        Creates an array of random floats [0,1] with specified shape.

        Returns
        ---------
        rands_arr : `numpy.ndarray`
            Array of random float with specified shape.
        """
        rand_shape = len(self.log_mhalo_repeat_arr)
        rands_arr  = np.random.random(rand_shape)

        return rands_arr


    def _retrieve_hod_params_dict(self):
        """
        Produced a dictionary with the HOD parameters

        Returns
        --------
        hod_params : `dict`
            Dictionary containing the sets of HOD parameters.
        """
        # Define dictionary
        hod_params = {}
        hod_params['log_m0'    ] = self.log_m0
        hod_params['log_m1'    ] = self.log_m1
        hod_params['log_Mmin'  ] = self.log_Mmin
        hod_params['sigma_logM'] = self.sigma_logM
        hod_params['alpha'     ] = self.alpha
        hod_params['m0'        ] = 10**self.log_m0
        hod_params['m1'        ] = 10**self.log_m1
        hod_params['Mmin'      ] = 10**self.log_Mmin

        return hod_params
