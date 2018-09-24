#
# Project Librarian: Alex Urban
#              Graduate Student
#              UW-Milwaukee Department of Physics
#              Center for Gravitation & Cosmology
#              <alexander.urban@ligo.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Module to define functions and attributes corresponding 
to both gravitational-wave candidates and external triggers.
"""
__author__ = "Alex Urban <alexander.urban@ligo.org>"


# Imports.
import numpy as np
import healpy as hp
import VOEventLib.VOEvent
import VOEventLib.Vutil

from ligo.gracedb.rest import GraceDb, DEFAULT_SERVICE_URL
from lalinference.io import fits


###################################
# Functions for external triggers #
###################################

def kappa(err):
    """ Approximant to the von Mises-Fisher concentration parameter """
    R = np.exp( -err**2 / 2 )
    return R * (3 - R**2) / (1 - R**2)

def pdf(n, nside, theta0, phi0, err):
    """ Posterior probability density function for the sky location of the
        external trigger, fit to a von Mises-Fisher distribution on the unit
        sphere. """
    # If you're already in the most probable pixel, return unity.
    if n == hp.ang2pix(nside, theta0, phi0): return 1.

    # Otherwise, calculate and return the unnormalized probability in this pixel.
    else:
        k = kappa(err)
        th, ph = hp.pix2ang(nside, n)
        xi = k * ( ( np.sin(theta0) * np.sin(th) * np.cos(ph - phi0) ) + ( np.cos(theta0) * np.cos(th) ) - 1 )
        return np.exp( xi )


#######################################################
# Define object classes for GWs and external triggers #
#######################################################

class ExtTrig(object):
    """ Instance of an external trigger event (i.e. gamma-ray burst) """
    def __init__(self, graceid, gracedb=None, search_for_gw_triggers=False):
        self.graceid = graceid
        if search_for_gw_triggers:
            self.neighbor_type = 'G'
        else:
            self.neighbor_type = 'S' # by default, look for coincident superevents
        self.fits = '{0}.fits.gz'.format(self.graceid) # name of .fits file for this event

        # Initiate correct instance of GraceDb.
        if gracedb is None:
            self.gracedb = GraceDb( DEFAULT_SERVICE_URL ) 
        else:
            self.gracedb = gracedb

        # Inherit other properties from GraceDb.
        event = list(self.gracedb.events(query=self.graceid))[0]
        self.RA = event['extra_attributes']['GRB']['ra']  # right ascention
        self.dec = event['extra_attributes']['GRB']['dec']  # declination
        self.err_rad = event['extra_attributes']['GRB']['error_radius']  # error radius
        self.t90 = event['extra_attributes']['GRB']['T90']  # T90
        self.inst = event['pipeline']  # instrument that detected the event
        self.gpstime = float( event['gpstime'] )  # event time in GPS seconds
        # FIXME: GPS times in GraceDB. We will also need support for non-GRBs (e.g., Supernovae).

    def submit_gracedb_log(self, message, filename=None, tagname=None):
        """ Wrapper for gracedb.writeLog() for this event """
        if filename is not None: self.gracedb.writeLog(self.graceid, message, filename, tagname=tagname)
        else: self.gracedb.writeLog(self.graceid, message, tagname=tagname)

    def sky_map(self, nside):
        """ Returns a numpy array equivalent to the one that would get written
            to a FITS file for this event, with resolution nside """
        # convert RA, dec and error radius to standard spherical coordinates
        theta, phi, err = np.deg2rad( (90. - self.dec, self.RA, self.err_rad) )

        # calculate the probability distribution and store it in a skymap
        npix = hp.nside2npix(nside)
        trig_map = np.array( [pdf(i, nside, theta, phi, err) for i in range(npix)] )
        trig_map /= np.sum(trig_map) # normalize

        return trig_map

    def write_fits(self, nside, publish=False):
        """ Write a FITS file containing the sky map for this event, with resolution nside,
            and upload to GraceDB if the 'publish' flag is passed """ 

        # Write to a .fits file.
        fits.write_sky_map(self.fits, self.sky_map(nside), objid=self.graceid, gps_time=self.gpstime)

        # Publish to GraceDB if the 'publish' flag is passed.
        if publish: self.submit_gracedb_log(self.graceid, "RAVEN: Uploaded sky map",
            filename=self.fits, tagname="sky_loc")


class GW(object):
    """ Instance of a gravitational-wave candidate event """
    def __init__(self, graceid, fitsfile=None, gracedb=None):
        self.graceid = graceid # graceid of GW candidate
        self.neighbor_type = 'E'
        self.fits = fitsfile # name of fits file

        if self.fits:
            self.sky_map = fits.read_sky_map( self.fits )

        # Initiate correct instance of GraceDb.
        if gracedb is None:
            self.gracedb = GraceDb( DEFAULT_SERVICE_URL )
        else:
            self.gracedb = gracedb

        # Inherit the FAR and event time from GraceDb.
        event = list(self.gracedb.events(query=self.graceid))[0]
        self.far = event['far']
        self.gpstime = float( event['gpstime'] )

    def submit_gracedb_log(self, message, tagname=None):
        """ wrapper for gracedb.writeLog() for this event """
        self.gracedb.writeLog(self.graceid, message, tagname=tagname)


class SE(object):
    """Instance of a superevent"""
    def __init__(self, superevent_id, fitsfile=None, gracedb=None):
        self.graceid = superevent_id
        self.neighbor_type = 'E'
        self.fits = fitsfile # name of fits file

        if self.fits:
            self.sky_map = fits.read_sky_map( self.fits )

        if gracedb is None:
            self.gracedb = GraceDb( DEFAULT_SERVICE_URL )
        else:
            self.gracedb = gracedb

        # Inherit the FAR and event time of the preferred event from GraceDb.
        superevent = self.gracedb.superevent(self.graceid).json()
        self.preferred_event = superevent['preferred_event']
        preferred_event = list(self.gracedb.events(query=self.preferred_event))[0]
        self.far = preferred_event['far']
        self.gpstime = float( preferred_event['gpstime'] )

    def submit_gracedb_log(self, message, tagname=None):
        """ wrapper for gracedb.writeLog() for this event """
        # Right now, the ext_coinc tag does not exist for superevent log comments, but no error is generated
        self.gracedb.writeLog(self.graceid, message, tagname=tagname)
