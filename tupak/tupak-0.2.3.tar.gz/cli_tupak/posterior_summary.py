import argparse


def setup_command_line_args():
    parser = argparse.ArgumentParser(
        description="Print a summary of the posteriors")
    parser.add_argument("-r", "--results", nargs='+',
                        help="List of results files to use.")
    parser.add_argument("-p", "--parameters", nargs='+', default=None,
                        help="List of parameters.")
    args, _ = parser.parse_known_args()

    return args


def main():
    args = setup_command_line_args()
    import tupak
    results = [tupak.core.result.read_in_result(filename=r)
               for r in args.results]
    for result in results:
        for key in result.parameter_labels:
            print("{} = {}".format(
                key, result.get_one_dimensional_median_and_error_bar(key)))
