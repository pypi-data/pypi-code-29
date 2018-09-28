from abc import ABC, abstractmethod


class AI(ABC):

    @abstractmethod
    def turn(self, *args, **kwargs):
        raise NotImplementedError


class CoreAI(AI):

    @abstractmethod
    def turn(self, board: [list], symbol: str) -> (int, int):
        """
        :param board: Contains the current state of the game
        :param symbol: Contains your symbol on the board - either X if you are the first player or O if you are the 2nd.
        :return: pos_x, pos_y where your AI wants to place a stone
        """
        for i in range(8):
            for j in range(8):
                if self.free(i, j, board):
                    return i, j

    @staticmethod
    def free(x: int, y: int, board: [list]) -> bool:
        if board[x][y] == '#':
            return True
        return False
