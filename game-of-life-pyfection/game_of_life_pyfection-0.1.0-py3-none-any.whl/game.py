from time import sleep
from typing import Optional, Iterable

from game_of_life_pyfection.board import Board
from game_of_life_pyfection.settings import Settings


class Game:
    def __init__(self, settings: Settings, seed: Optional[Iterable[int]] = None):
        board = Board(settings)
        board.populate_board()
        board.initialize_state(seed)

        self.board = board
        self.settings = settings
        self.current_generation = 0

    def is_infection_started(self):
        return self.current_generation >= self.settings.infect_after

    def play(self):
        """
        Main game loop
        """
        stage_switch_case = {
            False: self.board.calculate_next_generation_classic,
            True: self.board.calculate_next_generation_infected
        }

        while self.current_generation <= self.settings.max_generations:

            print(self.board.render_board_flat())

            stage_switch_case[self.is_infection_started()]()

            self.board.change_cell_states()

            sleep(self.settings.sleep_period)

            self.current_generation += 1