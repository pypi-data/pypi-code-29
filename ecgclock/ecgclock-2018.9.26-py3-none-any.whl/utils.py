
################################### Imports: ###################################

import numpy as np
import datetime
import multiprocessing as mp
import datetime as dt
import pandas as pd
import math
import ecgclock

################################## Functions: ##################################

def angle_to_time(th):
    """Convert an angle like pi/2 into a string like '06:00'.

    Keyword arguments:
    th -- angle in radians, starting from 0 at 00:00 and increasing to 2pi at 24:00
    """
    th = np.mod(th, 2*np.pi)
    minute = 1.0*th/(2*np.pi) * 24  # well, hour not minute
    hour   = int(np.floor(minute))
    minute = int(round( (minute - hour) * 60 ))
    return str(hour).zfill(2) + ":" + str(minute).zfill(2)
    # TODO: maybe use this function to generate x tick labels?

def time_to_angle(timestr):
    """Convert a string like '06:00' into an angle like pi/2.

    Keyword arguments:
    timestr -- time (string, 24-hour, hh:mm)
    """
    h,m = timestr.split(':')
    min_of_day = 60*int(h) + int(m)
    return 2*np.pi*(min_of_day/1440.0)

def times_to_angles(times):
    """Convert a list of times into angles in radians.  Midnight is 0 (or 2pi), 6AM
    is pi/2, noon is pi, 6PM is 3pi/2.  These values can be mapped to the proper
    clock positions (i.e. midnight at 'top' of clock) using theta_direction=-1
    and theta_offset=pi/2 on your axes.  If the date is available, it will be
    used to 'wrap around' the clock, e.g. angles for times tomorrow will be 2pi
    higher than those for today.  Otherwise, at each midnight crossing, the
    angle will reset to 0.

    Keyword arguments:
    times -- list of datetimes (or times)
    """
    # angles will be indexed relative to midnight before the data started:
    first_time = times[0].replace(hour=0, minute=0, second=0, microsecond=0)
    angles = np.zeros_like(times, dtype=float)
    for i,t in enumerate(times):  # TODO: vectorize/parallelize this loop
        h = t.hour; m = t.minute; s = t.second; us = t.microsecond
        t_as_hr = h + ( (((s + (us/1e6))/60.0) + m) / 60.0 )  # time as hour of day
        angle = (t_as_hr/24.0) * 2*np.pi  # time in radians
        if type(t) == datetime.datetime:
            angle += 2*np.pi * (t - first_time).days  # offset by 2pi per day elapsed
            # TODO: wrap around even when we don't have dates
        angles[i] = angle
    return angles

def polar_interp( thetas, rs, min_dTheta=(2*np.pi/1440) ):
    """Add more points to theta and r vectors to fill in large gaps in theta.  This
    is needed because matplotlib draws straight lines between data points, even
    on polar axes.

    Keyword arguments:
    thetas -- list of theta values, same length as rs.  values must be consecutive and increasing.
    rs -- list of radial values, same length as thetas
    min_dTheta -- minimum output resolution, default value is 1 point per minute (1440 mins/360 degrees)
    """
    th_new = [ thetas[0] ]
    r_new = [ rs[0] ]
    for i in range(1,len(thetas)):
        dTheta = thetas[i] - thetas[i-1]
        if ( dTheta > min_dTheta ):
            # poor resolution here, add more points (TODO: simplify this part (vectorize/parallelize whole thing?))
            points_to_add = int(np.ceil(1.0*dTheta/min_dTheta - 1))
            new_dth = 1.0 * dTheta / (points_to_add+1)
            th_to_add = [ thetas[i-1] + pt*new_dth for pt in range(1, points_to_add+1) ]
            r_to_add = np.interp(th_to_add,
                                 [ thetas[i-1], thetas[i] ],
                                 [ rs[i-1], rs[i] ] )
            th_new.extend(th_to_add)
            r_new.extend(r_to_add)
        # Always keep the existing point:
        th_new.append(thetas[i])
        r_new.append(rs[i])
    return np.array(th_new), np.array(r_new)
    # TODO: use this function for loaded ranges too, not just single-patient data

