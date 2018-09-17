import copy
import itertools
import time
from collections import deque

from .cell import Cell
from .exceptions import ComputeError, FormatError, GameError


class Solver():

    @staticmethod
    def validate(table):
        """Check whether or not a table is perfectly complete.
        """
        # test each column
        for i in range(9):
            test_cell = Cell()
            test_cell.minus(*table[i])
            if len(test_cell) > 0:
                return False
        # test each row
        for j in range(9):
            test_cell = Cell()
            test_cell.minus(*(table[i][j] for i in range(9)))
            if len(test_cell) > 0:
                return False
        # test each box
        for ki,kj in (itertools.product([0,3,6], repeat=2)):
            test_cell = Cell()
            for i, j in ((x, y) for x in range(ki, ki+3) for y in range(kj, kj+3)):
                test_cell.minus(table[i][j])
            if len(test_cell) > 0:
                return False
        return True
    
    @classmethod
    def solve(cls, table):
        """Algorithm goes here, pass a 2d list in and get a filled back.
        """

        start_time = time.clock()
        result = cls._scan(table, 0)
        result.info['cost'] = time.clock() - start_time
        if not result:
            raise GameError('Scan over the whole world, but couldn\'t find any result:(')
        return result

    @classmethod
    def _scan(cls, table, deep):
        svl = cls(table)
        if svl.is_end():
            if svl.is_confirm():
                svl.info['deep'] = deep
                return svl
            return None
        x, y = min(svl.uncertain, key=lambda p: svl.table[p[0]][p[1]])
        for k in svl.table[x][y].all_possibility():
            new_table = copy.deepcopy(svl.table)
            new_table[x][y] = k
            try:
                svl2 = cls._scan(new_table, deep+1)
                if not svl2:
                    continue
                return svl2
            except ComputeError:
                pass

    def __repr__(self):
        line = '+-----------+-----------+-----------+\n'
        s = ''
        for i in range(9):
            s += line if i%3 == 0 else ''
            s += '| {} ! {} ! {} | {} ! {} ! {} | {} ! {} ! {} |\n'.format(*self.table[i])
        s += line
        return s

    def draw(self):
        print(repr(self), end='')

    def is_confirm(self):
        if not self.completed:
            self.completed = Solver.validate(self.table)
        return self.completed

    def walk_row(self, x, y):
        return ((x,i) for i in range(9) if not i == y)

    def walk_column(self, x, y):
        return ((i,y) for i in range(9) if not i == x)

    def walk_box(self, x, y):
        kx, ky = (x-x%3, y-y%3) # get first cell's coordinate of box in which x,y is located 
        return ((i, j) for i in range(kx, kx+3) for j in range(ky, ky+3) if i != x and j != y)

    def related_cells(self, x, y):
        for i in itertools.chain(self.walk_row(x, y),
            self.walk_column(x, y), self.walk_box(x, y)):
            yield i

    def all_affected_cells(self, x, y):
        for (i, j) in self.related_cells(x, y):
            if isinstance(self.table[i][j], Cell):
                yield self.table[i][j]

    def compute_possible_values(self, x, y):
        if isinstance(self.table[x][y], int):
            return self.table[x][y]
        if self.table[x][y] is None:
            self.table[x][y] = Cell()
            self.table[x][y].set_pos(x, y)
        cell = self.table[x][y]
        
        for (i, j) in self.related_cells(x, y):
            if isinstance(self.table[i][j], int):
                cell.minus(self.table[i][j])

        if len(cell) == 0:
            raise ComputeError('Collapsed at ROW-{} COL-{}'.format(*map(lambda x: x+1, cell.get_pos())))
        return cell

    def push_affected_cells(self, x, y):
        for p in self.uncertain:
            self.dirty.append(p)
            
    def is_end(self):
        return True if len(self.uncertain) == 0 else False

    def __init__(self, table):
        self.table = table
        self.info = {'deep':-1}
        self.uncertain = set()
        self.completed = False

        for x in range(len(self.table)):
            for y in range(len(self.table[x])):
                self.table[x][y] = self.compute_possible_values(x, y)
                if isinstance(self.table[x][y], Cell):
                    self.uncertain.add((x,y))
        self.dirty = deque(self.uncertain)

        while len(self.dirty) > 0:
            x, y = pos = self.dirty.popleft()
            cell = self.table[x][y]
            if pos in self.uncertain:
                if len(cell) == 1:
                    value = cell.get_one()
                    self.uncertain.remove(pos)
                    self.push_affected_cells(x, y)
                    self.table[x][y] = value
                else:
                    self.compute_possible_values(x, y)


    def __getitem__(self, k):
        return self.info[k]
