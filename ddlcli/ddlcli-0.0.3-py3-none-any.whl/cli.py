import argparse
import sys
from ddlcli.job_util import submit_job

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--task_config',
        type=str,
        help='Path to the training task configuration')

    parser.add_argument(
        '--master_endpoint_override',
        type=str,
        help='override to master server for submitting job')

    FLAGS, _ = parser.parse_known_args()

    invalid_function_msg = "Please provide the name of function. Support functions are: \n" \
                           "\t submit: submit a training job"
    try:
        if len(sys.argv) < 2:
            assert (len(sys.argv) > 2), invalid_function_msg
        function_name = sys.argv[1]

        if function_name == "submit":
            assert (FLAGS.task_config is not None), "task_config is a required argument"
            submit_job(FLAGS.task_config, FLAGS.master_endpoint_override)
        else:
            assert False, invalid_function_msg
    except Exception as e:
        print(str(e))

