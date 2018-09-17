import argparse
import os
import sys

from . import Solver, load_from_file, load_from_input


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
        help='The file in which a string format of a Soduku problem is contained')
    details = parser.add_argument_group()
    details.add_argument('-t', '--time', action='store_true', help='Print cost time')
    details.add_argument('-d', '--deep', action='store_true', help='Print guess times')
    # parser.add_argument('-v', '--verbose', action='store_true', help='Give some detail infomation')
    args = parser.parse_args()
    if args.file:
        problem = load_from_file(args.file)
    else:
        print('Please type the problem in:')
        problem = load_from_input()

    process = Solver.solve(problem)
    process.draw()
    if args.time:
        print('Cost: {:.3f}s'.format(process['cost']))
    if args.deep:
        print('Deep: {}'.format(process['deep']))
        
    return 0

if __name__ == '__main__':
    main()
