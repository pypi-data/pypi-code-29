import sys
from subprocess import Popen, STDOUT, PIPE, check_output, CalledProcessError

def run_cmd(cmd, task="Task not described", verbosity=0):

    def format_called_process_error(error_obj):
        message = ""
        message += str("\ncmd: {}".format(error_obj.cmd))
        message += str("\nreturn code: {}".format(error_obj.returncode))
        if hasattr(error_obj, 'stdout'):
            if error_obj.stdout != None:
                message += str("\nstdout:\t{}".format(error_obj.stdout.decode('utf-8')))
        if hasattr(error_obj, 'stderr'):
            if error_obj.stderr != None:
                message += str("\nstderr:\t{}".format(error_obj.stderr.decode('utf-8')))
        return message

    try:
        # WARNING: constructing shell commands without input validation
        #          could lead to security issues!
        output = check_output(cmd, shell=True, stderr=STDOUT).decode('utf-8')

        if verbosity >= 2:
            print ("SHELL COMMAND SUCCEEDED: {} ".format(task))

        if verbosity == 3:
            output_lines = str(output).split(os.linesep)
            if len(output_lines) > 11:
                print("OUTPUT (last ten lines): ")
                last_lines = output_lines[-11:]
                for line in last_lines:
                    print(line)
            elif len(output_lines) == 0:
                pass
            else:
                print("OUTPUT: ")
                for line in output_lines:
                    print(line)

        if verbosity >= 4:
            print("OUTPUT:\n{}".format(output))

        sys.stdout.flush()
        return output

    except CalledProcessError as e:

        if e.returncode==127:

            message = str("A program was not found in shell command for: {}, returned code {}".format(task, e.returncode))

            if verbosity >= 1:
                message += format_called_process_error(e)
            sys.exit(message)

        elif e.returncode<=125:
            message = str("shell command failed for {}, returned code {}".format(task,e.returncode))

            if verbosity >= 1:
                message += format_called_process_error(e)
            sys.exit(message)

        else:
            # Things get hairy and unportable - different shells return
            # different values for coredumps, signals, etc.
            message = str("shell command for {} likely crashed, shell retruned code {}".format(task,e.returncode))
            if verbosity >= 1:
                message += format_called_process_error(e)
            sys.exit(message)

    except OSError as os_e:
        # unlikely, but still possible: the system failed to execute the shell
        # itself (out-of-memory, out-of-file-descriptors, and other extreme cases).
        message = str("a system-related error occured for shell command for {}: \n\terror code:{}\n\terror message:{}".format(task, os_e.errno, os_e.strerror))
        message += str("\n\tshell command: {}".format(cmd))
        if hasattr(os_e, 'filename'):
            message += str("\n\tfilename:{}".format(os_e.filename))
        if hasattr(os_e, 'filename2'):
            message += str("\n\tfilename2:{}".format(os_e.filename2))
        sys.exit(message)