def general_filter( times, values, filter_width=5, filt_type=np.nanmedian, centered=True ):
    """Filters the values list with a width of filter_width minutes.  Returns
    the filtered values list.  Note that the results at the beginning and end of
    the list will be skewed; we don't pad values 'outside' of the list.

    Keyword arguments:
    times -- list of datetimes
    values -- list of values corresponding to times
    filter_width -- in minutes
    filt_type -- the function to apply to each window, e.g. max or np.average
    centered -- filter window is centered on each value (default).  else, use only previous values.
    """
    assert (len(times) == len(values))
    angles = times_to_angles(times)  # because this handles time wraparound for
                                     # us, and allows us to compare floats
                                     # rather than time strings/objects
    # TODO: don't duplicate work; allow passing in angles if we already have them.
    filter_width_radians = 1.0 * filter_width / (24*60) * 2*np.pi
    values_filtered = np.array(values)
    values = np.array(values)  # for small speedup
    angles = np.array(angles)  # for big speedup

    # Single-threaded:
    for i in range( len(values) ):
        if centered:
            x = np.searchsorted(angles, angles[i] - filter_width_radians/2.0              )  # start index
            y = np.searchsorted(angles, angles[i] + filter_width_radians/2.0, side='right')  # end index
        else:
            x = np.searchsorted(angles, angles[i] - filter_width_radians)
            y = i+1  # '+1' to include current value.  may switch to just 'i' to use only past values.
        values_filtered[i] = filt_type( values[x:y] )  # TODO?: optimize this if filter gets wide
        # TODO?: smarter/faster search, e.g. by remembering where we left off
        # last time or by parallelizing that for loop

    # Multi-"threaded":
    # pool = mp.Pool(processes=mp.cpu_count())
    # fargs = [(angles, values, filter_width_radians, i)
    #          for i in range(len(angles))]  # TODO: avoid duplication
    # values_filtered = pool.map(par_med_filt, fargs)  # TODO
    # pool.close()
    # pool.join()
    # Doesn't save much time, probably because of duplication.

    return values_filtered

def medfilt( times, values, filter_width=5, centered=True ):
    """Median-filters the values list with a width of filter_width minutes.  Returns
    the filtered values list.  Note that the results at the beginning and end of
    the list will be skewed; we don't pad values 'outside' of the list.

    Keyword arguments:
    times -- list of time strings
    values -- list of values corresponding to times
    filter_width -- in minutes
    centered -- filter window is centered on each value (default).  else, use only previous values.
    """
    values = np.array(values, dtype=float)
    return general_filter( times, values, filter_width=filter_width,
                           filt_type=np.nanmedian, centered=centered )

# def par_med_filt(packed_args):
#     """Computes the output of a median filter at position i in values, where the
#     window boundaries are determined by angles and filter_width_radians.  This
#     is intended to be used as a helper for medfilt().

#     Keyword arguments:
#     packed_args -- (list of angles, list of values, filter_width_radians, position)
#     """
#     angles, values, filter_width_radians, i = packed_args
#     assert (len(angles) == len(values))
#     x = np.searchsorted(angles, angles[i] - filter_width_radians/2.0              )  # start index
#     y = np.searchsorted(angles, angles[i] + filter_width_radians/2.0, side='right')  # end index
#     return np.median( values[x:y] )

def sec_to_msec(values, cutoff=10):
    """Take a list of values and return either: (a) the same list or (b) the list
    multiplied by 1000.  If the values in the list are 'too low', we assume we
    must do (b).  This is useful when we read a bunch of times that were
    supposed to be in milliseconds, but they might have been in seconds by accident.

    Keyword arguments:
    values -- list of values to be converted
    cutoff -- if most values are above this number, we won't convert the list
    """
    values = np.array(values, dtype=float)
    if np.nanmedian(values) < cutoff:
        values *= 1000.0
    return values

def msec_to_sec(values, cutoff=10):
    """Take a list of values and return either: (a) the same list or (b) the list
    divided by 1000.  If the values in the list are 'too high', we assume we
    must do (b).  This is useful when we read a bunch of times that were
    supposed to be in seconds, but they might have been in msec by accident.

    Keyword arguments:
    values -- list of values to be converted
    cutoff -- if most values are below this number, we won't convert the list
    """
    # TODO: may be able to remove this after make_normal_range is updated
    values = np.array(values, dtype=float)
    if np.nanmedian(values) > cutoff:
        values /= 1000.0
    return values

