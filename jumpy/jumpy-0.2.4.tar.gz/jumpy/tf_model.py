################################################################################
# Copyright (c) 2015-2018 Skymind, Inc.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
################################################################################

from .java_classes import TFGraphMapper, Nd4j, NDArrayIndex
from .ndarray import array

class TFModel(object):
    def __init__(self, filepath):
        self.sd = TFGraphMapper.getInstance().importGraph(filepath)

    def __call__(self, input):
        input = array(input).array  # INDArray
        shape = input.shape()
        self.sd.associateArrayWithVariable(input)
        out = self.sd.execAndEndResult()
        return array(out)
