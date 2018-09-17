import unittest
from xl_sudoku_solver.cell import Cell
from xl_sudoku_solver.exceptions import *

IMPOSSIBLE_VALUES = [False,False,False,False,False,False,False,False,False]
ALL_POSSIBLE_VALUES = [True,True,True,True,True,True,True,True,True]

class TestCell(unittest.TestCase):

    def test_init(self):
        self.assertEqual(len(Cell()._values), 9)
        self.assertEqual(Cell()._values, ALL_POSSIBLE_VALUES)

    def test_minus(self):
        self.assertEqual(Cell(ALL_POSSIBLE_VALUES).minus(1), Cell([False,True,True,True,True,True,True,True,True]))
        self.assertEqual(Cell(ALL_POSSIBLE_VALUES).minus(2,3), Cell([True,False,False,True,True,True,True,True,True]))

    def test_get_one(self):
        cell = Cell(ALL_POSSIBLE_VALUES)
        cell.minus(1,2,3)
        self.assertEqual(cell.get_one(), 4)
        cell.minus(5)
        self.assertEqual(cell.get_one(), 4)
        cell.minus(4)
        self.assertEqual(cell.get_one(), 6)

    def test_len(self):
        cell = Cell(ALL_POSSIBLE_VALUES)
        cell.minus(1,2,3)
        self.assertEqual(len(cell), 6)
        cell.minus(7)
        self.assertEqual(len(cell), 5)
        cell.minus(3,2)
        self.assertEqual(len(cell), 5)
        cell.minus(4,8)
        self.assertEqual(len(cell), 3)

    def test_is_certain(self):
        self.assertEqual(Cell(IMPOSSIBLE_VALUES).is_certain(), False)
        self.assertEqual(Cell(ALL_POSSIBLE_VALUES).is_certain(), False)
        cell = Cell(ALL_POSSIBLE_VALUES)
        cell.minus(1,2,3)
        self.assertEqual(cell.is_certain(), False)
        cell.minus(4)
        self.assertEqual(cell.is_certain(), False)
        cell.minus(5, 6, 7)
        self.assertEqual(cell.is_certain(), False)
        cell.minus(8)
        self.assertEqual(cell.is_certain(), True)
        cell.minus(9)
        self.assertEqual(cell.is_certain(), False)

    def test_pos(self):
        cell = Cell()
        self.assertEqual(cell.get_pos(), (0, 0))
        cell.set_pos(1,2)
        self.assertEqual(cell.get_pos(), (1,2))

if __name__ == '__main__':
    unittest.main()