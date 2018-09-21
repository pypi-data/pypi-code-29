import os
import sys
import numpy as np
from Bio import AlignIO

sys.path.insert(1, os.path.abspath(os.path.join(sys.path[0], "..")))
from modelestimator._bootstraper.bootstraper import bootstraper
from modelestimator._handle_input.handle_input_file import handle_input_file

def test_bootstrap_1():
    REFERENCE_FILE_PATH = os.path.abspath(os.path.join(sys.path[0], "tests\\test_bootstrap_1\\1000LongMultialignment.phylip"))
    MULTIALIGNMENT = handle_input_file(REFERENCE_FILE_PATH, "phylip")

    RESAMPLINGS = 25
    THRESHOLD = 0.001
    BOOTSTRAP_NORM,_ = bootstraper(RESAMPLINGS, THRESHOLD, MULTIALIGNMENT)
    assert (BOOTSTRAP_NORM > 35) and (BOOTSTRAP_NORM < 45)

test_bootstrap_1()