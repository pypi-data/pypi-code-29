import unittest
from pairsnp import *
import numpy as np

class TestPairsnp(unittest.TestCase):
    def test_ambig(self):
        sparse_matrix, consensus, seq_names = calculate_snp_matrix("./pairsnp/tests/ambig.aln")
        d = calculate_distance_matrix(sparse_matrix, consensus, "dist", False)
        self.assertTrue(np.array_equal(d, np.array([[0,   0,  2,  1,  1],
                                        [0, 0,  2,  2,  2],
                                        [2, 2,  0,  3,  3],
                                        [1, 2,  3,  0,  0],
                                        [1, 2,  3,  0,  0]])))

    def test_ambig_with_n(self):
        sparse_matrix, consensus, seq_names = calculate_snp_matrix("./pairsnp/tests/ambig.aln")
        d = calculate_distance_matrix(sparse_matrix, consensus, "dist", True)
        self.assertTrue(np.array_equal(d, np.array([[0, 2,  4,  3,  3],
                                                    [2, 0,  4,  4,  4],
                                                    [4, 4,  0,  5,  5],
                                                    [3, 4,  5,  0,  0],
                                                    [3, 4,  5,  0,  0]])))

    def test_empty(self):
        assertRaises(calculate_snp_matrix("./pairsnp/tests/empty.aln"))

