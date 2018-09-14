#!/usr/bin/python
#
# This file is part of PyRQA.
# Copyright 2015 Tobias Rawald, Mike Sips.

"""
Testing recurrence quantification analysis implementations according to the fixed radius neighbourhood.
"""

import unittest

from pyrqa.selector import SingleSelector
from pyrqa.types import MatrixRepresentation
from pyrqa.variants.base_test import BaseTest
from pyrqa.variants.rqa.fixed_radius.baseline import Baseline
from pyrqa.variants.rqa.fixed_radius.execution_engine import ExecutionEngine

from pyrqa.variants.rqa.fixed_radius.uniform_grid.atomic_operations_column_materialisation_uncompressed_bit_no_recycling import AtomicOperationsColumnMaterialisationUncompressedBitNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.atomic_operations_column_materialisation_uncompressed_byte_no_recycling import AtomicOperationsColumnMaterialisationUncompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.atomic_operations_row_materialisation_uncompressed_bit_no_recycling import AtomicOperationsRowMaterialisationUncompressedBitNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.atomic_operations_row_materialisation_uncompressed_byte_no_recycling import AtomicOperationsRowMaterialisationUncompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.sorting_column_materialisation_uncompressed_bit_no_recycling import SortingColumnMaterialisationUncompressedBitNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.sorting_column_materialisation_uncompressed_byte_no_recycling import SortingColumnMaterialisationUncompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.sorting_row_materialisation_uncompressed_bit_no_recycling import SortingRowMaterialisationUncompressedBitNoRecycling
from pyrqa.variants.rqa.fixed_radius.uniform_grid.sorting_row_materialisation_uncompressed_byte_no_recycling import SortingRowMaterialisationUncompressedByteNoRecycling

VARIANTS = (AtomicOperationsColumnMaterialisationUncompressedBitNoRecycling,
            AtomicOperationsColumnMaterialisationUncompressedByteNoRecycling,
            AtomicOperationsRowMaterialisationUncompressedBitNoRecycling,
            AtomicOperationsRowMaterialisationUncompressedByteNoRecycling,
            SortingColumnMaterialisationUncompressedBitNoRecycling,
            SortingColumnMaterialisationUncompressedByteNoRecycling,
            SortingRowMaterialisationUncompressedBitNoRecycling,
            SortingRowMaterialisationUncompressedByteNoRecycling)


class Test(BaseTest):
    """
    Tests for RQA, Fixed Radius.
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
                                               matrix_representation=MatrixRepresentation.Uncompressed,
                                               variants=VARIANTS,
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_rqa_results(result_baseline,
                                     result)
        else:
            for variant in VARIANTS:
                execution_engine = ExecutionEngine(settings,
                                                   opencl=opencl,
                                                   verbose=False,
                                                   edge_length=edge_length,
                                                   selector=selector,
                                                   matrix_representation=MatrixRepresentation.Uncompressed,
                                                   variants=(variant,),
                                                   variants_kwargs=variants_kwargs)

                result = execution_engine.run()

                self.compare_rqa_results(result_baseline,
                                         result,
                                         variant=variant)

if __name__ == "__main__":
    unittest.main()
