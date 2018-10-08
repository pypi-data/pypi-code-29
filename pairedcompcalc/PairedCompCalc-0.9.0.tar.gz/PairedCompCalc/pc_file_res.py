"""Functions to read Paired-comparison test results,
stored in file format defined by Martin Dahlquist, 2002

*** Version History:
2018-09-30, sub-class of PairedCompFile, iterator of PairedCompItem objects
"""

# *** allow save in res format ???

# from pathlib import Path
# import datetime as dt

from PairedCompCalc import pc_base


# ------------------------------------------ Exception:
class FileFormatError(RuntimeError):
    """Signal any form of file format error when reading
    """


# ----------------------------------------------------------------
class PairedCompFile(pc_base.PairedCompFile):
    """PairedCompFile variant to read / write a *.res file
    containing paired-comparison results
    for ONE subject and ONE perceptual attribute,
    in test-conditions specified only by file path-string.
    """
    def __init__(self,
                 file_path,
                 pcf,
                 contents=None,
                 **kwargs):
        """
        :param file_path: path for existing *.res file
        :param pcf: a PairedCompFrame instance
        :param contents: (optional) dict with all (key, value) pairs for this format
        :param kwargs: any additional params, NOT USED
        """
        super().__init__(file_path, pcf)
        # self.forced_choice = forced_choice
        if contents is None:  # read from file
            with open_encoded_txt(self.file_path) as f:
                self.contents = load(f, self.pcf.forced_choice)
        else:  # prepare to save contents to file
            self.contents = contents

    def __repr__(self):
        return (f'PairedCompFile(\n\t' +
                ',\n\t'.join(f'{key}={repr(v)}'
                            for (key, v) in vars(self).items()) +
                '\n\t)')

    def __iter__(self):
        """generator of PairedCompItem instances,
        one for each result row in file
        """
        subject = self.contents['subject']
        attr = self.contents['attribute']
        test_cond = self.path_test_cond()
        for sr in self.contents['result']:
            yield pc_base.PairedCompItem(subject, attr, *sr, test_cond)


# def save(pcr, f, pcf):  # ***********************************
#     """Save self.contents in old 2002 format
#     :param pcr: one pc_data.PairedCompRecord instance
#     :param f: open file object for writing
#     :return: None
#     NOTE: this does not handle test_factors !
#     """
#     # convert it to old-class object
#     pcr2002 = PairedCompRecord2002(subject=pcr.subject,
#                                    systems=pcr.systems,
#                                    attribute=pcr.attribute,
#                                    result=pcr.result,
#                                    **pcr.othr)
#
#     pcr_dict = {'PairedCompRecord': pcr2002.__dict__}
#     dump(pcr_dict, f, pcf.forced_choice)


# def dump(session_dict, f, forced_choice):
#     """write a complete result for one PairedCompRecord2002
#     in ORCA text format, as defined by Dahlquist, 2002
#     :param session_dict: { 'PairedCompRecord': s }, where
#         s includes properties for one PairedCompRecord2002 object,
#         obtained, e.g., as s.__dict__
#     :param f: file-like object, allowing f.write() operations
#         If already existing, the f is over-written without warning
#     :param forced_choice: boolean = pc_data.PairedCompFrame.forced_choice
#     :return: None
#     Exceptions: KeyError is raised if session_dict does not include required data.
#     """
#     s = session_dict['PairedCompRecord']
#     with f:
#         f.write(s['comment'] + '\n')
#         f.write(s['subject'] + '\n')
#         # t = s.time_stamp
#         f.write(s['time_stamp'] + '\n')
#         f.write(s['attribute'] + '\n')
#         response_labels = s['response_labels']
#         f.write(''.join('\"' + m + '\"\n' for m in response_labels))
#         systems = s['systems']
#         n_systems = len(systems)
#         f.write(f'{n_systems},{len(response_labels)},2\n')
#         f.write(''.join(sys +'\n' for sys in systems))
#         f.write('\"matris\"\n')
#         # ***** calculate summary matrix ********************
#         for n in range(n_systems):
#             f.write(','.join(['0' for m in range(n_systems)]) + '\n')
#             # *** just a zero matrix, not used for analysis anyway
#         result = s['result']
#         f.write('\"antal stimuli\"\n' +
#                 f'{len(result)}\n')
#         f.write('\"Stim1\",\"Stim1\",\"Resp\",\"Rate\",\"Rep\"\n')
#         for sr in result:
#             ((a, b), r) = sr[0:2]
#             (i, j) = (systems.index(a), systems.index(b))
#             choice = (0 if r == 0 else 2 if r > 0 else 1)
#             # magn = abs(r) if s['forced_choice'] else 1 + abs(r)
#             magn = abs(r) if forced_choice else 1 + abs(r)
#             # NOTE: for historical reasons, magn must be
#             # index into response_labels, using MatLab:s origin-one indexing.
#             # Therefore, magn must always be 1, 2, etc. never = 0.
#             f.write(f'{1+i},{1+j},{choice},{magn},0\n')


