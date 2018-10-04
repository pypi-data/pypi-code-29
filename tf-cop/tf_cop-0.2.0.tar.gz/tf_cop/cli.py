# coding: UTF-8
import argparse
from .api import TfCop
import sys

parser = argparse.ArgumentParser(
    prog='tf_cop.py',
    usage='auto terraform review',
    description='https://pypi.org/project/tf-cop/',
    epilog='end',
    add_help=True,
)

parser.add_argument('tf_root_path', help='terraform root path (ex. ./terraform)', type=str)
parser.add_argument('-r', '--review_book_root_path', help='review_book root path (ex. ./review_book)', type=str,
                    default="")


def cli():
    args = parser.parse_args()
    tf_root_path = args.tf_root_path
    review_book_root_path = args.review_book_root_path
    tf_cop = TfCop(tf_root_path, review_book_root_path)
    try:
        print_info("tf_root_path\t: " + tf_root_path)
        print_info("rbook_root_path\t: " + review_book_root_path)
        tf_cop.tf_review()
        output = tf_cop.output(color_flg=True)
        print(output)
    except Exception as e:
        error_type = type(e).__name__
        sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
        sys.exit(1)


def print_info(_text):
    _text = "[INFO] " + _text
    print(_text)
