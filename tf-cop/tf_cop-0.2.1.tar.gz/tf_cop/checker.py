import re


class Checker:
    def __init__(self, _resource):
        self._resource = _resource

    def key_value_check(self, resource_dict, review_dict) -> bool:
        """
        check if resource_dict key_value is correct using review_dict
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :return: flg: (bool)
        """
        if "value" not in review_dict:
            review_dict["value"] = ".*"
        _text_prefix = "\t" + review_dict["title"] + "\t: "
        if review_dict["key"] not in resource_dict:
            _text = _text_prefix + review_dict["key"] + " not use"
            self._resource.add_test_result(review_dict["type"], _text)
            return False
        if not re.match(review_dict["value"], str(resource_dict[review_dict["key"]])):
            _text = _text_prefix + "value not matched " + review_dict["value"] + \
                    " " + str(resource_dict[review_dict["key"]])
            self._resource.add_test_result(review_dict["type"], _text)
            return False
        self._resource.add_test_result("pass", _text_prefix + "passed")
        return True

    def review_cycle(self, resource_dict, review_dict) -> bool:
        """
        make recursion review cycle
        :param resource_dict: (dict)
        :param review_dict: (dict)
        :return: flg: (bool)
        """
        flg = self.key_value_check(resource_dict, review_dict)
        if not flg:
            return False
        if review_dict["mode"] == "nested":
            if type(review_dict["nest"]) is list:
                for tmp_review_dict in review_dict["nest"]:
                    flg = self.review_cycle(resource_dict[review_dict["key"]], tmp_review_dict)
            else:
                flg = self.review_cycle(resource_dict[review_dict["key"]], review_dict["nest"])
        elif review_dict["mode"] == "if":
            if type(review_dict["nest"]) is list:
                for tmp_review_dict in review_dict["nest"]:
                    flg = self.review_cycle(resource_dict, tmp_review_dict)
            else:
                flg = self.review_cycle(resource_dict, review_dict["nest"])
        return flg