def load(f, forced_choice):
    """Read one file saved in old res format
    as defined by Martin Dahlquist, 2002
    :param f: open file object, allowing r.readline() operations
    :param forced_choice: boolean switch
    :return: dict with PairedCompRecord attributes from file,
        OR None, if any error encountered
    """
    def clean(s):
        """strip away unwanted characters from a string
        :param s: string
        :return: cleaned string
        """
        clean_s = s.strip('\n\"')
        if len(clean_s) == 0:
            raise FileFormatError(f'Unexpected empty line in {f_name}')
        else:
            return clean_s

    def decode_res(r, systems):
        """recode response item from res format to PairedCompRecord standards
        :param r: one paired-comparison result line (stim_1, stim_2, choice, magn)
        :param systems: list of string labels, corresponding to system indices in r
        :return: tuple (pair, response) in PairedCompRecord format, where
            pair = tuple of system string labels (A, B) for presented pair
            response = integer in {- max_difference,..., + max_difference}
        """
        (i,j, choice, m) = r[:4]
        pair = (systems[i-1], systems[j-1])  # index origin 1 in res file
        # m = (0 if choice == 0 else m-1 if forced_choice else m)
        if choice == 0:
            m = 0
        elif not forced_choice:
            m -= 1  # invert the change in function dump
        if choice == 1:
            m = - m
        elif choice < 0 or choice > 2:
            raise FileFormatError(f'Illegal choice value in result in {f_name}')
        return pair, m  #, tc
    # -----------------------------------------
    f_name = f.name
    # test_cond = decode_test_condition(f_name, test_factors)
    s = dict()  # dict for result
    with f:
        s['comment'] = clean(f.readline())
        s['subject'] = clean(f.readline())
        s['time_stamp'] = clean(f.readline())
        a = clean(f.readline())
        a = a.replace('\"', '')
        a = a.replace(',', ' ')
        s['attribute'] = a.split(sep=' ')[0]
        s['response_labels'] = r_labels = []
        while True:
            l = f.readline()
            if 0 == l.find('\"'):
                r_labels.append(clean(l))
            else:
                nsr = [int(n) for n in l.split(sep=',')]
                (n_systems, n_resp) = nsr[:2]
                break
        if n_resp != len(r_labels):
            raise FileFormatError(f'Inconsistent number of response labels in {f_name}')
            # ******* logger.warning is enough ?
        s['systems'] = systems = [clean(f.readline())
                                  for n in range(n_systems)]
        if 0 != (f.readline()).find('\"matr'):
            raise FileFormatError(f'matrix label not found in {f_name}')
        s['summary'] = [[int(n) for n in f.readline().split(sep=',')]
                        for n in range(n_systems)]
        l = f.readline()
        if (0 != l.find('\"num') and
            0 != l.find('\"ant')):
            raise FileFormatError(f'Number of results not found in {f_name}')
        n_pres = int(f.readline())
        s['result'] = result = []
        l = f.readline()
        if 0 != l.find('\"Stim'):
            raise FileFormatError(f'Unexpected result header in {f_name}')
        l = f.readline()
        while 0 < len(l):  # read until EOF
            r = [int(n) for n in l.split(sep=',')]
            result.append(decode_res(r, systems))  # ************ test_cond))
            l = f.readline()
        if n_pres != len(result):
            raise FileFormatError(f'Inconsistent number of results in {f_name}')
        # if any(abs(r[1]) >= len(r_labels) for r in result):
        #     raise FileFormatError(f'Response outside response_labels in {f_name}')
        # ****** this check must consider forced_choice *******
        if forced_choice and any(r[1] == 0 for r in result):
            raise FileFormatError(f'Expected forced_choice, but found zero response in {f_name}')
        return s
        # --------------------- OK: whole file has been read without problem


def open_encoded_txt(path):
    """Try to open a text file with a working encoding
    :param path: Path object or path string identifying a file
    :return: open file object
        OR None, if no working encoding was found

    Method: just try some encodings until a working one is found
    """
    encodings = ['utf-8', 'ISO-8859-1']
    for enc in encodings:
        try:
            with open(path, mode='rt', encoding=enc) as f:
                l = f.read()
            # No error: OK
            return open(path, mode='rt', encoding=enc)
            # open it again with right encoding
        except ValueError as e:
            pass  # try next encoding instead
    raise FileFormatError(f'Unknown text encoding in {path}')
