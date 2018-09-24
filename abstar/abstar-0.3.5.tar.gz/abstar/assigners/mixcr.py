#!/usr/bin/env python
# filename: mixcr.py

#
# Copyright (c) 2016 Bryan Briney
# License: The MIT license (http://opensource.org/licenses/MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import csv
import os
import shutil
import subprocess as sp
import sys
from tempfile import NamedTemporaryFile
import traceback

from abutils.core.sequence import Sequence
from abutils.utils.pipeline import make_dir

from .assigner import BaseAssigner
from ..core.germline import GermlineSegment, get_germline_database_directory
from ..core.vdj import VDJ


class MiXCR(BaseAssigner):
    """
    docstring for MiXCRAssigner
    """

    def __init__(self, species, receptor=None):
        super(MiXCR, self).__init__(species)


    def __call__(self, sequence_file, file_format):
        # check for the presence of the MiXCR binary
        if not self._check_for_binary():
            self._print_binary_not_found_error()
            sys.exit(1)

        ## !! This needs to happen earlier in the process, before splitting into jobs !! ##
        # # copy the appropriate germline DB to th MiXCR working directory
        # db_files = list_files(os.path.join(self.germline_directory, 'mixcr'), extension='json')
        # working_dir = os.path.expanduser('~/.mixcr/libraries')
        # make_dir(working_dir)
        # for f in db_files:
        #     shutil.copy(f, working_dir)


        # make germline alignments
        vdjca_file = NamedTemporaryFile(delete=False, mode='r')
        aln_cmd = 'mixcr align --save-description -s abstar-{} -b abstar -t 1 {} {}'.format(self.species,
                                                                                            sequence_file,
                                                                                            vdjca_file.name)
        aln = sp.Popen(aln_cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = aln.communicate()
        # export alignments
        aln_file = NamedTemporaryFile(delete=False, mode='r')
        aln_opts = ['-descR1', '-vHitsWithScore', '-dHitsWithScore', '-jHitsWithScore', '-sequence', '-OmaxHits=6']
        export_cmd = 'mixcr exportAlignments {} {} {}'.format(' '.join(aln_opts),
                                                              vdjca_file.name,
                                                              aln_file.name)
        export = sp.Popen(export_cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = export.communicate()
        # read alignments
        reader = csv.DictReader(aln_file, delimiter='\t')
        for row in reader:
            s = Sequence(row['sequence'], id=row['descR1'])
            try:
                # V-gene
                vhits = row['vHitsWithScore'].strip().split(',')
                v = self._process_germline_assignments(vhits)
                # D-gene
                dhits = row['dHitsWithScore'].strip().split(',')
                if dhits:
                    d = self._process_germline_assignments(dhits)
                else:
                    d = None
                # J-gene
                jhits = row['jHitsWithScore'].strip().split(',')
                j = self._process_germline_assignments(jhits)
                vdj = VDJ(s, v=v, d=d, j=j)
                self.assigned.append(vdj)
            except:
                vdj = VDJ(s)
                vdj.exception('GERMLINE GENE ASSIGNMENT ERROR', traceback.format_exc())
                self.unassigned.append(vdj)
        os.unlink(vdjca_file.name)
        os.unlink(aln_file.name)


    def _process_germline_assignments(self, hits):
        hitlist = []
        for hit in hits:
            full, score = hit.rstrip(')').split('(')
            hitlist.append({'full': full, 'score': int(score)})
        hitlist.sort(key=lambda x: x['score'], reverse=True)
        top_hit = hitlist[0]
        other_hits = hitlist[1:]
        others = [GermlineSegment(o['full'], self.species, score=o['score']) for o in other_hits]
        gs = GermlineSegment(top_hit['full'], self.species, score=top_hit['score'], others=others)
        return gs


    def _check_for_binary(self):
        for path in os.environ['PATH'].split(':'):
            if os.path.exists(os.path.join(path, 'mixcr')):
                return True
        return False


    def _print_binary_not_found_error(self):
        e = '\n\nERROR: nMiXCR binary not found!'
        e += '\nPlease verify that MiXCR is installed and that the binary location is in your system path.'
        e += '\n\n'
        print(e)



def copy_mixcr_library_file(species, receptor):
    db_dir = get_germline_database_directory(species, receptor)
    db_file = os.path.join(db_dir, 'mixcr/vdj.json')
    copy_dir = os.path.expanduser('~/.mixcr/libraries')
    copy_file = os.path.join(copy_dir, 'abstar-{}.json'.format(species))
    make_dir(copy_dir)
    shutil.copy(db_file, copy_file)



