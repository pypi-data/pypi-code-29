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
Module containing time- and sky- coincidence search functions.
"""
__author__ = "Alex Urban <alexander.urban@ligo.org>"


# Imports.
import sys
import numpy as np
import healpy as hp
import re

from .gracedb_events import GW, SE, ExtTrig
from ligo.gracedb.rest import GraceDb, DEFAULT_SERVICE_URL


#######################################
# Functions for background estimation #
#######################################

def Cacc(rho_sky):
    """ Estimator for the cumulative fraction of accidental associations with
        sky coincidence better than psky. """
    if rho_sky < 1e-50: return 1.
    else:
        x = np.log10(rho_sky)
        p = [6.43375601e+00, -3.83233594e+04, 1.35768892e+01]
        return p[0] * x**3 / (p[1] + p[2]*x**3)



#########################################################
# Functions implementing the actual coincidence search. #
#########################################################

def query(event_type, gpstime, tl, th, gracedb=None, group=None, pipelines=None):
    """ Query for coincident events of type event_type occurring within a window
        of [tl, th] seconds around gpstime """

    # Perform a sanity check on the time window.
    if tl >= th:
        sys.stderr.write( "ERROR: The time window [tl, th] must have tl < th." )
        sys.exit(1)

    # Initiate correct instance of GraceDb.
    if gracedb is None:
        gracedb = GraceDb( DEFAULT_SERVICE_URL )

    # Perform the GraceDB query.
    start, end = gpstime + tl, gpstime + th
    
    if event_type!='Superevent':
        arg = '{0} {1} .. {2}'.format(event_type, start, end)
        # Return list of graceids of coincident events.
        try:
            results = list(gracedb.events(arg))
            if pipelines:
                for event in results:
                    event_pipeline = event['pipeline']
                    if event_pipeline not in pipelines:
                        results.remove(event)
                return results
            else:
                return results
        except:
            sys.stderr.write( "ERROR: Problem accessing GraCEDb while \
                calling gracedb.events()" )
            sys.exit(1)

    else: # We are searching for a superevent
        arg = '{0} .. {1}'.format(start, end)
        # Return list of coincident superevent_ids.
        try:
            results = list(gracedb.superevents(arg))
            if group:
                for superevent in results:
                    preferred_event_id = superevent['preferred_event']
                    preferred_event_group = gracedb.event(
                        preferred_event_id).json()['group']
                    if preferred_event_group != group:
                        results.remove(superevent)
                return results
            else:
                return results
        except:
            sys.stderr.write( "ERROR: Problem accessing GraCEDb while \
                calling gracedb.events()" )
            sys.exit(1)


def search(event, tl, th, gracedb=None, group=None, pipelines=None):
    """ Perform a search for neighbors coincident in time within
        a window [tl, th] seconds around an event """

    # Identify neighbor types with their graceid strings.
    types = {'G': 'GW', 'E': 'External trigger', 'S': 'Superevent trigger',
             'T': 'Test'}
    groups = {'G': 'CBC Burst', 'E': 'External', 'S': 'Superevent'}

    # Initiate correct instance of GraceDb.
    if gracedb is None:
        gracedb = GraceDb( DEFAULT_SERVICE_URL )

    # Grab any and all neighboring events. Filter results depending on the group if specified.
    neighbors = query(groups[event.neighbor_type], event.gpstime, tl, th,
                      gracedb=gracedb, group=group, pipelines=pipelines)

    # If no neighbors, report a null result.
    if not neighbors:
        if group:
            message = "RAVEN: No %s %s candidates in window [%+d, %+d] \
                seconds" % (types[event.neighbor_type], group, tl, th)
        elif pipelines:
            message = "RAVEN: No %s %s candidates in window [%+d, %+d] \
                seconds" % (types[event.neighbor_type], pipelines, tl, th)
        else:
            message = "RAVEN: No %s candidates in window [%+d, %+d] \
                seconds" % (types[event.neighbor_type], tl, th)
        event.submit_gracedb_log(message, tagname="ext_coinc")

    # If neighbors are found, report each of them.
    else:
        for neighbor in neighbors:
            if neighbor.get('graceid'):
                gid = neighbor['graceid']
                link1 = 'events/'
                link2 = 'superevents/'
            else:
                gid = neighbor['superevent_id']
                link1 = 'superevents/'
                link2 = 'events/'
            gracedb_url = re.findall('(.*)api/', gracedb.service_url)[0]
            if group:
                message1 = "RAVEN: {0} {1} candidate found: \
                    <a href='{2}{3}".format(types[event.neighbor_type],
                                            group, gracedb_url, link1)
            else:
                message1 = "RAVEN: {0} candidate found: \
                    <a href='{1}{2}".format(types[event.neighbor_type],
                                            gracedb_url, link1)
            message1 += "%s'>%s</a> within [%+d, %+d] seconds" % (gid, gid, 
                                                                  tl, th)
            event.submit_gracedb_log(message1, tagname="ext_coinc")
            try:
                gracedb.writeLabel(event.graceid, 'EM_COINC')
            except:
                pass

            if pipelines: 
                message2 = "RAVEN: {0} {1} event <a href='{2}{3}".format(
                    types[event.graceid[0]], pipelines, gracedb_url, link2)
            else:
                message2 = "RAVEN: {0} event <a href='{1}{2}".format(
                    types[event.graceid[0]], gracedb_url, link2)
            message2 += "%s'>%s</a> within window [%+d, %+d] seconds" % (
                event.graceid, event.graceid, tl, th)
            gracedb.writeLog(gid, message2, tagname="ext_coinc")
            try:
                gracedb.writeLabel(gid, 'EM_COINC')
            except:
                pass

    # Return search results.
    return neighbors


def calc_signif_gracedb(se, exttrig, tl, th, incl_sky=False):
    """ Calculate the improvement in significance that is got out of the second tier
        of this hierarchical coincidence search. """

    # The combined rate of independent GRB discovery by Swift and Fermi is 0.807 per day,
    # according to Urban et al., in prep.
    gcn_rate = 0.807 / (60 * 60 * 24)

    # Is the GW superevent candidate's FAR sensible?
    if not se.far:
        message = "RAVEN: WARNING: This GW superevent candidate's FAR is a NoneType object."
        se.submit_gracedb_log(message)
        return

    # Include sky coincidence if desired.
    gracedb_events_url = re.findall('(.*)api/', se.gracedb.service_url)[0] + 'events/'
    if incl_sky:
        nside = hp.npix2nside( len(se.sky_map) )
        psky = (4 * np.pi)**2 * np.sum( [x * y for x, y in zip(se.sky_map, exttrig.sky_map(nside))] ) / len(se.sky_map)
        far = (th - tl) * gcn_rate * Cacc( psky ) * se.far
        message = "RAVEN: Spatiotemporal coincidence with external trigger <a href='{0}".format(gracedb_events_url)
        message += "{0}'>{1}</a> gives a coincident FAR = {2} Hz".format(exttrig.graceid, exttrig.graceid, far)
        se.submit_gracedb_log(message, tagname="ext_coinc")
        return

    # Otherwise, proceed with only time coincidence.
    else:
        far = (th - tl) * gcn_rate * se.far
        message = "RAVEN: Temporal coincidence with external trigger <a href='{0}".format(gracedb_events_url)
        message += "{0}'>{1}</a> gives a coincident FAR = {2} Hz".format(exttrig.graceid, exttrig.graceid, far)
        se.submit_gracedb_log(message, tagname="ext_coinc")
        return
