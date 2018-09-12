# Copyright 2018 Deep Air. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""vis_tools"""

from tabulate import tabulate
import datetime
import time

def unique_stats(df):
    temp = []
    for column in df:
        temp.append([column, len(df[column].unique()), len(df[column])])
    print(tabulate(temp, headers=['Field', 'Unique', 'Total']))


def _log_with_timestamp(message):
    '''
        prints message on console
        input :
            message     : msg to print (string)
    '''
    print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ']:'
          + message)
