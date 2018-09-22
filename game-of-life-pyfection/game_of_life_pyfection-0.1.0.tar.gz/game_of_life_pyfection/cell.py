from typing import Tuple


class Cell:

    def __init__(self, x: int, y: int, alive=False):
        self.x: int = x
        self.y: int = y

        self.state: bool = alive
        self.change: bool = False

    def neighbor_coordinates(self, x: int, y: int) -> Tuple[int, int]:
        return self.x+x, self.y+y

    def change_state(self):
        if self.change:
            self.state = not self.state
        self.change = False

    def __str__(self):
        return '1' if self.state else '0'
