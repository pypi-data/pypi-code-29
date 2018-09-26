
"""Module for visualizing the derivative of heart rate over 24 hours.
"""

################################### Imports: ###################################

# Need to do this to prevent warnings/errors when saving a batch of clocks:
import matplotlib
matplotlib.use('Qt4Agg')  # adds improved zoom over default backend
# matplotlib.use('GTKCairo')  # switch to vector graphics
# matplotlib.use('GTKAgg')  # nothing fancy over default.  similar to WXAgg.

import numpy as np
import multiprocessing as mp
from dateutil import parser

from .ecgclock import ECGClock
from .ann_loaders import load_from_csv
from .utils import times_to_angles, medfilt, polar_interp, angle_to_time, \
    general_filter, derivative

################################# Main Class: ##################################

class HRDerivClock(ECGClock):
    def __init__(self, title=None,
                 min_rad=-2, max_rad=2,
                 tick_spacing=0.5,
                 color_cycle=['b', 'm', 'c', 'k', 'y'],
                 parent_figure=None,
                 subplot=1):
        """Create an axis for plotting heart rate derivative.

        Keyword arguments:
        title -- axis title
        min_rad, max_rad -- radial lower and upper bound.    +/-3 may be better for percent change.
        tick_spacing -- distance between radial ticks/gridlines.  1.0 may be better for percent change.
        color_cycle -- order of colors to use for each line added to the plot
        parent_figure -- larger figure that hosts this clock as a subplot
        subplot -- which subplot of larger figure this clock occupies
        """
        # Save args to pass on:
        locals_minus_self = locals()
        locals_minus_self.pop('self', None)
        locals_minus_self.pop('tick_spacing', None)  # because superclass doesn't have this option yet

        #super(HRDerivClock, self).__init__( **locals_minus_self )  # python 2
        #super().__init__( **locals_minus_self )  # python 3?
        ECGClock.__init__(self, **locals_minus_self )  # python 2 or 3, maybe

        self.ax.format_coord = self.format_coord  # TODO!!!!: make 'percent' an
                                                  # arg of this, not add_rec().
                                                  # then fix format_coord units.
        self.ax.set_yticks( np.arange(min_rad,max_rad,tick_spacing) )  # TODO: endpoint.

    def add_recording_from_csv(self, filename, label=None, color=None, filtering=10,
                               auto_fit=False, min_max=True, percent=False):
        """Read HR dataset from file (assumed to be in bpm), take derivative, and add it
        to the plot.  If there are large gaps in time, data points in between
        will be interpolated.

        Keyword arguments:
        filename -- csv to read data from
        label -- what to call this on the plot legend
        color -- line color (or None to follow normal rotation)
        filtering -- width of filter in minutes, or 0 to disable filtering
        auto_fit -- re-scale radial axis to fit this data
        min_max -- rather than plotting the values, plot the min/max envelope of the values
        percent -- plot the percent change rather than the absolute change
        """
        # TODO: change this to properly override add_recording() and add_recording_from_csv()
        # TODO: normalize to HR, i.e. pct change rather than bpm change?
        # TODO: could default None label to filename
        times, values = load_from_csv(filename)
        angles = times_to_angles(times)
        if filtering:
            values = medfilt( times, values, filter_width=filtering )

        values = derivative( times, values, percent=percent )
        # TODO: postfilt here?  tough not to clobber everything if we do.  e.g.:
        # values = medfilt( times, values, filter_width=0.07 )  # testing

        if (auto_fit):
            self.ax.set_ylim( min(values), max(values) )
            self.ax.set_yticks( np.linspace(min(values), max(values), 7) )

        if (not min_max):
            interp_angles, interp_values = polar_interp( angles, values )
            self.ax.plot(interp_angles, interp_values, zorder=0, color=color, label=label)
            # Splitting up into two colors (above and below zero):
            # pos_slope = [x if (x > 0) else np.nan for x in interp_values]
            # neg_slope = [x if (x < 0) else np.nan for x in interp_values]
            # self.ax.plot(interp_angles, pos_slope, zorder=0, color=color, label=label)
            # self.ax.plot(interp_angles, neg_slope, zorder=0, color=color, label=label)
        else:
            # TODO: color option
            upper_bounds = general_filter( times, values, filter_width=20, filt_type=max )
            lower_bounds = general_filter( times, values, filter_width=20, filt_type=min )
            interp_angles, interp_values = polar_interp( angles, upper_bounds )
            self.ax.plot(interp_angles, interp_values, zorder=0, color='r')
            #self.ax.plot(angles, upper_bounds, zorder=0, color='r')  # no interp
            interp_angles, interp_values = polar_interp( angles, lower_bounds )
            self.ax.plot(interp_angles, interp_values, zorder=0, color='r')
            #self.ax.plot(angles, lower_bounds, zorder=0, color='r')  # no interp

    def format_coord(self, th, r):
        """Return a human readable string from a (theta, r) coordinate."""
        return 'time=' + angle_to_time(th) + ', dHR/dt=%1.2fbpm/sec'%(r)

################################################################################
