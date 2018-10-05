import sys
import grewritingpool.helper

def main(args):
    if len(args) == 1:
        if args[0] in ("-h", "--help"):
            print("grewriting [all|issue|argument]")
            sys.exit()
        else:
            grewritingpool.helper._print_random_article(args[0])
    elif len(args) == 0:
        grewritingpool.helper._print_random_article()
    else:
        print("grewritingpool.py [all|issue|argument]")
        sys.exit(1)