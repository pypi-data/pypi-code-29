import re


class Checker:
    def __init__(self, logger):
        self._logger = logger

    def key_value_check(self, resource_dict, review_dict):
        if "value" not in review_dict:
            review_dict["value"] = ".*"
        if review_dict["key"] not in resource_dict:
            _text = review_dict["key"] + " not use"
            self._logger.alert(resource_dict, review_dict, _text)
            return False, _text
        if not re.match(review_dict["value"], str(resource_dict[review_dict["key"]])):
            _text = "value not matched " + review_dict["value"] + " " + str(resource_dict[review_dict["key"]])
            self._logger.alert(resource_dict, review_dict, _text)
            return False, _text
        self._logger.passed(resource_dict, review_dict, "passed")
        return True, ""

    def review_cycle(self, resource_dict, review_dict):
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
