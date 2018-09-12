# coding=utf-8
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

u"""Define version number here and read it from setup.py automatically"""
from __future__ import absolute_import
import sys

if sys.version_info.major == 2:
    __version__ = u"0.2.1.a27"  # coverage: ignore
else:
    __version__ = u"0.2.1.a35"
