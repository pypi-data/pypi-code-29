import os

import yaml
import json
import argparse


class Result:
    def __init__(self, passed, path, msg=''):
        self.passed = passed
        self.path = path
        self.msg = msg

    def to_output(self):
        if self.passed:
            return f'{self.path} PASSED'
        return f'{self.path} FAILED\n{self.msg}'

    def to_xml(self):
        if self.passed:
            return f'<testcase name="{self.path}"></testcase>'
        return f'<testcase name="{self.path}"><failure>{self.msg}</failure></testcase>'


def xunit_report(results, file_type):
    nr_of_tests = len(results)
    nr_of_fails = len([result for result in results if not result.passed])
    test_cases = ''.join([result.to_xml() for result in results])
    return f'<?xml version="1.0" encoding="utf-8"?><testsuite errors="0" failures="{nr_of_fails}" name="{file_type}" tests="{nr_of_tests}">{test_cases}</testsuite>'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xunit', help='Generate xunit result file', action='store_true')
    parser.add_argument('--xunit-output-file', help='Xunit result file name', default='testreport.xml')
    parser.add_argument('files', nargs='+')
    return parser.parse_args()


def yaml_validation_result(file):
    try:
        yaml.load(file)
    except yaml.YAMLError as e:
        return Result(passed=False, path=file.name, msg=str(e))
    return Result(passed=True, path=file.name)


def json_validation_result(file):
    try:
        json.load(file)
    except json.decoder.JSONDecodeError as e:
        return Result(passed=False, path=file.name, msg=str(e))
    return Result(passed=True, path=file.name)


def report_valid_files(file_type):
    args = parse_args()
    results = []
    for file_name in args.files:
        with open(file_name, 'r') as config_file:
            if(file_type) == 'yaml':
                result = yaml_validation_result(config_file)
            elif(file_type) == 'json':
                result = json_validation_result(config_file)
            else:
                assert False
            results.append(result)
        print(result.to_output())

        if args.xunit:
            xunit_folder = os.path.dirname(args.xunit_output_file)
            if xunit_folder:
                os.makedirs(xunit_folder, exist_ok=True)
            with open(args.xunit_output_file, 'w') as xunit_file:
                xunit_file.write(xunit_report(results, file_type))


def report_valid_json_files():
    report_valid_files('json')


def report_valid_yaml_files():
    report_valid_files('yaml')
