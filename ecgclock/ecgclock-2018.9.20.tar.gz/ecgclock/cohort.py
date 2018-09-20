
################################### Imports: ###################################

import pandas as pd
import numpy as np
import datetime as dt

#################################### Class: ####################################

class Cohort:

    def __init__(self, **kwargs):
        """Collection of ECGMeasurements objects.

        Keyword arguments:
        anns -- a list of ECGMeasurements
        name -- a name for this cohort, e.g. 'adult male'
        """
        self.anns = kwargs.pop('anns', [])
        self.name = kwargs.pop('name', [])
        self.percentiles = {}

    def compute_pctls(self, measurement, weights='beat', recompute=False):
        """Compute percentile ranges for a given measurement, at a resolution of 1
        minute.  The results will be stored in self.percentiles[measurement].
        Note: weighting by subject or recording can inadvertently give lots of
        weight to noise, particularly in small cohorts.

        Keyword arguments:
        measurement -- which measurement to analyze, e.g. 'QTcF_II'
        weights     -- give equal weight to each 'beat', 'recording', or 'subject'
        recompute   -- recompute even when the results already exist
        """
        # TODO: some kind of upsampling or downsampling of anns in order to
        # weight by recording/subject
        # TODO?: support arbitrary resolution
        if measurement in self.percentiles and not recompute:
            return
        bins = {}
        for minute in range(1440):
            bins[minute] = []
        if weights == 'beat':
            for ann in self.anns:
                ann.data['min_of_day'] = ann.data.index.minute + 60*ann.data.index.hour
                for minute in range(1440):
                    relevant_rows = ann.data[ann.data['min_of_day'] == minute]
                    bins[minute] += relevant_rows[measurement].values.tolist()
        elif weights == 'recording':
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
        self.percentiles[measurement] = results

    def nsubj(self):
        """Return the number of unique subjects in this cohort.  Not available if
        percentiles were loaded from CSV.
        """
        if self.anns == []:
            return None
        subjids = list(set([ann.subjid for ann in self.anns]))
        if None in subjids:
            # if any subjid is unknown, nsubj is unknown
            return None
        else:
            return len(subjids)

    def nrec(self):
        """Return the number of recordings (ECGMeasurements objects) in this cohort.
        Not available if percentiles were loaded from CSV.
        """
        if self.anns == []:
            return None
        return len(self.anns)

    def save_pctls(self, measurement, filename):
        """Save percentile ranges to a CSV file.  Assuming we were computing QTc
        percentiles, the output will look like:

          First row:      time,    0%,    1%,    2%, ...
          Second row: 00:00:30, <QTc>, <QTc>, <QTc>, ...
          Third row:  00:01:30, <QTc>, <QTc>, <QTc>, ...
          ...

        Keyword arguments:
        measurement -- which measurement to save, e.g. 'QTcF_II'
        filename    -- where to save, e.g. 'qtcf.csv'
        """
        headers = [str(i) + '%' for i in range(101)]
        self.percentiles[measurement].to_csv(filename, header=headers)

    def load_pctls(self, measurement, filename):
        """Load percentile ranges from a CSV file.

        Keyword arguments:
        measurement -- which measurement the file contains, e.g. 'QTcF_II'
        filename    -- file to load
        """
        self.percentiles[measurement] = pd.read_csv(filename, index_col='time')
        self.percentiles[measurement].columns = range(101)  # TODO: may be safer to int(strip%(header)))
        self.percentiles[measurement].index = pd.Index(
            data = [dt.time(hour=h,minute=m,second=30) for h in range(24) for m in range(60)],
            name = 'time'
        )

################################################################################
