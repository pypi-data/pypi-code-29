import pprint

pp = pprint.PrettyPrinter(indent=4, width=30, depth=1)

color_set = {
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

break_line_double = "==========================================================\n"
break_line_single = "----------------------------------------------------------\n"

test_type_color_set = {
    "PASS": "GREEN",
    "WARN": "YELLOW",
    "ALERT": "RED",
    "SKIP": "CYAN"
}


def set_color(text: str, color: str) -> str:
    """
    set color
    :param text: (str)
    :param color: (str)
    :return: text: (str)
    """
    res = color_set[color]
    res += text
    res += color_set["END"]
    return res


class TestResult:
    """
    test result
    """

    def __init__(self, _test_type: str, _comment: str):
        self._test_type = _test_type.upper()
        self._comment = _comment

    def output(self, color_flg: bool = False) -> str:
        """
        output
        :param color_flg:
        :return: comment
        """
        if not color_flg:
            return "[" + self._test_type + "]" + self._comment + "\n"
        if self._test_type in test_type_color_set.keys():
            return set_color("[" + self._test_type + "]" + self._comment + "\n", test_type_color_set[self._test_type])
        else:
            return set_color("[" + self._test_type + "]" + self._comment + "\n", "WHITE")


class ResourceResult:
    """
    resource reviw result
    """

    def __init__(self, tf_obj_name: str, resource_type: str, resource_name: str):
        self._tf_obj_name = tf_obj_name
        self._resource_type = resource_type.upper()
        self._resource_name = resource_name
        self._test_results_list = []
        self._count_dict = {}

    def skip(self, _message: str) -> None:
        """
        add test skip log
        :param _message: (str)
        :return: None
        """
        _test_result = TestResult("SKIP", _message)
        self._test_results_list.append(_test_result)
        if "SKIP" not in self._count_dict.keys():
            self._count_dict["SKIP"] = 0
        self._count_dict["SKIP"] += 1

    def add_test_result(self, _result_type: str, _message: str) -> None:
        """
        add test result
        :param _result_type:
        :param _message:
        :return: None
        """
        _test_result = TestResult(_result_type, _message)
        self._test_results_list.append(_test_result)
        if _result_type not in self._count_dict.keys():
            self._count_dict[_result_type] = 0
        self._count_dict[_result_type] += 1

    def output(self, color_flg: bool = False) -> str:
        """
        result
        :param color_flg: (bool)
        :return: res: (str)
        """
        res = self.__resource_info(color_flg)
        for test_result in self._test_results_list:
            res += test_result.output(color_flg)
        if len(self._test_results_list) == 0:
            res += "[INFO]\tno test ...\n"
        return res

    @property
    def count_dict(self) -> dict:
        return self._count_dict

    def __resource_info(self, color_flg: bool = False) -> str:
        """
        resource info
        :return: res
        """
        res = "\n" + break_line_double
        _text = self._tf_obj_name.upper() + "." + self._resource_name.upper() + "\n"
        if color_flg:
            res += self._resource_type + " " + set_color(_text, "UNDERLINE")
        else:
            res += self._resource_type + " " + _text
        res += break_line_double
        return res
