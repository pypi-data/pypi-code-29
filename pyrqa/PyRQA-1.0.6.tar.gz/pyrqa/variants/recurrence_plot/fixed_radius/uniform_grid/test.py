#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Testing recurrence plot implementations according to the fixed radius neighbourhood.
"""

import sys
import unittest

import numpy as np


from pyrqa.selector import SingleSelector
from pyrqa.time_series import SingleTimeSeries
from pyrqa.variants.base_test import BaseTest
from pyrqa.variants.recurrence_plot.fixed_radius.baseline import Baseline
from pyrqa.variants.recurrence_plot.fixed_radius.execution_engine import ExecutionEngine

from pyrqa.variants.recurrence_plot.fixed_radius.uniform_grid.atomic_operations_column_materialisation_uncompressed_byte import AtomicOperationsColumnMaterialisationUncompressedByte
from pyrqa.variants.recurrence_plot.fixed_radius.uniform_grid.atomic_operations_row_materialisation_uncompressed_byte import AtomicOperationsRowMaterialisationUncompressedByte
from pyrqa.variants.recurrence_plot.fixed_radius.uniform_grid.sorting_column_materialisation_uncompressed_byte import SortingColumnMaterialisationUncompressedByte
from pyrqa.variants.recurrence_plot.fixed_radius.uniform_grid.sorting_row_materialisation_uncompressed_byte import SortingRowMaterialisationUncompressedByte

VARIANTS = (AtomicOperationsColumnMaterialisationUncompressedByte,
            AtomicOperationsRowMaterialisationUncompressedByte,
            SortingColumnMaterialisationUncompressedByte,
            SortingRowMaterialisationUncompressedByte)


class Test(BaseTest):
    """
    Tests for RQA, Fixed Radius, OpenCL.
    """

    def perform_recurrence_analysis_computations(self,
                                                 settings,
                                                 opencl=None,
                                                 verbose=False,
                                                 edge_length=None,
                                                 selector=SingleSelector(),
                                                 variants_kwargs=None,
                                                 all_variants=False):
        if opencl:
            opencl.reset()

        if not edge_length:
            edge_length = Test.time_series.number_of_vectors

        baseline = Baseline(settings,
                            verbose=verbose)

        result_baseline = baseline.run()

        if all_variants:
            execution_engine = ExecutionEngine(settings,
                                               opencl=opencl,
                                               verbose=False,
                                               edge_length=edge_length,
                                               selector=selector,
                                               variants=VARIANTS,
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_recurrence_plot_results(result_baseline,
                                                 result)

        else:
            for variant in VARIANTS:
                execution_engine = ExecutionEngine(settings,
                                                   opencl=opencl,
                                                   verbose=False,
                                                   edge_length=edge_length,
                                                   selector=selector,
                                                   variants=(variant,),
                                                   variants_kwargs=variants_kwargs)

                result = execution_engine.run()

                self.compare_recurrence_plot_results(result_baseline,
                                                     result,
                                                     variant)

if __name__ == "__main__":
    unittest.main()
