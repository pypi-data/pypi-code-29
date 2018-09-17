import os
import unittest

from xl_sudoku_solver import Solver, load_from_file


class TestSolver(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,1,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,8,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,1,9,8],
            [1,9,3,5,2,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,8,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,8,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,3,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,1,6,2]
        ]))
        self.assertFalse(Solver.validate([
            [4,1,5,8,7,9,6,2,3],
            [6,8,9,2,1,3,7,4,5],
            [2,3,7,4,6,5,8,9,8],
            [1,9,2,5,3,7,4,8,6],
            [8,7,6,1,2,4,5,3,9],
            [3,5,4,6,9,8,2,1,7],
            [5,6,1,9,8,2,2,7,4],
            [7,2,8,3,4,6,9,5,1],
            [9,4,3,7,5,1,1,6,3]
        ]))

    def test_solve(self):

        def path(testfile):
            return os.path.join(os.path.dirname(__file__), testfile)

        Solver.solve(load_from_file(path('problem-simple-1.txt'))).draw()
        Solver.solve(load_from_file(path('problem-simple-2.txt'))).draw()
        Solver.solve(load_from_file(path('problem-primary-1.txt'))).draw()
        Solver.solve(load_from_file(path('problem-primary-2.txt'))).draw()
        Solver.solve(load_from_file(path('problem-medium-1.txt'))).draw()
        Solver.solve(load_from_file(path('problem-medium-2.txt'))).draw()
        Solver.solve(load_from_file(path('problem-senior-1.txt'))).draw()
        Solver.solve(load_from_file(path('problem-senior-2.txt'))).draw()
        Solver.solve(load_from_file(path('problem-memory.txt'))).draw()
        Solver.solve(load_from_file(path('problem-extreme-1.txt'))).draw()
        Solver.solve(load_from_file(path('problem-extreme-2.txt'))).draw()
        Solver.solve(load_from_file(path('problem-extreme-3.txt'))).draw()
