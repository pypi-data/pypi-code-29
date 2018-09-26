
################################### Imports: ###################################

import os
import pandas as pd
import numpy as np
import datetime as dt
from .ann_loaders.compas import correct_compas_loader
from .utils import msec_to_sec, medfilt

#################################### Class: ####################################

class Recording:
    # TODO?: subclass DataFrame

    def __init__(self, **kwargs):
        """Create a Recording.  Note that 'recording' isn't exactly the best name for
        this; really it's the annotations/measurements *from* an ECG recording.
        The measurements will be accessible via the 'data' attribute, which is a
        pandas DataFrame.  If load_data is False, the data will be loaded from
        disk each time it's accessed (rather than loading it once and keeping it
        in memory).

        Keyword arguments:
        filename  -- a file to load data from
        data      -- a pandas DataFrame with a datetime index, and column(s) of EGG
                     measurements.  This may be used if you have already loaded a set
                     of annotations and want to create a Recording from those,
                     rather than from a file.
        subjid    -- subject ID number, for accounting use
        load_data -- load data from disk immediately (and keep it in RAM)
                     (default: True).  setting to False is useful when you want
                     to load a bunch of Recordings into a Cohort without
                     actually loading all of the data into memory.

        Example usage:
            >>> anns = Recording(filename='example.csv')
            >>> anns.data
                                           qt        rr
            time
            2012-02-15 06:55:03.106  0.421341  1.582359
            2012-02-15 06:55:04.061  0.421714  1.536198
            2012-02-15 06:55:04.972  0.421714  1.118468
            ...
            >>> anns.compute_qtc('qt', 'rr', qtc_col='qtcf')
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
        # TODO: how to save custom columns if load_data was False (or notify the
        # user when they create a column that won't be saved)?
        self.filename         = kwargs.pop('filename',  None)
        data                  = kwargs.pop('data',      None)
        self.subjid           = kwargs.pop('subjid',    None)
        self.keep_data_loaded = kwargs.pop('load_data', True)
        if data != None and self.filename != None:
            raise ValueError("Either 'data' or 'filename' must be None.")
        if data != None and type(data) != pd.DataFrame:
            raise TypeError("'data' must be a pandas DataFrame.")
        if data != None:
            self.data = data
        elif self.keep_data_loaded and self.filename != None:
            self.data = self.load_data(**kwargs)
        else:
            self.data = None

    def get_data(self):
        """Returns the pandas DataFrame for this file.  Will generate it from the file
        if it's not already loaded.
        """
        if self._data is None:
            return self.load_data()
        else:
            return self._data

    def set_data(self, data):
        self._data = data

    def del_data(self):
        self._data = None

    data = property(get_data, set_data, del_data,
                    "pandas DataFrame of annotations from this file")

    def load_data(self, **kwargs):
        """Load a set of ECG measurements from a file.  The file may be a CSV or COMPAS
        output.  Returns a pandas DataFrame.
        """
        filename = self.filename
        file_ext = os.path.splitext(filename)[-1]
        if file_ext == '.csv':
            return self.load_csvfile(**kwargs)
        elif file_ext == '.twb' or file_ext == '.txt':
            return self.load_compasfile(**kwargs)
        raise ValueError("Don't know how to load %s." % filename)
        # TODO?: name index column 'time'
        # TODO?: make sure all (non-index) columns are floats

    def load_csvfile(self, **kwargs):
        """Load values from a CSV file.  The time column (time_col) can be specified
        with either an integer index or a string matching the column header.
        Returns a pandas DataFrame.

        Keyword arguments:
        time_col    -- which column contains time values (default: 'time' or 0)
        has_headers -- whether the CSV file has a header row (default: True)
        headers     -- list of column names (e.g. if the file has no header row) (default: None)
        delimiter   -- column separator (default: ',')
        quotechar   -- quote character (default: '"')
        """
        # TODO: move this function to ann_loaders
        filename = self.filename
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
        file_contents = pd.read_csv(
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

    def load_compasfile(self, **kwargs):
        """Load values from a COMPAS file (TXT or TWB).  Returns a pandas DataFrame.
        """
        # TODO: move this function to ann_loaders
        filename = self.filename
        vals, headers = correct_compas_loader(filename)
        index = [dt.datetime.combine(row[0],row[1]) for row in vals]
        vals = np.array(vals)[:,2:]
        headers = headers[2:]
        file_contents = pd.DataFrame(
            data    = vals,
            index   = index,
            columns = headers,
            # copy=False
        )
        file_contents.index.name = 'time'  # because this header may be blank in the source
        return file_contents

    def write_to_csv(self, filename, columns=None):
        """Write data to CSV file.  Note that this function can be used to convert
        other file formats to CSV.  e.g.:
            >>> anns = Recording(filename='example.twb')
            >>> anns.write_to_csv('example.csv')

        Keyword arguments:
        filename -- where to save the output
        columns  -- a list of columns to save, e.g. ['QTcF','TpTe']
        """
        self.data.to_csv(filename, columns=columns)

    def compute_hr_corrected_col(self, in_col, rr_col, out_col=None,
                                 method='Fridericia', rr_avg_secs=0,
                                 overwrite=False):
        """Compute a new column using existing measurement and RR columns.  RR may
        optionally be averaged with a running median filter.

        Keyword arguments:
        in_col      -- name of input column (e.g. 'QTp')
        rr_col      -- name of RR column
        out_col     -- name of output column (default: in_col+'cF' or 'cB')
        method      -- 'Fridericia' (default) or 'Bazett'
        overwrite   -- overwrite out_col if it already exists
        rr_avg_secs -- number of seconds to compute running RR average (0 = disable, default)
        """
        # TODO?: Framingham, etc.
        # TODO?: probably move this function to utils (and have time,'qt',rr
        # arrays as input), but still allow calling from here
        if not self.keep_data_loaded:
            raise RuntimeError("Cannot edit data columns without loading data.")
        methods = {
            'Fridericia': {'exp': 3.0, 'suffix': 'cF'},
            'Bazett':     {'exp': 2.0, 'suffix': 'cB'}
        }
        if out_col is None:
            out_col = in_col+methods[method]['suffix']
        if not overwrite and out_col in self.data.columns:
            raise RuntimeError("Cannot write to %s; column already exists." % out_col)
        exp = methods[method]['exp']
        vals = self.data[in_col].values.astype(float)
        rr   = self.data[rr_col].values.astype(float)
        if rr_avg_secs > 0:
            times = self.data.index.to_pydatetime()
            rr = medfilt(times, rr, filter_width=rr_avg_secs/60.0, centered=False)
        rr_sec = msec_to_sec(rr)
        corrected_vals = vals / np.power(rr_sec, 1/exp)
        self.data[out_col] = corrected_vals

    def compute_qtc(self, qt_col, rr_col, qtc_col=None, method='Fridericia',
                    rr_avg_secs=0, overwrite=False):
        """Compute a QTc column using existing QT and RR columns.  RR may optionally be
        averaged with a running median filter.

        Keyword arguments:
        qt_col      -- name of QT column
        rr_col      -- name of RR column
        qtc_col     -- name of output column (default: 'QTcB' or 'QTcF')
        method      -- 'Fridericia' (default) or 'Bazett'
        overwrite   -- overwrite out_col if it already exists
        rr_avg_secs -- number of seconds to compute running RR average (0 = disable, default)
        """
        self.compute_hr_corrected_col(qt_col, rr_col, qtc_col, method,
                                      rr_avg_secs, overwrite)

################################################################################
