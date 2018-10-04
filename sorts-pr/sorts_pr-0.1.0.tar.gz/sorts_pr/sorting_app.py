from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument('list')
parser.add_argument('--bub', dest='algorithm', action='store_const', const=bubble_sort, default=bubble_sort)
parser.add_argument('--sel', dest='algorithm', action='store_const', const=selection_sort, default=bubble_sort)
parser.add_argument('--ins', dest='algorithm', action='store_const', const=insertion_sort, default=bubble_sort)
parser.add_argument('--qui', dest='algorithm', action='store_const', const=quick_sort, default=bubble_sort)

if __name__ == '__main__':
    args = parser.parse_args()
    alist = ast.literal_eval(args.list)
    fn = args.algorithm
    fn(alist)
    print(alist)