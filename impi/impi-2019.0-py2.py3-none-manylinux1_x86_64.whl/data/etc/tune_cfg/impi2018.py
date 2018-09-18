#!/usr/bin/env python
#
# Copyright 2003-2018 Intel Corporation.
# 
# This software and the related documents are Intel copyrighted materials, and
# your use of them is governed by the express license under which they were
# provided to you (License). Unless the License provides otherwise, you may
# not use, modify, copy, publish, distribute, disclose or transmit this
# software or the related documents without Intel's prior written permission.
# 
# This software and the related documents are provided as is, with no express
# or implied warranties, other than those that are expressly stated in the
# License.
#

""" Custom converter of the optimization tree in json format
    to a legacy I_MPI_ADJUST format
"""

from __future__ import print_function

import json
import sys
from collections import OrderedDict


def main(m_key, m_doc):
    def print_tree(obj, header=[]):
        if isinstance(obj, dict):
            start = 0
            param = ""
            ranges = []
            for k, v in list(obj.items()):
                pos = k.find(search)
                if pos >= 0:
                    if not isinstance(v, dict) or len(v) != 1:
                        print ("ERROR: not a parameter: ", v)
                        quit()
                    for i, j in list(v.items()):
                        if param and i != param:
                            print ("ERROR: wrong parameter name: ", i)
                            quit()
                        param = i
                        end = int(k[pos + slen:])
                        ranges.append((int(j), start, end))
                        start = end + 1
                else:
                    print_tree(v, header + [str(k)])
            if ranges:
                franges = ["{}:{}-{}".format(alg, start, end) if end != -1 else str(alg) for alg, start, end in ranges]
                print (",".join(header) + ": " + param + "=" + ";".join(franges))
    m_obj = json.loads(m_doc, object_pairs_hook=OrderedDict)
    search = m_key + "="
    slen = len(search)
    print_tree(m_obj)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("ERROR: the script requires a range key argument: ", sys.argv[0])
        quit()
    range_key, doc = sys.argv[1], " ".join([line.rstrip() for line in sys.stdin])
    main(range_key, doc)
