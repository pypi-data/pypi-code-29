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

from pyrqa.variants.rqa.fixed_radius.tree.ckdtree_materialisation_compressed_byte_no_recycling import CKDTreeMaterialisationCompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.tree.ckdtree_materialisation_uncompressed_byte_no_recycling import CKDTreeMaterialisationUncompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.tree.kdtree_materialisation_compressed_byte_no_recycling import KDTreeMaterialisationCompressedByteNoRecycling
from pyrqa.variants.rqa.fixed_radius.tree.kdtree_materialisation_uncompressed_byte_no_recycling import KDTreeMaterialisationUncompressedByteNoRecycling

VARIANTS = (CKDTreeMaterialisationCompressedByteNoRecycling,
            CKDTreeMaterialisationUncompressedByteNoRecycling,
            KDTreeMaterialisationCompressedByteNoRecycling,
            KDTreeMaterialisationUncompressedByteNoRecycling)


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
                                               matrix_representation=MatrixRepresentation.CSC,
                                               variants=(CKDTreeMaterialisationCompressedByteNoRecycling,
                                                         KDTreeMaterialisationCompressedByteNoRecycling),
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_rqa_results(result_baseline,
                                     result)

            execution_engine = ExecutionEngine(settings,
                                               opencl=opencl,
                                               verbose=False,
                                               edge_length=edge_length,
                                               selector=selector,
                                               matrix_representation=MatrixRepresentation.Uncompressed,
                                               variants=(CKDTreeMaterialisationUncompressedByteNoRecycling,
                                                         KDTreeMaterialisationUncompressedByteNoRecycling),
                                               variants_kwargs=variants_kwargs)

            result = execution_engine.run()

            self.compare_rqa_results(result_baseline,
                                     result)
        else:
            for variant in VARIANTS:
                if variant == CKDTreeMaterialisationCompressedByteNoRecycling or variant == KDTreeMaterialisationCompressedByteNoRecycling:
                    matrix_representation = MatrixRepresentation.CSC
                elif variant == CKDTreeMaterialisationUncompressedByteNoRecycling or variant == KDTreeMaterialisationUncompressedByteNoRecycling:
                    matrix_representation = MatrixRepresentation.Uncompressed

                execution_engine = ExecutionEngine(settings,
                                                   opencl=opencl,
                                                   verbose=False,
                                                   edge_length=edge_length,
                                                   selector=selector,
                                                   matrix_representation=matrix_representation,
                                                   variants=(variant,),
                                                   variants_kwargs=variants_kwargs)

                result = execution_engine.run()

                self.compare_rqa_results(result_baseline,
                                         result,
                                         variant=variant)

if __name__ == "__main__":
    unittest.main()
