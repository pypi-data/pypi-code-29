# coding: UTF-8
import hcl
import os
import yaml
import codecs
import glob
import re
from .tf_cop_logger import TfCopLogger
from .checker import Checker


class TfCop:
    def __init__(self):
        self._logger = TfCopLogger()
        self._checker = Checker(self._logger)

    def tf_review(self, tf_root_path: str = "./terraform", review_book_root_path: str = "./review_book"):
        file_path_list = self.__get_regex_path(tf_root_path + "/**", '.*.tf\Z')
        flg = True
        try:
            for file_path in file_path_list:

                with codecs.open(file_path, 'r', 'utf-8') as fp:
                    obj = hcl.load(fp)
                if not "resource" in obj:
                    continue
                obj = obj["resource"]

                for resource_name in obj.keys():
                    review_book_path = review_book_root_path + '/' + resource_name.split("_")[1] + '.yaml'
                    if not os.path.exists(review_book_path):
                        self._logger.add_system_log("review book does not exist : " + review_book_path)
                        continue
                    with codecs.open(review_book_path, 'r', 'utf-8') as fp2:
                        review_book = yaml.load(fp2)
                    for obj_name in obj[resource_name].keys():
                        self._logger.add_resource_info(resource_name, obj_name)
                        if not resource_name in review_book:
                            self._logger.skip("no test")
                            continue
                        for review_dict in review_book[resource_name]:
                            flg, res = self._checker.review_cycle(obj[resource_name][obj_name], review_dict)
        except Exception as e:
            self._logger.add_program_error_log(str(e))
            flg = False
        return flg

    def result(self):
        return self._logger.output()

    def result_summary(self):
        return self._logger.output_summary()

    def program_error_log(self):
        return self._logger.program_error_log

    def __get_regex_path(self, path: str, regex: str) -> list:
        all_file_path_list = glob.glob(path, recursive=True)
        file_path_list = []
        for file_path in all_file_path_list:
            if re.match(regex, file_path):
                file_path_list.append(file_path)
        return file_path_list



