# Copyright 2013-2014 Oliver Cope
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from morf.compat import ustr


def iterable(ob):
    """
    Return True if ``ob`` is iterable and not a string type
    """
    try:
        iter(ob)
    except TypeError:
        return False
    return not isinstance(ob, (bytes, ustr))
