"""General utility classes and functions for internal use.
"""


class FileReadError(RuntimeError):
    """Any type of exception during file read
    to be sub-classed for more specific variants depending on file format
    """


# ---------------------------------------------------------
class StimRespFile:
    """Container of phoneme-identification responses
    from one or more listeners, in one or more test conditions,
    represented as a sequence of StimRespRecord instances.

    This super-class is used mainly for READiNG a data file.
    It derives test-conditions from path strings,
    to be used for test factors not defined in the file itself.

    Sub-classes must be defined for each specific file format.
    """
    def __init__(self, file_path=None, test_factors=None):
        """
        :param file_path: (optional) Path instance for READING
            Another path may be defined in the save method.
        :param test_factors: (optional) dict with elements (test_factor, tf_cat_list),
            as saved in a ConfMatrixFrame instance
        """
        self.file_path = file_path
        if test_factors is None:
            test_factors = dict()
        self.test_factors = test_factors

    def __repr__(self):
        return (f'StimRespFile(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                             for (key, v) in vars(self).items()) +
                '\n\t)')

    def path_test_cond(self):
        """Create a dict of test conditions defined by path-string
        """
        return {tf: _find_test_cond_in_path(tc_list, str(self.file_path))
                for (tf, tc_list) in self.test_factors.items()}


# ---------------------------------------- private help function:

def _find_test_cond_in_path(tf_categories, path_string):
    """Find test-condition label as sub-string of given path string.
    :param tf_categories: list of possible test-factor category labels
    :param path_string: string
    :return: test_cond = first element in tf_cat_list for which
        a matching sub-string was found in path_string.

    Arne Leijon, 2018-09-09
    """
    def test_cond_in_file(tc, path):
        """Check if tc agrees with file path_string string
        :param tc: test-condition code, string or tuple of strings
        :param path: string path_string
        :return: boolean True if a match was found
        """
        if isinstance(tc, str):
            return tc in path
        elif type(tc) is tuple:
            return all(tc_i in path for tc_i in tc)
        else:
            return False
        # ----------------------------------------

    for tc in tf_categories:
        # if tc in str(path_string):
        # **************** allow tc to be a tuple of strings ???
        if test_cond_in_file(tc, path_string):
            return tc
    return None