def derivative( times, values, percent=False ):
    """Compute the point-by point derivative of values with respect to time (in
    seconds).  e.g. if you pass in a list of QT values, a list containing the
    slope (QT/second) will be returned.

    Keyword arguments:
    times -- list of datetimes
    values -- list of values corresponding to times
    percent -- return the percent change rather than the absolute change
    """
    assert (len(times) == len(values))
    deriv = values[:]
    for i in range( len(values) ):
        # TODO: vectorize the bulk of this, then fix end cases
        if (i==0):
            numer = values[i+1] - values[i]
            denom =  times[i+1] -  times[i]
        elif (i == len(values)-1):
            numer = values[i]   - values[i-1]
            denom =  times[i]   -  times[i-1]
        else:
            numer = values[i+1] - values[i-1]
            denom =  times[i+1] -  times[i-1]
        denom = denom.total_seconds()
        if (percent):
            numer = 100.0 * numer / values[i]
        deriv[i] = 1.0 * numer / denom
    return deriv
    # TODO: take data point spacing into account?

def compute_pctls(measurement, anns=[], files=[], weights='beat'):
    """Compute percentile ranges for a given measurement, at a resolution of 1
    minute.  Note: weighting by subject or recording can inadvertently give lots
    of weight to noise, particularly in small cohorts.  If anns and files are
    both specified, we will assume that both sets should be used.  Note that a
    scratch column 'min_of_day' will be created in all anns.  Returns a pandas
    DataFrame of measurement values with one column per percentile and a time index.

    Keyword arguments:
    measurement -- which measurement to analyze, e.g. 'QTcF_II'
    anns        -- list of Recordings containing the needed column
    files       -- list of files (e.g. CSVs) containing the needed column
    weights     -- give equal weight to each 'beat', 'recording', or 'subject'
    """
    # TODO: accept a Cohort or a list of filenames, not just list of Recordings
    # TODO: some kind of upsampling or downsampling of anns in order to
    # weight by subject
    # TODO?: support arbitrary resolution
    bins = {}
    for minute in range(1440):
        bins[minute] = []
    if not anns and not files:
        raise ValueError("must specify either anns or files.")
    if weights == 'beat':
        for ann in anns:
            if ann.keep_data_loaded:
                update_minute_bins(ann,measurement,bins)
            else:
                ann_copy = ecgclock.Recording(filename=ann.filename, subjid=ann.subjid)
                update_minute_bins(ann_copy,measurement,bins)
        for filename in files:
            ann = ecgclock.Recording(filename=filename)
            update_minute_bins(ann,measurement,bins)
            # TODO: make sure ann is free()d here
    elif weights == 'recording':
        # this shouldn't be too bad... compute percentiles on each recording
        # individually, then average them together.
        raise NotImplementedError()
    elif weights == 'subject':
        raise NotImplementedError()
    else:
        raise ValueError("'weights' must be 'beat', 'recording', or 'subject'.")
    timeindex = [dt.time(hour=h,minute=m,second=30) for h in range(24) for m in range(60)]
    results = pd.DataFrame(data=None, index=timeindex, columns=range(101))
    results.index.name = 'time'
    for b in bins:
        data_with_nans = np.array(bins[b], dtype=float)
        cleaned_data = data_with_nans[~np.isnan(data_with_nans)]
        if len(cleaned_data) == 0:
            this_time_pctls = [None for _ in range(101)]
        else:
            this_time_pctls = np.percentile(cleaned_data, range(101))
        results.loc[timeindex[b]] = this_time_pctls
    return results

def update_minute_bins(ann,measurement,bins):
    """Add measurements from ann to bins."""
    ann.data['min_of_day'] = ann.data.index.minute + 60*ann.data.index.hour
    for minute in range(1440):
        relevant_rows = ann.data[ann.data['min_of_day'] == minute]
        bins[minute] += relevant_rows[measurement].values.tolist()

################################################################################
