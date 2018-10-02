# coding: UTF-8
import argparse
from .api import TfCop
import sys

parser = argparse.ArgumentParser(
    prog='tf_cop.py',
    usage='auto terraform review',
    description='https://pypi.org/project/tf-cop/',  # 引数のヘルプの前に表示
    epilog='end',  # 引数のヘルプの後で表示
    add_help=True,  # -h/–help オプションの追加
)

parser.add_argument('tf_root_path', help='terraform root path (ex. ./terraform)', type=str)
parser.add_argument('-r', '--review_book_root_path', help='review_book root path (ex. ./review_book)', type=str,
                    default="")


def cli():
    tf_cop = TfCop()
    args = parser.parse_args()
    tf_root_path = args.tf_root_path
    review_book_root_path = args.review_book_root_path
    try:
        tf_cop.tf_review(tf_root_path, review_book_root_path)
        output = tf_cop.output(color_flg=True)
        print(output["output_log"])
        print(output["output_summary_log"])
    except Exception as e:
        error_type = type(e).__name__
        sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
        sys.exit(1)

