import logging
import random
from collections import defaultdict
from typing import Optional, Iterable, List, Union

from game_of_life_pyfection.cell import Cell
from game_of_life_pyfection.constants import *
from game_of_life_pyfection.settings import Settings

logger = logging.getLogger(__name__)


class Board:
    def __init__(self, settings: Settings):
        logger.debug(f'Initializing board with settings:\n{settings}')

        self.settings = settings
        self.cells: List[Cell] = []
        self.current_generation: int = 0

    def populate_board(self):
        """
        Populates the board with new dead cells
        """
        logger.debug('Populating board')

        for y in range(self.settings.height):
            for x in range(self.settings.width):
                self.cells.append(Cell(x, y))

    def initialize_state(self, seed: Optional[Iterable[int]] = None):
        """
        Initializes the state of each cell on the board using a given seed.
        If seed is not provided, a random state will be initialized for every cell.
        :param seed: List of ints representing either a cell is dead or alive
        """
        if seed:
            logger.debug('Initializing board state from seed')
            for i, s in enumerate(seed):
                self.cells[i].state = bool(s)
        else:
            self.initialize_state_random()

    def initialize_state_random(self):
        """
        Initializes a random state for each cell
        """
        logger.debug('Initializing random board state')
        for cell in self.cells:
            cell.state = bool(random.getrandbits(1))

    def get_cell(self, x: int, y: int) -> Union[Cell, None]:
        # Make sure cell is in board bounds
        if 0 > x or x >= self.settings.width or 0 > y or y >= self.settings.height:
            return None
        else:
            return self.cells[y * self.settings.width + x]

    def get_all_neighbors(self, cell: Cell) -> List[Cell]:
        neighbors = [self.get_cell(*cell.neighbor_coordinates(*neighbor)) for neighbor in NEIGHBORS.values()]
        return neighbors

    def get_horizontal_neighbors(self, cell: Cell) -> List[Cell]:
        neighbors = [
            self.get_cell(*cell.neighbor_coordinates(*NEIGHBORS[LEFT])),
            self.get_cell(*cell.neighbor_coordinates(*NEIGHBORS[RIGHT]))
        ]
        return neighbors

    def get_vertical_neighbors(self, cell: Cell) -> List[Cell]:
        neighbors = [
            self.get_cell(*cell.neighbor_coordinates(*NEIGHBORS[TOP])),
            self.get_cell(*cell.neighbor_coordinates(*NEIGHBORS[BOTTOM]))
        ]
        return neighbors

    def calculate_next_generation_classic(self):
        """
        Calculates the states of each cell according to rules classic game of life
        """
        logger.debug('Calculating next generation')

        # Iterate cells and check if their state needs to be changed before the next generation
        for cell in self.cells:

            neighbors = self.get_all_neighbors(cell)

            # If cell is alive, check if cell survives this generation
            if cell.state and not (2 <= self.live_neighbors_amount(neighbors) <= 3):
                cell.change = True

            # Check if cell is dead, check if cell reproduces this generation
            elif not cell.state and self.live_neighbors_amount(neighbors) == 3:
                cell.change = True

    def calculate_next_generation_infected(self):
        """
        Calculates the states of each cell according to rules of infection period
        """
        logger.debug('Calculating next generation (infection period)')

        # Iterate cells and check if their state needs to be changed before the next generation
        for cell in self.cells:
            neighbors = self.get_all_neighbors(cell)

            # If cell is alive
            if cell.state:
                vertical_neighbors = self.get_vertical_neighbors(cell)
                horizontal_neighbors = self.get_horizontal_neighbors(cell)

                if len(vertical_neighbors) == 2 and self.all_neighbors_alive(vertical_neighbors):
                    cell.change = True

                elif len(horizontal_neighbors) == 2 and self.all_neighbors_alive(horizontal_neighbors):
                    cell.change = True

            # If cell is dead
            elif not cell.state and self.live_neighbors_amount(neighbors) == 1:
                cell.change = True

    @staticmethod
    def live_neighbors_amount(neighbors: List[Cell]) -> int:
        """
        Counts the amount of living cells in a list of cells. ignores nones.
        :param neighbors: List of cells
        :return: The amount of living cells in neighbors list
        """
        return len([c for c in neighbors if c is not None and c.state])

    @staticmethod
    def all_neighbors_alive(neighbors: List[Cell]) -> bool:
        """
        Checks if all cells in neighbors are living
        :param neighbors: List of cells
        :return: Returns True if all cells are alive, else returns False
        """
        return all((c.state if c is not None else c for c in neighbors))

    def change_cell_states(self):
        """
        Calls change_state on all available cells
        """
        logger.debug('Trying to change state on all cells')

        for cell in self.cells:
            cell.change_state()

    def render_board_2d(self) -> str:

        rendered_cells = defaultdict(list)
        for cell in self.cells:
            rendered_cells[cell.y].append(str(cell))

        rendered_board = []
        for k in sorted(rendered_cells.keys()):
            row = rendered_cells[k]
            rendered_board.append(' '.join(row))

        return '\n'.join(rendered_board)

    def render_board_flat(self) -> str:
        rendered_board = [str(cell) for cell in self.cells]
        return ' '.join(rendered_board)
