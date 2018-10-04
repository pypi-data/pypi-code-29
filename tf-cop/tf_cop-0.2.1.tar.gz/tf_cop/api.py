# coding: UTF-8
import hcl
import os
import yaml
import codecs
import glob
import re
from .checker import Checker
from .resource_result import ResourceResult

default_rbook_root_path = os.path.dirname(__file__) + '/_default_review_book/'


class TfCop:
    def __init__(self, tf_root_path: str, rbook_root_path: str = "", use_default: bool = True, debug: bool = False):
        """
        initialize
        :param tf_root_path: (str)
        :param rbook_root_path: (str)
        :param use_default: (bool)
        :param debug: (bool)
        """
        self._use_default = use_default
        self._resources_dict = {}
        self._tf_root_path = tf_root_path
        self._rbook_root_path = rbook_root_path
        self._debug = debug
        self._system_log = ""

    def tf_review(self) -> bool:
        """
        parse tf files and pass to review function
        :return: flg: (bool)
        """
        file_path_list = self.__get_regex_path(self._tf_root_path + "/**", '.*.tf\Z')
        try:
            for file_path in file_path_list:
                self.__debug_print("reading tf file\t:" + file_path)
                with codecs.open(file_path, 'r', 'utf-8') as fp:
                    tf_dict = hcl.load(fp)
                self.__tf_parse(tf_dict, "resource")
                self.__tf_parse(tf_dict, "data")
            return True
        except Exception as e:
            print(str(e))
            return False

    def output(self, color_flg: bool = False) -> str:
        """
        result for test
        :param color_flg: (bool)
        :return: res: (str)
        """
        res = ""
        for key in self._resources_dict.keys():
            res += self._resources_dict[key].output(color_flg)
        res += self.output_summary()
        return res

    def output_summary(self) -> str:
        """
        make output summary
        :return: str
        """
        summary_count_dict = {}
        for key in self._resources_dict.keys():
            count_dict = self._resources_dict[key].count_dict
            for key in count_dict.keys():
                if key not in summary_count_dict:
                    summary_count_dict[key] = 0
                summary_count_dict[key] += count_dict[key]
        res = "\n =======================\n"
        res += "| RESOURCE NUM\t: " + str(len(self._resources_dict)) + "\t|\n"
        for key in summary_count_dict.keys():
            res += "| " + key + " NUM\t: " + str(summary_count_dict[key]) + "\t|\n"
        res += " =======================\n"
        return res

    def __tf_parse(self, tf_dict: dict, resource_type: str) -> bool:
        """
        parse tf file (hcl)
        :param tf_dict: (dict)
        :param resource_type: (str)
        :return: (bool)
        """
        if resource_type not in tf_dict:
            return False
        tf_dict = tf_dict[resource_type]
        for tf_obj_name in tf_dict.keys():
            self.__debug_print("reviewing\t:" + resource_type.upper() + "\t" + tf_obj_name)
            if self._use_default:
                review_book_default_path = default_rbook_root_path + "/" + resource_type + "/" + \
                                           tf_obj_name.split("_")[1] + '.yaml'
                self.__review(review_book_default_path, tf_dict, tf_obj_name, resource_type)
            review_book_path = self._rbook_root_path + '/' + resource_type + "/" + \
                               tf_obj_name.split("_")[1] + '.yaml'
            self.__review(review_book_path, tf_dict, tf_obj_name, resource_type)
        return True

    def __review(self, review_book_path: str, tf_dict: dict, tf_obj_name: str, resource_type: str) -> bool:
        """
        review tf files using review_book
        :param review_book_path: (str)
        :param tf_dict: (dict)
        :param tf_obj_name: (str)
        :return: None
        """
        for resource_name in tf_dict[tf_obj_name].keys():
            self.__debug_print("reviewing\t:" + resource_name)
            _resource = self.__resource(tf_obj_name, resource_type, resource_name)
            if not os.path.exists(review_book_path):
                res = "review book does not exist : " + review_book_path
                self._system_log += res
                self._resources_dict[self.__resource_key(tf_obj_name, resource_type, resource_name)] = _resource
                return False
            with codecs.open(review_book_path, 'r', 'utf-8') as fp2:
                review_book = yaml.load(fp2)
            if not tf_obj_name in review_book:
                res = "no test : " + tf_obj_name
                _resource.skip(res)
            else:
                for review_dict in review_book[tf_obj_name]:
                    _checker = Checker(_resource)
                    _checker.review_cycle(tf_dict[tf_obj_name][resource_name], review_dict)
            self._resources_dict[self.__resource_key(tf_obj_name, resource_type, resource_name)] = _resource
        return True

    def __get_regex_path(self, path: str, regex: str) -> list:
        """
        get file path matching regex
        :param path: (str)
        :param regex: (str)
        :return: file_path_list: (dict)
        """
        all_file_path_list = glob.glob(path, recursive=True)
        file_path_list = []
        for file_path in all_file_path_list:
            if re.match(regex, file_path):
                file_path_list.append(file_path)
        return file_path_list

    def __resource(self, tf_obj_name: str, resource_type: str, resource_name: str) -> ResourceResult:
        """
        return ResourceResult
        :param tf_obj_name: (str)
        :param resource_type: (str)
        :param resource_name: (str)
        :return: ResourceResult: (ResourceResult)
        """
        _resource_key = self.__resource_key(tf_obj_name, resource_type, resource_name)
        if _resource_key in self._resources_dict.keys():
            return self._resources_dict[_resource_key]
        else:
            self._resources_dict[_resource_key] = ResourceResult(tf_obj_name, resource_type, resource_name)
            return self._resources_dict[_resource_key]

    def __debug_print(self, _text: str) -> None:
        """
        for debug print
        :param _text: (str)
        :return: None
        """
        if self._debug:
            print("[DEBUG]\t:" + _text)

    @staticmethod
    def __resource_key(tf_obj_name: str, resource_type: str, resource_name: str):
        """
        return resource key (only for self._resources_dict)
        :param tf_obj_name: (str)
        :param resource_type: (str)
        :param resource_name: (str)
        :return: (str)
        """
        return tf_obj_name + "_" + resource_type + "_" + resource_name
