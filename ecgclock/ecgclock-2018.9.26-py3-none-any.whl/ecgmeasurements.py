
################################### Imports: ###################################

import os
import pandas
import numpy as np
import datetime as dt
from .ann_loaders.compas import correct_compas_loader
from .utils import msec_to_sec, medfilt

#################################### Class: ####################################

class ECGMeasurements:
    # TODO?: maybe rename to something simpler like Recording?
    # TODO?: subclass DataFrame

    def __init__(self, **kwargs):
        """Create an ECGMeasurements object.  data will be accessible via the 'data'
        attribute, which is a pandas DataFrame.

        Keyword arguments:
        data     -- a pandas DataFrame with a datetime index and column(s) of EGG measurements
        filename -- a file to load data from
        subjid   -- subject ID number

        Example usage:
            >>> anns = ECGMeasurements(filename='example.csv')
            >>> anns.data
                                           qt        rr
            time
            2012-02-15 06:55:03.106  0.421341  1.582359
            2012-02-15 06:55:04.061  0.421714  1.536198
            2012-02-15 06:55:04.972  0.421714  1.118468
            ...
            >>> anns.data['qtcf'] = anns.data['qt']/np.power(anns.data['rr'],1/3)
            >>> anns.data
                                           qt        rr      qtcf
            time
            2002-02-15 06:55:03.106  0.421341  1.582359  0.361575
            2002-02-15 06:55:04.061  0.421714  1.536198  0.365485
            2002-02-15 06:55:04.972  0.421714  1.118468  0.406266
            ...
            >>> clk = QTClock()
            >>> clk.add_recording(anns, 'qtcf')
            >>> clk.show()
        """
        # TODO?: something better than (or in addition to) subjid to specify how
        # this object should be grouped with others
        filename      = kwargs.pop('filename', None)
        data          = kwargs.pop('data',     None)
        self.subjid   = kwargs.pop('subjid',   None)
        if data != None and filename != None:
            raise ValueError("Either 'data' or 'filename' must be None.")
        if data != None and type(data) != pandas.DataFrame:
            raise TypeError("'data' must be a pandas DataFrame.")
        if data != None:
            self.data = data
        elif filename != None:
            self.data = self.load_file(filename, **kwargs)
        else:
            self.data = None

    def load_file(self, filename, **kwargs):
        """Load a set of ECG measurements from a file.  The file may be a CSV or COMPAS
        output.  Returns a pandas DataFrame.
        """
        file_ext = os.path.splitext(filename)[-1]
        if file_ext == '.csv':
            return self.load_csvfile(filename, **kwargs)
        elif file_ext == '.twb' or file_ext == '.txt':
            return self.load_compasfile(filename, **kwargs)
        raise ValueError("Don't know how to load %s." % filename)
        # TODO?: name index column 'time'
        # TODO?: make sure all (non-index) columns are floats

    def append_file(self, filename, **kwargs):
        """Append another set of measurements to this one."""
        raise NotImplementedError()
        # TODO.  this may get messy because column names will have to match.
        # also may end up prepending or merging to keep time column sorted.

    def load_csvfile(self, filename, **kwargs):
        """Load values from a CSV file.  The time column (time_col) can be specified
        with either an integer index or a string matching the column header.
        Returns a pandas DataFrame.

        Keyword arguments:
        filename    -- a CSV file that may or may not contain headers
        time_col    -- which column contains time values (default: 'time' or 0)
        has_headers -- whether the CSV file has a header row (default: True)
        headers     -- list of column names (e.g. if the file has no header row) (default: None)
        delimiter   -- column separator (default: ',')
        quotechar   -- quote character (default: '"')
        """
        # TODO: move this function to ann_loaders
        time_col    = kwargs.get('time_col',    None)
        has_headers = kwargs.get('has_headers', True)
        headers     = kwargs.get('headers',     None)
        delimiter   = kwargs.get('delimiter',   ',')
        quotechar   = kwargs.get('quotechar',   '"')
        # TODO: make sure all combos of kwargs work as expected for files both
        # with and without headers
        if time_col == None:
            if has_headers:
                time_col = 'time'
            else:
                time_col = 0
        file_contents = pandas.read_csv(
            filename,
            index_col             = time_col,
            header                = 0 if has_headers else None,
            names                 = headers,
            parse_dates           = True,
            infer_datetime_format = True,
            delimiter             = delimiter,
            quotechar             = quotechar,
            # TODO?:
            # usecols               = ...,
            # dtype                 = ...,
            # converters            = ...,
            # (should probably use **kwargs.  be sure to pop extras off above.)
        )
        # TODO: ensure the messy date parser in pandas is parallelized like mine was
        return file_contents

    def load_compasfile(self, filename, **kwargs):
        """Load values from a COMPAS file (TXT or TWB).  Returns a pandas DataFrame.

        Keyword arguments:
        filename -- a COMPAS annotation file
        """
        # TODO: move this function to ann_loaders
        vals, headers = correct_compas_loader(filename)
        index = [dt.datetime.combine(row[0],row[1]) for row in vals]
        vals = np.array(vals)[:,2:]
        headers = headers[2:]
        file_contents = pandas.DataFrame(
            data    = vals,
            index   = index,
            columns = headers,
            # copy=False
        )
        return file_contents

    def write_to_csv(self, filename):
        """Write data to CSV file.  Note that this function can be used to convert
        other file formats to CSV.  e.g.:
            >>> anns = ECGMeasurements(filename='example.twb')
            >>> anns.write_to_csv('example.csv')
        """
        # TODO?: support selecting subset of columns
        self.data.to_csv(filename)

    def compute_hr_corrected_col(self, in_col, rr_col, out_col=None, method='Fridericia', rr_avg_secs=0):
        """Compute a new column using existing measurement and RR columns.  RR may
        optionally be averaged with a running median filter.

        Keyword arguments:
        in_col  -- name of input column (e.g. 'QTp')
        rr_col  -- name of RR column
        out_col -- name of output column (default: in_col+'cF' or 'cB')
        method  -- 'Fridericia' (default) or 'Bazett'
        rr_avg_secs -- number of seconds to compute running RR average (0 = disable, default)
        """
        # TODO?: Framingham, etc.
        # TODO?: probably move this function to utils (and have time,'qt',rr
        # arrays as input), but still allow calling from here
        # TODO?: overwrite=False arg
        methods = {
            'Fridericia': {'exp': 3.0, 'suffix': 'cF'},
            'Bazett':     {'exp': 2.0, 'suffix': 'cB'}
        }
        if out_col is None:
            out_col = in_col+methods[method]['suffix']
        exp = methods[method]['exp']
        vals = self.data[in_col].values.astype(float)
        rr   = self.data[rr_col].values.astype(float)
        if rr_avg_secs > 0:
            times = self.data.index.to_pydatetime()
            rr = medfilt(times, rr, filter_width=rr_avg_secs/60.0, centered=False)
        rr_sec = msec_to_sec(rr)
        corrected_vals = vals / np.power(rr_sec, 1/exp)
        self.data[out_col] = corrected_vals

    def compute_qtc(self, qt_col, rr_col, qtc_col=None, method='Fridericia', rr_avg_secs=0):
        """Compute a QTc column using existing QT and RR columns.  RR may optionally be
        averaged with a running median filter.

        Keyword arguments:
        qt_col  -- name of QT column
        rr_col  -- name of RR column
        qtc_col -- name of output column (default: 'QTcB' or 'QTcF')
        method  -- 'Fridericia' (default) or 'Bazett'
        rr_avg_secs -- number of seconds to compute running RR average (0 = disable, default)
        """
        self.compute_hr_corrected_col(qt_col, rr_col, qtc_col, method, rr_avg_secs)

################################################################################
