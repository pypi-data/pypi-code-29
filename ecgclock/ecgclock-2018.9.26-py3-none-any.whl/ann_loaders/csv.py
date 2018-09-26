
# TODO: completely remove this file / function

################################### Imports: ###################################

import csv
import os

################################## Functions: ##################################

def load_from_csv(csv_filename, cols_wanted=[0,1], col_fmt=[str,float]):
    """Read a CSV file and return the specified columns as separate lists, converted
    to the specified data types.  Using the default values of cols_wanted and
    col_fmt, for example, we could load a CSV where each line was in the format
    "11:06:30,452".  If we can't parse the first row of the csv file, we will
    assume it was a header row and skip it.

    Keyword arguments:
    csv_filename -- the file to read from
    cols_wanted -- which columns to read.  return values will follow this order.
    col_fmt -- respective data types for columns listed in cols_wanted.
    """
    if ( len(cols_wanted) != len(col_fmt) ):
        raise IndexError('load_from_csv(): cols_wanted and col_fmt must be same length.')

    results = [ [] for i in range(len( cols_wanted )) ]
    if os.name == 'nt':
        fmode = 'rt'  # because 'U' isn't an option.  good luck.
    else:
        fmode = 'rtU'  # because 'U' isn't default in Python 2.
    with open(csv_filename, fmode) as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            new_results = ['' for _ in range(len( cols_wanted ))]
            try:
                for j, col in enumerate(cols_wanted):
                    new_results[j] = col_fmt[j]( row[col] )
                    # TODO: handle NaN/blank values somehow... probably not in here, though.
            except ValueError:
                if (i == 0):
                    continue  # assume we just choked on header row
                else:
                    raise
            for j, res in enumerate(new_results):
                results[j].append( res )
    return tuple(results)

################################################################################

# TODO?: could try to handle string entries like '0.5s' or '450ms' etc.  instead
# of requiring float.
