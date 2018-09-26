
################################### Imports: ###################################

import pandas as pd
import datetime as dt
from .utils import compute_pctls

#################################### Class: ####################################

class Cohort:

    def __init__(self, **kwargs):
        """A collection of Recordings.

        Keyword arguments:
        anns -- a list of Recordings
        name -- a name for this cohort, e.g. 'adult male'
        """
        self.anns  = kwargs.pop('anns', [])
        self.name  = kwargs.pop('name', None)
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
        # TODO?: somehow correct weights based on length of recording as well.
        # i.e. normalize to 24 hours.  so e.g. with 2 recs of 24 and 26 hours,
        # the extra 2 hours on one doesn't get double weight.
        if measurement in self.percentiles and not recompute:
            return
        self.percentiles[measurement] = compute_pctls(measurement, anns=self.anns,
                                                      weights=weights)

    def nsubj(self):
        """Return the number of unique subjects in this cohort.  This is based purely on
        the Recordings (anns) present, not on measurement percentile files.
        """
        if self.anns == []:
            if len(self.percentiles) > 0:
                return None  # percentiles may have been loaded from CSV without providing anns
            elif len(self.percentiles) == 0:
                return 0  # nothing loaded
        subjids = list(set([ann.subjid for ann in self.anns]))
        if None in subjids:
            # if any subjid is unknown, nsubj is unknown
            return None
        else:
            return len(subjids)

    def nrec(self):
        """Return the number of Recordings in this cohort.  This is based purely on the
        Recordings (anns) present, not on measurement percentile files.
        """
        if self.anns == []:
            if len(self.percentiles) > 0:
                return None  # percentiles may have been loaded from CSV without providing anns
            elif len(self.percentiles) == 0:
                return 0  # nothing loaded
        return len(self.anns)

    def nbeats(self):
        """Return the number of beats in this cohort.  This is based purely on the
        Recordings (anns) present, not on measurement percentile files.
        """
        raise NotImplementedError()

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
