# coding: UTF-8
import hcl
import os
import yaml
import codecs
import glob
import re
from .tf_cop_logger import TfCopLogger
from .checker import Checker

default_review_book_root_path = os.path.dirname(__file__) + '/_default_review_book/'


class TfCop:
    def __init__(self, use_default: bool = True):
        self._logger = TfCopLogger()
        self._checker = Checker(self._logger)
        self._use_default = use_default

    def tf_review(self, tf_root_path: str, review_book_root_path: str):
        """
        parse tf files and pass to review function
        :param tf_root_path: (str)
        :param review_book_root_path: (str)
        :return: flg: (bool)
        """
        file_path_list = self.__get_regex_path(tf_root_path + "/**", '.*.tf\Z')
        flg = True
        try:
            for file_path in file_path_list:
                with codecs.open(file_path, 'r', 'utf-8') as fp:
                    tf_dict = hcl.load(fp)
                if not "resource" in tf_dict:
                    continue
                tf_dict = tf_dict["resource"]
                for resource_name in tf_dict.keys():
                    if self._use_default:
                        review_book_default_path = default_review_book_root_path + resource_name.split("_")[1] + '.yaml'
                        self.__review(review_book_default_path, tf_dict, resource_name)
                    review_book_path = review_book_root_path + '/' + resource_name.split("_")[1] + '.yaml'
                    self.__review(review_book_path, tf_dict, resource_name)
        except Exception as e:
            self._logger.add_program_error_log(str(e))
            flg = False
        return flg

    def output(self, color_flg: bool = False):
        return self._logger.output(color_flg)

    def __review(self, review_book_path: str, tf_dict: dict, resource_name: str):
        """
        review tf files using review_book
        :param review_book_path: (str)
        :param tf_dict: (dict)
        :param resource_name: (str)
        :return: flg, comment
        """
        if not os.path.exists(review_book_path):
            res = "review book does not exist : " + review_book_path
            self._logger.add_system_log(res)
            return False, res
        with codecs.open(review_book_path, 'r', 'utf-8') as fp2:
            review_book = yaml.load(fp2)
        for tf_dict_name in tf_dict[resource_name].keys():
            self._logger.add_resource_info(resource_name, tf_dict_name)
            if not resource_name in review_book:
                res = "no test : " + resource_name
                self._logger.skip(res)
                return False, res
            for review_dict in review_book[resource_name]:
                flg, res = self._checker.review_cycle(tf_dict[resource_name][tf_dict_name], review_dict)
        return True, "test pass"

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
