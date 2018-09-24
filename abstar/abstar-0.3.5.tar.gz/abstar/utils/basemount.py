#!/usr/bin/python
# filename: basemount.py

#
# Copyright (c) 2018 Bryan Briney
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

from datetime import datetime
from glob import glob
import os
import shutil

import arrow

from abutils.utils.decorators import lazy_property
from abutils.utils.pipeline import make_dir
from abutils.utils.progbar import progress_bar



class BasemountProject():
    '''

    '''
    def __init__(self, parent_dir):
        self.parent_dir = os.path.abspath(parent_dir)
        self.name = os.path.basename(self.parent_dir)
    

    @lazy_property
    def date(self):
        app_sessions_dir = os.path.join(self.parent_dir, 'AppSessions')
        app_sessions = glob(os.path.join(app_sessions_dir, 'FASTQ Generation*'))
        try:
            app_session = sorted(app_sessions)[0]
            date = arrow.get(os.path.basename(app_session).lstrip('FASTQ Generation '))
        except:
            date = None
        return date

    @lazy_property
    def fastqs(self):
        fastq_dir = os.path.join(self.parent_dir, 'Samples')
        fastqs = []
        for subdir in glob(os.path.join(fastq_dir, '*')):
            files_subdir = os.path.join(subdir, 'Files')
            if os.path.exists(files_subdir):
                fastqs += glob(os.path.join(files_subdir, '*.fastq.gz'))
        return sorted(fastqs)


    @property
    def num_fastqs(self):
        return len(self.fastqs)

    
    def copy_fastqs(self, destination_dir, show_progress=True):
        make_dir(destination_dir)
        if show_progress:
            start = datetime.now()
            progress_bar(0, self.num_fastqs, start_time=start)
        for i, fastq_file in enumerate(self.fastqs, 1):
            shutil.copy(fastq_file, destination_dir)
            if show_progress:
                is_complete = i == self.num_fastqs
                progress_bar(i, self.num_fastqs, start_time=start, complete=is_complete)





def get_basemount_projects(basemount_dir):
    projects_dir = os.path.join(basemount_dir, 'Projects')
    projects = [BasemountProject(d) for d in glob(os.path.join(projects_dir, '*'))]
    