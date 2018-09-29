import pprint

pp = pprint.PrettyPrinter(indent=4, width=30, depth=1)


class pycolor:
    """
    color set for output
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


class TfCopLogger:
    """
    logging
    """

    def __init__(self):
        self._output_log = ""
        self._program_error_log = ""
        self._system_log = ""
        self._pass_num = 0
        self._warn_num = 0
        self._alert_num = 0

    def skip(self, message):
        self._output_log += pycolor.YELLOW
        self._output_log += "[SKIP] " + message + "\n"
        self._output_log += pycolor.END

    def passed(self, resource_dict, review_dict, text):
        self._pass_num += 1
        self._output_log += pycolor.GREEN
        self._output_log += "[PASS] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pycolor.END

    def warning(self, resource_dict, review_dict, text):
        self._warn_num += 1
        self._output_log += pycolor.YELLOW
        self._output_log += "[WARN] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += pycolor.END

    def alert(self, resource_dict, review_dict, text):
        self._alert_num += 1
        self._output_log += pycolor.RED
        self._output_log += "[ALERT] " + review_dict['title'] + " : " + text + "\n"
        self._output_log += pp.pformat(resource_dict) + "\n"
        self._output_log += pycolor.END

    def add_resource_info(self, resource_name, obj_name):
        self._output_log += "\n==========================================================\n"
        self._output_log += "RESOURCE " + pycolor.UNDERLINE
        self._output_log += resource_name.upper() + "." + obj_name.upper() + "\n"
        self._output_log += pycolor.END
        self._output_log += "==========================================================\n"

    def output(self):
        if self._program_error_log:
            self._output_log += pycolor.CYAN
            self._output_log += self._program_error_log
        self._output_log += self.output_summary()
        return self._output_log

    def output_summary(self):
        res = "\n\n==========================================================\n"
        res += "PASS NUM\t: " + str(self._pass_num) + "\n"
        res += "WARN NUM\t: " + str(self._alert_num) + "\n"
        res += "ALERT NUM\t: " + str(self._alert_num) + "\n"
        res += "==========================================================\n"
        return res

    def add_program_error_log(self, error_message: str):
        self._program_error_log += "\n--------------------------------------------\n"
        self._program_error_log += pycolor.RED
        self._program_error_log += error_message
        self._program_error_log += pycolor.END
        self._program_error_log += "\n--------------------------------------------\n"

    def add_system_log(self, system_log: str):
        self._system_log += "\n--------------------------------------------\n"
        self._system_log += system_log
        self._system_log += "\n--------------------------------------------\n"

    @property
    def system_log(self):
        return self._system_log

    @property
    def program_error_log(self):
        return self._program_error_log
