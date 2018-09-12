import os
import re
class EventHandler:
    def __init__(self, fname, suffix = '_events'):
        # Removing extension and suffix (if present)
        fname = re.sub( r'\.tsv$', '', fname )
        fname = re.sub( suffix + '$', '', fname )
        self.__filename = '{}{}.tsv'.format(fname, suffix)
        self.trials = [] # First line should be the header

    def get_filename(self):
        return self.__filename

    # TODO: Check if trials are lists, or join will fail
    def set_trials(self, trials):
        self.trials = trials

    def export_bids(self):
        # Preparing tsv lines
        output = ''
        for line in self.trials:
            output += "\t".join([str(i) for i in line]) + "\n"

        # Saving output
        with open(self.__filename, 'w') as f:
            f.write(output)