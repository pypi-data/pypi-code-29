
################################### Imports: ###################################

import numpy as np
import csv
from dateutil import parser  # arbitrary datetime strings -> datetime object
import datetime
import multiprocessing as mp
import math

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

def times_to_angles(times, parallel=True):
    """Convert a list of times (where each time is a string like
    '1998-04-02T09:26:03.620') into angles in radians.  Midnight is 0 (or 2pi),
    6AM is pi/2, noon is pi, 6PM is 3pi/2.  These values can be mapped to the
    proper clock positions (i.e. midnight at 'top' of clock) using
    theta_direction=-1 and theta_offset=pi/2 on your axes.  If the date is
    available in the time strings, it will be used to 'wrap around' the clock,
    e.g. angles for times tomorrow will be 2pi higher than those for today.  If
    dates are unknown/unlisted, we will always assume that times wrapping
    through midnight proceed to the next consecutive day - e.g. if a data point
    at '23:59' is followed by one at '00:01', we assume 2 minutes elapsed even
    though it could really be 2 minutes plus 24*k hours.

    Keyword arguments:
    times -- times, as a list of strings.  e.g.: ['11:06:15', '11:06:20']
    parallel -- should we parallelize the conversion process?
    """
    # angles will be indexed from the midnight before the data started:
    first_time = parser.parse(times[0]).replace(hour=0, minute=0, second=0, microsecond=0)

    running_offset = 0  # for wrapping around when we don't know dates

    #times = np.array(times)

    # parser.parse() is quite slow, so we usually want to parallelize this part:
    if parallel:
        pool = mp.Pool(processes=mp.cpu_count())
        times = pool.map(parser.parse, times)
        pool.close()
        pool.join()
    else:
        times = [parser.parse(t) for t in times]
    # (Parsing could be done much faster if we could assume a standard input
    # format, but we want to accept fairly arbitrary date/time strings.)

    angles = []
    for t in times:
        h = t.hour; m = t.minute; s = t.second; us = t.microsecond
        # year = t.year; month = t.month; day = t.day
        t_as_hr = h + ( (((s + (us/1e6))/60.0) + m) / 60.0 )  # time as hour of day
        angle = (t_as_hr/24.0) * 2*np.pi  # time in radians

        # If we know dates:
        angle += 2*np.pi * (t - first_time).days  # offset by 2pi per day elapsed

        # If we don't know dates:
        angle += running_offset
        if ( (angles) and (angle < angles[-1]) ):
            running_offset += 2*np.pi
            angle += 2*np.pi

        angles.append(angle)
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
            # poor resolution here, add more points (TODO: simplify this part)
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

    return th_new, r_new
    # TODO: use this function for loaded ranges too, not just single-patient data

def general_filter( times, values, filter_width=5, filt_type=np.median ):
    """Filters the values list with a width of filter_width minutes.  Returns
    the filtered values list.  Note that the results at the beginning and end of
    the list will be skewed; we don't pad values 'outside' of the list.

    Keyword arguments:
    times -- list of time strings
    values -- list of values corresponding to times
    filter_width -- in minutes
    filt_type -- the function to apply to each window, e.g. max or np.average.
    """
    assert (len(times) == len(values))
    angles = times_to_angles(times)  # because this handles time wraparound for
                                     # us, and allows us to compare floats
                                     # rather than time strings/objects
    # TODO: don't duplicate work; allow passing in angles if we already have them.
    filter_width_radians = 1.0 * filter_width / (24*60) * 2*np.pi
    values_filtered = values[:]
    values = np.array(values)  # for small speedup
    angles = np.array(angles)  # for big speedup

    # Single-threaded:
    for i in range( len(values) ):
        x = np.searchsorted(angles, angles[i] - filter_width_radians/2.0              )  # start index
        y = np.searchsorted(angles, angles[i] + filter_width_radians/2.0, side='right')  # end index
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

def medfilt( times, values, filter_width=5 ):
    """Median-filters the values list with a width of filter_width minutes.  Returns
    the filtered values list.  Note that the results at the beginning and end of
    the list will be skewed; we don't pad values 'outside' of the list.

    Keyword arguments:
    times -- list of time strings
    values -- list of values corresponding to times
    filter_width -- in minutes
    """
    return general_filter( times, values, filter_width=filter_width, filt_type=np.median )

def par_med_filt(packed_args):
    """Computes the output of a median filter at position i in values, where the
    window boundaries are determined by angles and filter_width_radians.  This
    is intended to be used as a helper for medfilt().

    Keyword arguments:
    packed_args -- (list of angles, list of values, filter_width_radians, position)
    """
    angles, values, filter_width_radians, i = packed_args
    assert (len(angles) == len(values))
    x = np.searchsorted(angles, angles[i] - filter_width_radians/2.0              )  # start index
    y = np.searchsorted(angles, angles[i] + filter_width_radians/2.0, side='right')  # end index
    return np.median( values[x:y] )

