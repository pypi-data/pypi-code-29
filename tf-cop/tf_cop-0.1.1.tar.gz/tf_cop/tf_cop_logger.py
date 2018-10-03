import pprint

pp = pprint.PrettyPrinter(indent=4, width=30, depth=1)


class TfCopLogger:
    """
    logging
    """

    def __init__(self):
        self._color_set = {
            "BLACK": '\033[30m',
            "RED": '\033[31m',
            "GREEN": '\033[32m',
            "YELLOW": '\033[33m',
            "BLUE": '\033[34m',
            "PURPLE": '\033[35m',
            "CYAN": '\033[36m',
            "WHITE": '\033[37m',
            "END": '\033[0m',
            "BOLD": '\038[1m',
            "UNDERLINE": '\033[4m',
            "INVISIBLE": '\033[08m',
            "REVERCE": '\033[07m'
        }
        self._output = {
            "output_log": "",
            "output_summary_log": "",
            "program_error_log": "",
            "system_log": "",
            "count": {
                "resource": 0,
                "skip": 0,
                "pass": 0,
                "warn": 0,
                "alert": 0
            }
        }
        self._break_line_double = "==========================================================\n"
        self._break_line_single = "----------------------------------------------------------\n"

    def skip(self, message: str):
        """
        add test skip log
        :param message: (str)
        :return: None
        """
        self._output["count"]["resource"] += 1
        self._output["count"]["skip"] += 1
        self._output["output_log"] += self.__set_color("[SKIP] " + message + "\n", "YELLOW")

    def passed(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test pass log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._output["count"]["pass"] += 1
        self._output["output_log"] += self.__set_color("[PASS] " + review_dict['title'] + " : " + text + "\n", "GREEN")

    def warn(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test warn log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._output["count"]["warn"] += 1
        self._output["output_log"] += self.__set_color(
            "[WARN] " + review_dict['title'] + " : " + text + "\n" + pp.pformat(resource_dict) + "\n",
            "YELLOW"
        )

    def alert(self, resource_dict: dict, review_dict: dict, text: str):
        """
        add test alert log
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :param text: (str)
        :return: None
        """
        self._output["count"]["alert"] += 1
        self._output["output_log"] += self.__set_color(
            "[ALERT] " + review_dict['title'] + " : " + text + "\n" + pp.pformat(resource_dict) + "\n",
            "RED"
        )

    def add_resource_info(self, resource_name: str, obj_name: str):
        """
        add resource info log
        :param resource_name: (str)
        :param obj_name: (str)
        :return: None
        """
        self._output["count"]["resource"] += 1
        self._output["output_log"] += "\n" + self._break_line_double
        self._output["output_log"] += "RESOURCE " + self.__set_color(
            resource_name.upper() + "." + obj_name.upper() + "\n",
            "UNDERLINE"
        )
        self._output["output_log"] += self._break_line_double

    def add_program_error_log(self, error_message: str):
        """
        add program error log
        :param error_message: (str)
        :return: None
        """
        self._output["program_error_log"] += "\n" + self._break_line_single
        self._output["program_error_log"] += self.__set_color(error_message, "RED")
        self._output["program_error_log"] += "\n" + self._break_line_single

    def add_system_log(self, system_log: str):
        """
        add system log
        :param system_log: (str)
        :return: None
        """
        self._output["system_log"] += "\n" + self._break_line_single
        self._output["system_log"] += system_log
        self._output["system_log"] += "\n" + self._break_line_single

    def output(self, color_flg: bool = False):
        """
        system log
        :param color_flg: (bool)
        :return: system_log: (str)
        """
        self.__set_summary_log()
        if color_flg:
            return self._output
        else:
            return self.__remove_color(self._output)

    def __set_color(self, text: str, color: str):
        """
        set color
        :param text: (str)
        :param color: (str)
        :return: text: (str)
        """
        res = self._color_set[color]
        res += text
        res += self._color_set["END"]
        return res

    def __remove_color(self, dict: dict):
        """
        remove color str
        :param dict: (dict)
        :return: dict: (dict)
        """
        for key in dict.keys():
            if type(dict[key]) == "dict":
                dict[key] = self.__remove_color(dict[key])
            elif type(dict[key]) == "str":
                for color in self._color_set.keys():
                    dict[key] = dict[key].replace(self._color_set[color], "")
        return dict

    def __set_summary_log(self):
        """
        make output summary
        :return: None
        """
        self._output["output_summary_log"] = "\n =======================\n"
        self._output["output_summary_log"] += "| RESOURCE NUM\t: " + str(self._output["count"]["resource"]) + "\t|\n"
        self._output["output_summary_log"] += "| SKIP NUM\t: " + str(self._output["count"]["skip"]) + "\t|\n"
        self._output["output_summary_log"] += "| PASS NUM\t: " + str(self._output["count"]["pass"]) + "\t|\n"
        self._output["output_summary_log"] += "| WARN NUM\t: " + str(self._output["count"]["warn"]) + "\t|\n"
        self._output["output_summary_log"] += "| ALERT NUM\t: " + str(self._output["count"]["alert"]) + "\t|\n"
        self._output["output_summary_log"] += " =======================\n"
