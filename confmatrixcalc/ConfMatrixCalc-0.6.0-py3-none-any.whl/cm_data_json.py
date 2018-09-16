"""Load / save stimulus-response data in serialized json file format.
One file may include several StimRespRecord instances,
for one or more subjects and one or more test-conditions.
"""

from pathlib import Path
import json
import logging

from ConfMatrixCalc import __version__
from . import cm_base


logger = logging.getLogger(__name__)


# ---------------------------------------------------------
class StimRespFile(cm_base.StimRespFile):
    """Container of phoneme-identification responses
    from one or more listeners, in one or more test conditions,
    represented as a sequence of StimRespRecord instances.
    This class is used mainly to read / write a json file.
    """
    def __init__(self, records=None, file_path=None, test_factors=None, **kwargs):
        """
        :param records: (optional) list of StimRespRecord instances.
        :param file_path: (optional) Path instance for READING
            Another path may be defined in the save method.
        :param test_factors: (optional) dict with elements (test_factor, tf_cat_list),
            as saved in a ConfMatrixFrame instance
        """
        super().__init__(file_path, test_factors)
        if records is None and file_path is not None:
            # self is used for READING
            records = self.load()  #file_path, test_factors)
        self.records = records

    def __repr__(self):
        return (f'StimRespFile(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                             for (key, v) in vars(self).items()) +
                '\n\t)')

    def __iter__(self):
        """Iterate over all records loaded from a file
        """
        path_test_cond = self.path_test_cond()
        for r in self.records:
            # merge path test-cond with test-cond loaded from file:
            test_cond = path_test_cond.copy()
            test_cond.update(r['test_cond'])
            r['test_cond'] = test_cond
            yield r

    def load(self):
        """Load phoneme-identification data from given file.
        :return: records = list of dicts loaded from file
        """
        try:
            with self.file_path.open() as f:
                file_dict = json.load(f)
            file_dict = file_dict['StimRespFile']
            if '__version__' in file_dict.keys() and file_dict['__version__'] < __version__:
                _update_version_format(file_dict)
            return file_dict['records']
        except (KeyError, json.decoder.JSONDecodeError):
            raise cm_base.FileReadError(f'File {self.file_path} does not contain StimRespFile data')

    def save(self, f_name=None, dir='.'):
        """Save sequence of StimRespRecord dicts to file
        :param dir: (optional) path to directory for saving
        :param f_name: (optional) file name
        :return: None
        """
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        # make sure it exists, create new hierarchy if needed
        if f_name is None:
            f_name = self.records[0].subject
        file_path = (dir / f_name).with_suffix('.json')
        self_dict = {'records': self.records,
                     '__version__': __version__}
        with open(file_path, 'wt') as f:
            json.dump({'StimRespFile': self_dict}, f)
        self.file_path = file_path


# ------------------------------------------------ internal module help functions

def _update_version_format(p_dict):
    """Update contents from an input json file to fit current StimRespFile version
    :param p_dict: a PairedCompRecord dict saved with an old package version
    :return: None
    """
    pass  # nothing to update