def decimate( times, values, q=5, aggregator=np.average, parallel=True):
    """Downsamples a set of times and values.  The final chunk will be discarded if
    it doesn't contain q samples.  The aggregator function is applied
    independently to the times and the values.  Example:
    decimate( ['1:35','1:36','1:37','1:38'], [4,3,2,1], q=2, aggregator=max)
    returns
    ( ['1:36','1:38'], [4, 2] ).
    Note that the behavior of this function may not be what you intended if the
    spacing of the data points is irregular.

    Keyword arguments:
    times -- list of time strings
    values -- list of values corresponding to times
    q -- downsampling factor
    aggregator -- method used to aggregate each group of samples
    parallel -- parse input times in parallel
    """
    # TODO: allow time-based window rather than point-based.
    # TODO?: just act on one vector of values, let person run it again to do
    # times?  need to know if we have to do time conversions though.  can we
    # average, etc. normal datetime objects?  or what about user selecting 2
    # different aggregators?
    assert (len(times) == len(values))

    times_downsampled = [None]*(len(times)//q)
    values_downsampled = [None]*(len(values)//q)

    if parallel:
        pool = mp.Pool(processes=mp.cpu_count())
        times = pool.map(parser.parse, times)
        pool.close()
        pool.join()
    else:
        times = [parser.parse(t) for t in times]

    # WIP:
    times = [t.timestamp() for t in times]  # datetime objects -> unix time (float)
    for i in range( len(values)//q ):
        values_downsampled[i] = aggregator( values[i*q:(i+1)*q] )
        times_downsampled[i] = aggregator( times[i*q:(i+1)*q] )
    times_downsampled = [datetime.datetime.fromtimestamp(t).isoformat() for t in times_downsampled]  # unix time -> time string
    # Note: python3 required...

    return times_downsampled, values_downsampled

def sec_to_msec(values, cutoff=10):
    """Take a list of values and return either: (a) the same list or (b) the list
    multiplied by 1000.  If the values in the list are 'too low', we assume we
    must do (b).  This is useful when we read a bunch of times that were
    supposed to be in milliseconds, but they might have been in seconds by accident.

    Keyword arguments:
    values -- list of values to be converted
    cutoff -- if most values are above this number, we won't convert the list
    """
    if (np.median(values) < cutoff):
        values = [val * 1000.0 for val in values]
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
    if (np.median(values) > cutoff):
        values = [val / 1000.0 for val in values]
        # values = np.array(values)
        # values = values / 1000.0
        # values = values.tolist()
    return values

def derivative( times, values, parallel=True, percent=False ):
    """Compute the point-by point derivative of values with respect to time (in
    seconds).  e.g. if you pass in a list of QT values, a list containing the
    slope (QT/second) will be returned.

    Keyword arguments:
    times -- list of time strings
    values -- list of values corresponding to times
    parallel -- parallelize (parts of) this function?
    percent -- return the percent change rather than the absolute change
    """
    assert (len(times) == len(values))

    deriv = values[:]

    if parallel:
        pool = mp.Pool(processes=mp.cpu_count())
        times = pool.map(parser.parse, times)
        pool.close()
        pool.join()
    else:
        times = [parser.parse(t) for t in times]

    for i in range( len(values) ):
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
    # TODO: parallelize that loop

    return deriv
    # TODO: take data point spacing into account?

################################## CSV utils: ##################################

def make_normal_range( csv_list, output_filename, val_col=1, has_headers=False,
                       hr_correction=0, rr_col=None, time_col=0 ):
    """Take a list of CSV files, and compute percentiles (every minute) for their
    values.  Values may be QTc, TpTe, etc.  Time is assumed to be in column 0 if
    not specified.  The output will have a header row.

    Keyword arguments:
    csv_list -- list of csv files, like ['E:\4101082813\pat41QT.csv', 'E:\1102061313\pat06QT.csv']
    output_filename -- where to save the result, e.g. 'QTcF_Cohort1_baseline.csv'
    val_col -- which column contains the values.
    hr_correction -- exponent to correct values for RR.  e.g. 2=Bazett.  0 to disable.
    rr_col -- column in CSVs containing RR values, if heart rate correction is enabled
    time_col -- column in CSVs containing times
    """
    # Put values from all CSVs into bins:
    bins = [[] for _ in range(60*24)]  # one bin per minute
    for csv_filename in csv_list:
        with open(csv_filename, 'rt') as csvfile:
            csv_reader = csv.reader(csvfile)
            for i, row in enumerate(csv_reader):
                if i==0 and has_headers: continue
                # add value from this row to appropriate bin
                t = parser.parse( row[time_col] )
                m = t.hour*60 + t.minute
                if row[val_col]==None or row[val_col]=='': continue
                if hr_correction and (row[rr_col]==None or row[rr_col]=='' or float(row[rr_col]) == 0): continue
                if hr_correction:
                    bins[m].append( float(row[val_col]) /
                                    math.pow(msec_to_sec([float(row[rr_col])])[0], 1.0/hr_correction) )
                else:
                    bins[m].append( row[val_col] )
    # Compute percentiles within each bin (minute):
    results = compute_range_percentiles(bins)
    # Write output:
    write_normal_range_csv(output_filename, results)
    # TODO: support different val_col for each CSV.  i.e. give it as a list.

def compute_range_percentiles(bins):
    # Compute percentiles within each bin (minute):
    results = []
    for bin in bins:
        try:
            bin_flt = [float(x) for x in bin]
            results.append( np.percentile(bin_flt, range(101)).tolist() )
        except IndexError:
            results.append( None )  # probably had no data for this minute.
    return results

def write_normal_range_csv(output_filename, results):
    # Write results to CSV.  Assuming we were computing QTc percentiles, the
    # output will look like:
    # First row:      time,    0%,    1%,    2%, ...
    # Second row: 00:00:30, <QTc>, <QTc>, <QTc>, ...
    # Third row:  00:01:30, <QTc>, <QTc>, <QTc>, ...
    headers = [str(i) + '%' for i in range(101)]
    headers = ['time'] + headers
    with open(output_filename, 'w') as csv_out_file:
        csv_writer = csv.writer(csv_out_file)
        csv_writer.writerow(headers)
        for t, row in enumerate(results):
            if (row==None):
                continue  # don't write the rows that had no data
            h = int(t / 60)
            m =     t % 60
            t_str = str(h).zfill(2) + ':' + str(m).zfill(2) + ':30'
            # :30 because e.g. minute 0 covers 00:00:00-00:01:00, and we store the midpoint 00:00:30
            csv_writer.writerow( [t_str] + row )

################################################################################
