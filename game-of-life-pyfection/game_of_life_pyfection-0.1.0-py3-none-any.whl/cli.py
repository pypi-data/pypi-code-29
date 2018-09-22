import argparse


class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Game Of Life: Pyfection.')
        parser.add_argument('width', metavar='-w', type=int, help='width of the board')
        parser.add_argument('height', metavar='-h', type=int, help='height of the board')
        parser.add_argument('infect_after', metavar='-i', type=int, help='infection starts after this round')
        parser.add_argument('max_generations', metavar='-m', type=int, help='Maximal amount of generations')
        parser.add_argument('seed', metavar='-s', type=int, nargs='+',
                            help='The initial seed for the board, if left empty, board will seed randomly')

        self.__parser = parser

    def parse(self):
        return self.__parser.parse_args()