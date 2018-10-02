import re


class Checker:
    def __init__(self, logger):
        self._logger = logger

    def key_value_check(self, resource_dict, review_dict):
        """
        check if resource_dict key_value is correct using review_dict
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :return: flg, message
        """
        if "value" not in review_dict:
            review_dict["value"] = ".*"
        if review_dict["key"] not in resource_dict:
            _text = review_dict["key"] + " not use"
            if "warn" in review_dict and review_dict["warn"]:
                self._logger.warn(resource_dict, review_dict, _text)
            else:
                self._logger.alert(resource_dict, review_dict, _text)
            return False, _text
        if not re.match(review_dict["value"], str(resource_dict[review_dict["key"]])):
            _text = "value not matched " + review_dict["value"] + " " + str(resource_dict[review_dict["key"]])
            if "warn" in review_dict and review_dict["warn"]:
                self._logger.warn(resource_dict, review_dict, _text)
            else:
                self._logger.alert(resource_dict, review_dict, _text)
            return False, _text
        self._logger.passed(resource_dict, review_dict, "passed")
        return True, ""

    def review_cycle(self, resource_dict, review_dict):
        """
        make recursion review cycle
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :return: flg, message
        """
        flg, res = self.key_value_check(resource_dict, review_dict)
        if not flg:
            return False, res
        if review_dict["mode"] == "nested":
            if type(review_dict["nest"]) is list:
                for tmp_review_dict in review_dict["nest"]:
                    flg, res = self.review_cycle(resource_dict[review_dict["key"]], tmp_review_dict)
                return flg, res
            else:
                flg, res = self.review_cycle(resource_dict[review_dict["key"]], review_dict["nest"])
                return flg, res
        elif review_dict["mode"] == "if":
            if type(review_dict["nest"]) is list:
                for tmp_review_dict in review_dict["nest"]:
                    flg, res = self.review_cycle(resource_dict, tmp_review_dict)
                return flg, res
            else:
                flg, res = self.review_cycle(resource_dict, review_dict["nest"])
                return flg, res
        return flg, res
