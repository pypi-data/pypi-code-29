"""This module provides a class and supporting functions for visualizing
features from long-term ECG monitoring data.
"""

################################### Imports: ###################################

# Need to do this to prevent warnings/errors when saving a batch of clocks:
import matplotlib
matplotlib.use('Qt4Agg')  # adds improved zoom over default backend
# matplotlib.use('GTKCairo')  # switch to vector graphics
# matplotlib.use('GTKAgg')  # nothing fancy over default.  similar to WXAgg.

import numpy as np
from cycler import cycler

from .ecgfigure import ECGFigure
from .ecgmeasurements import ECGMeasurements
from .utils import angle_to_time, time_to_angle, times_to_angles, \
    polar_interp, medfilt, sec_to_msec
from .cohort import Cohort

################################# Main Class: ##################################

class ECGClock(object):
    def __init__(self, title=None,
                 autoscale=True,
                 min_rad=0, max_rad=2000,
                 color_cycle=['b', 'm', 'c', 'k', 'y'],  # TODO?: update for new matplotlib standard
                 parent_figure=None,
                 subplot=1):
        """Prepare a '24 hour' polar plot to add recordings to.  If no parent figure is
        specified, this will be a new standalone plot.  Otherwise, it will be a
        subplot on the parent figure.

        Keyword arguments:
        title -- title of this subplot (or whole figure, if this is the only subplot)
        autoscale -- auto-scale the r axis.  min_rad, max_rad have no effect if this is enabled.
        min_rad -- inner radius of clock, in milliseconds
        max_rad -- outer radius of clock, in milliseconds
        color_cycle -- colors to cycle through when adding recordings/ranges.
                       e.g.: [plt.cm.autumn(i) for i in np.linspace(0, 1, 7)]
        parent_figure -- the matplotlib.figure.Figure that this clock will be on
        subplot -- position of this subplot on the parent figure
        """
        # Save pointers to important things, creating a new Figure if needed to hold this plot:
        if parent_figure:
            self.parent_figure = parent_figure
        else:
            self.parent_figure = ECGFigure()
        self.fig = self.parent_figure.fig
        self.subplot = subplot

        # Add this clock to the parent Figure:
        subplot_rows, subplot_cols = self.parent_figure.nrows, self.parent_figure.ncols
        self.ax = self.fig.add_subplot( subplot_rows, subplot_cols,
                                        self.subplot, projection='polar')
        #self.ax = self.ax.flatten()  # TODO: not needed?

        # Adjust axes parameters:
        if autoscale:
            self.ax.set_autoscaley_on(True)
            # TODO: this is kind of bad.  may want to do something like ylim = 1.2*(98% value)
        else:
            self.ax.set_ylim(min_rad, max_rad)
        self.ax.set_theta_direction(-1)
        self.ax.set_theta_offset(np.pi/2.0)
        self.ax.set_xticklabels(['00:00', '03:00', '06:00', '09:00',
                                 '12:00', '15:00', '18:00', '21:00'])

        # Show time under mouse cursor (instead of angle):
        self.ax.format_coord = self.format_coord

        #self.ax.set_color_cycle(color_cycle)  # TODO?: overall vs subplot color cycle
        self.ax.set_prop_cycle( cycler('color', color_cycle) )

        if parent_figure:
            self.set_title(title)
        else:
            self.parent_figure.set_title(title)

    def set_title(self, title):
        """Set/change the title for this plot.

        Keyword arguments:
        title -- the new title (string)
        """
        if title:
            self.ax.set_title(title + '\n')
            # \n to prevent overlap with '00:00' label

    def add_recording(self, measurements, column, label=None, color=None, filtering=0):
        """Add a set of measurements to the plot.  If there are large gaps in time, data
        points in between will be interpolated.

        Keyword arguments:
        measurements -- an ECGMeasurements object
        column       -- which column of measurements contains the data to plot
        label        -- what to call this on the plot legend
        color        -- line color (or None to follow normal rotation)
        filtering    -- width of filter in minutes, or 0 to disable filtering
        """
        # TODO: HR correction (function(s))
        values = sec_to_msec(measurements.data[column].values)  # TODO: allow bypassing this
        times = measurements.data.index.to_pydatetime()
        angles = times_to_angles(times)
        if filtering:
            values = medfilt( times, values, filter_width=filtering )
        interp_angles, interp_values = polar_interp( angles, values )  # TODO: pass dTheta too
        self.ax.plot(interp_angles, interp_values, zorder=0, color=color, label=label)
        # TODO: note/handle different starting dates when multiple recordings are added.

    def add_recording_from_file(self, filename, column, label=None, color=None, filtering=0):
        """Load a set of measurements from disk and add it to the plot.

        Keyword arguments:
        filename  -- file containing the data
        column    -- which column of the file to plot
        label     -- what to call this on the plot legend
        color     -- line color (or None to follow normal rotation)
        filtering -- width of filter in minutes, or 0 to disable filtering
        """
        # TODO: HR correction (function(s))
        measurements = ECGMeasurements(filename=filename)
        self.add_recording(measurements, column, label=label, color=color, filtering=filtering)

    def add_percentile_range(self, cohort, field, lower=25, upper=75,
                             label=None, color=None, alpha=0.4,
                             smoothing=20, clip=True):
        """Load a precomputed range from a file, and add it to the plot.  zorder is
        set to -1 in this function, so foreground items should use zorder>-1.
        We assume that the axis has theta_direction=-1 and theta_offset=pi/2.

        Keyword arguments:
        cohort -- a Cohort object (i.e. a collection of ECGMeasurements)
        field  -- which column (e.g. 'QTcF_II') to extract from anns
        lower  -- lower percentile bound to show
        upper  -- upper percentile bound to show
        label  -- what to call this region on the plot legend
        color  -- color of the new region (note: you should probably specify this... see
                  http://stackoverflow.com/questions/30535442/matplotlib-fill-between-does-not-cycle-through-colours)
        alpha  -- transparency of the new region
        clip   -- clip plotted values to fit on the axis.  polar plot can get weird without this.
        smoothing -- median filter window size for smoothing lower and upper bounds
        """
        # TODO?: allow interpolation between columns, e.g. to get 2.5 percentile
        cohort.compute_pctls(measurement=field)
        times = cohort.percentiles[field].index
        lower_bounds = np.array(cohort.percentiles[field][lower].values, dtype=float)
        upper_bounds = np.array(cohort.percentiles[field][upper].values, dtype=float)
        thetas = times_to_angles( times )
        lower_bounds = sec_to_msec(lower_bounds)
        upper_bounds = sec_to_msec(upper_bounds)
        if smoothing:
            # pad the beginning and end of the data sets before filtering.
            # assumption: thetas represents <= 24 hours of values.
            half_window = 2*np.pi * (smoothing/2.0) / (24*60)
            start_overlap = np.mod(thetas[-1] + half_window, 2*np.pi)
            end_overlap   = np.mod(thetas[0]  - half_window, 2*np.pi)
            start_i = np.argmax(thetas>start_overlap)
            end_i = len(thetas) - np.argmax( np.mod(np.flip(thetas), 2*np.pi) < end_overlap )
            padded_times = np.concatenate((       times[end_i:],        times,        times[:start_i]))
            padded_lb    = np.concatenate((lower_bounds[end_i:], lower_bounds, lower_bounds[:start_i]))
            padded_ub    = np.concatenate((upper_bounds[end_i:], upper_bounds, upper_bounds[:start_i]))
            # smooth lower and upper bounds using medfilt()
            padded_lb = medfilt( padded_times, padded_lb, filter_width=smoothing )
            padded_ub = medfilt( padded_times, padded_ub, filter_width=smoothing )
            # un-pad the arrays
            lower_bounds = padded_lb[start_i:start_i+len(lower_bounds)]
            upper_bounds = padded_ub[start_i:start_i+len(upper_bounds)]
        # TODO?: may want to do that smoothing block after the next block
        # TODO: average may be nicer than median for this
        if ( np.mod(thetas[-1], 2*np.pi) != np.mod(thetas[0], 2*np.pi) ):
            # if the region doesn't end at the same angle where it started, add
            # one more point to close the area
            thetas = np.append(thetas, thetas[0])
            while (thetas[-1] < thetas[-2]):
                # ensure thetas[-1] > thetas[-2]:
                thetas[-1] += 2*np.pi
            lower_bounds = np.append(lower_bounds, lower_bounds[0])
            upper_bounds = np.append(upper_bounds, upper_bounds[0])
            # Note: this breaks when the plot is missing a large region!  TODO:
            # interpolate more data points in that case?
        if label is None: label = field
        if clip:
            ymin, ymax = self.ax.get_ylim()
            np.clip(lower_bounds, ymin, ymax, lower_bounds)
            np.clip(upper_bounds, ymin, ymax, upper_bounds)
        self.ax.fill_between(thetas, lower_bounds, upper_bounds,
                             alpha=alpha, linewidth=0, zorder=-1,
                             label=label, color=color)

    def add_annotation(self, time, r, x, y, label='', color='black'):
        """Add an annotation to a plot.  The annotation consists of a point at (time,r)
        and an arrow from (x,y) to that point.  The label appears at the tail of the arrow.

        Keyword arguments:
        time, r -- marker location
        x, y -- text location (fraction from bottom left of ENTIRE FIGURE)
        label -- text at arrow tail
        color -- line and marker color
        """
        if (x <= 0.5):
            ha = 'left'
        else:
            ha = 'right'
        if (y <= 0.5):
            va = 'bottom'
        else:
            va = 'top'
        th = time_to_angle(time)
        #print self.get_ax(subplot)  # debugging
        self.ax.plot(th, r, 'o', color=color, mew=0)
        self.ax.annotate(label,
                         xy=(th, r),
                         xytext=(x, y),
                         color=color,
                         textcoords='figure fraction',  # TODO: is subplot fraction an option?
                         arrowprops=dict(facecolor=color, ec=color, shrink=0.05,
                                         width=1, headwidth=8),
                         horizontalalignment=ha,
                         verticalalignment=va
        )

    def add_legend(self):
        """Add the legend to the top right of the figure, outside of the plot area.
        """
        self.ax.legend(loc="upper left", bbox_to_anchor=(1,1.1))
        # TODO: maybe pass other args through to ax.legend()
        # TODO: overall vs subplot legends?

    def show(self):
        """Show the figure on screen, i.e. with all subplots including this one.
        """
        self.parent_figure.show()
        # TODO: only show individual subplot here... update description then.

    def save(self, filename):
        """Save the figure to disk, i.e. with all subplots including this one.  If the
        plot has been modified (zoomed, resized, etc.) via show(), these changes
        will be included.

        Keyword arguments:
        filename -- file to save to, e.g. 'qt_clock.png'
        """
        self.fig.savefig(filename, bbox_inches='tight')
        # TODO: default to title as filename if none specified?
        # TODO: only save individual subplot here... update description then.

    def format_coord(self, th, r):
        """Return a human readable string from a (theta, r) coordinate."""
        # TODO: could take label+units as args, then children just pass theirs up
        return 'time=' + angle_to_time(th) + ', val=%1.0f'%(r)  # TODO: units on val?

# TODO: kwargs in several places?

#################################### TODO: #####################################

# - fix spacing between figures, titles, etc. when using subplots
# - start/end arrows (or other markers)?  could get messy... maybe just an
#   option to list the start/end times
# - specify starting offset of a plot, e.g. where '00:00' in csv really means
#   some other time?

################################################################################
