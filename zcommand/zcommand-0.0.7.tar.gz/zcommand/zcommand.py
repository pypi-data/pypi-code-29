#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys

class Command(object):
    def __init__(self, help_cmd=None):
        self.function = {}
        self.function_name = {}
        self.status = {}
        self.status_name = {}
        self.status_value = {}
        self.help_use_len = 0
        self.help_slot = 4
        self.run_hook = []
        self.run_hook_exclude_cmd = []
        self.status = dict()
        if isinstance(help_cmd, str):
            self.add(help_cmd, self.help_func, 0, 1, help_cmd + " [cmd]",
                    "后跟[cmd]查看详细信息", map_name="help")
        elif isinstance(help_cmd, (tuple,list)):
            self.add(help_cmd, self.help_func, 0, 1, " ".join(help_cmd) + " [cmd]",
                    "后跟[cmd]查看详细信息", map_name="help")
        else:
            pass

    def add(self, name, func, argc_min, argc_max, help_use,
            help_explain, help_detail=None, accept_status=False, map_name=None):
        '''
            name: 识别用户输入，是一个string表示只有一种类型的输入，tuple,list表示有多种类型的输入
            func: 函数
            argc_min: 函数需要最少参数个数
            argc_max: 函数需要最大参数个数
            help_use: 函数使用用法
            help_explain: 函数解释
            help_detail: 函数详细解释，可选
            accept_status: 接受状态信息，可选，默认不接受
            map_name: 存在map里的名字，如果没有的话，根据name得出
                    如果name是string，则map_name=name如果是tuple,list，则取第一个，即map_name=name[0]
        '''
        map_name = self.set_name_name(self.function_name, name, map_name)
        if map_name is False:
            return False
        self.function[map_name] = {
                    "func": func,
                    "argc_min": argc_min,
                    "argc_max": argc_max,
                    "status": accept_status,
                    "help": {
                        'use': help_use,
                        'explain': help_explain,
                        'detail': help_detail
                        }
                }
        self.help_use_len = max((len(help_use), self.help_use_len))
        return True

    def delete(self, name):
        if self.exist_func(name):
            del self.function[name]
            for _name,_map_name in self.function_name.items():
                if map_name == _map_name:
                    del self.status_name[_name]
            return True
        return False

    def set_name_name(self, name_dict, name, map_name):
        if isinstance(name, (tuple, list)):
            if len(name) == 0:
                return False
            if map_name is None:
                map_name = name[0]
            for next_name in name:
                name_dict[next_name] = map_name
        elif isinstance(name, str):
            if map_name is None:
                map_name = name
            name_dict[name] = map_name
        else:
            return False
        return map_name

    def add_status(self, name, default_value, help_use, help_explain, help_detail=None, map_name=None):
        '''
            name: 识别用户输入，是一个string表示只有一种类型的输入，tuple,list表示有多种类型的输入
            default_value: 默认值
            value_type: 值根据默认值判断，支持bool, list, string
                bool: 对应0个参数
                string: 对应1个参数
                list: 对应多个参数，中间用逗号分隔
                因为bool类型不需要要指定值，所以当命令行有改参数时，该状态变为not default_value
            help_use: 函数使用用法
            help_explain: 函数解释
            help_detail: 函数详细解释，可选
            注意: 如果status_name与func_name同名的话，用户输入时会默认为func_name
        '''
        if isinstance(default_value, bool):
            value_type = bool
        elif isinstance(default_value, tuple):
            value_type = list
            default_value = list(default_value)
        elif isinstance(default_value, list):
            value_type = list
        elif isinstance(default_value, str):
            value_type = str
        else:
            print(default_value)
            print("add_status不支持其他类型")
            return False
        map_name = self.set_name_name(self.status_name, name, map_name)
        if map_name is False:
            return False
        self.status[map_name] = {
                    "default_value": self.copy_value(default_value),
                    "value_type": value_type,
                    "help": {
                        'use': help_use,
                        'explain': help_explain,
                        'detail': help_detail
                        }
                }
        self.status_value[map_name] = default_value
        self.help_use_len = max((len(help_use), self.help_use_len))
        return True

    def delete_status(self, map_name):
        if self.exist_status(map_name):
            del self.status[map_name]
            del self.status_value[map_name]
            for _name,_map_name in self.status_name.items():
                if map_name == _map_name:
                    del self.status_name[_name]
            return True
        return False

    def exist_func(self, name):
        return bool(self.function_name.get(name))

    def exist_status(self, name):
        return bool(self.status_name.get(name))

    def exist(self, name):
        return self.exist_func(name) or self.exist_status(name)

    def get_function(self, name):
        name = self.function_name[name]
        return self.function[name]

    def get_status(self, name):
        name = self.status_name[name]
        return self.status[name]

    def get_status_value(self, name):
        name = self.status_name[name]
        return self.status_value[name]

    def set_status_value(self, name, value):
        name = self.status_name[name]
        self.status_value[name] = value

    def set_help_slot(self, new_help_slot):
        if new_help_slot > 0:
            self.help_slot = new_help_slot
            return True
        return False

    def get_help(self, name, detail=False, status=False):
        if status:
            if not self.exist_status(name):
                return ""
            help_ = self.get_status(name)['help']
            ret = help_['use']
        else:
            if self.exist_func(name):
                help_ = self.get_function(name)['help']
                ret = help_['use']
            else:
                if not self.exist_status(name):
                    return ""
                help_ = self.get_status(name)['help']
                ret = help_['use']
        ret = ret.ljust(self.help_use_len + self.help_slot)
        ret = ret + help_['explain'] + "\n"
        if detail and help_['detail']:
            ret = ret + self.help_slot * " " + "详细: "
            if isinstance(help_['detail'], str):
                ret = ret + help_['detail']
            elif callable(help_['detail']):
                ret = ret + help_['detail']()
        return ret.strip()

    def __unique_value(self, _dict):
        ret_name = []
        ret_value = []
        for name, value in _dict.items():
            if value not in ret_value:
                ret_name.append(name)
                ret_value.append(value)
        ret_name.sort()
        return ret_name

    def help(self, name=None):
        if name is not None:
            return self.get_help(name, True)
        ret = ["执行命令:"]
        function_cmd = self.__unique_value(self.function_name)
        for cmd in function_cmd:
            ret.append(self.get_help(cmd))
        ret.append("\n状态命令:")
        status_cmd = self.__unique_value(self.status_name)
        for cmd in status_cmd:
            ret.append(self.get_help(cmd, status=True))
        ret.append("\n注意: 状态命令必须在执行命令前使用")
        return "\n".join(ret)

    def help_func(self, name=None):
        print(self.help(name))
    def copy_value(self, value):
        if isinstance(value, (str, int, float, tuple, bool)):
            return value
        elif isinstance(value, list):
            return value[:]
        else:
            print("类型不识别")
            return None

    def run(self, name=None, argv=tuple()):
        if name is None:
            print(self.help())
            return True
        if self.exist_func(name):
            cmd = self.get_function(name)
            if cmd['argc_min'] <= len(argv) <= cmd['argc_max']:
                if name not in self.run_hook_exclude_cmd:
                    while len(self.run_hook) != 0:
                        now_run = self.run_hook.pop()
                        now_run()
                if len(argv) == 0:
                    if cmd['status']:
                        return cmd['func'](**self.status_value)
                    else:
                        return cmd['func']()
                else:
                    if cmd['status']:
                        return cmd['func'](*argv, **self.status_value)
                    else:
                        return cmd['func'](*argv)
            if cmd['argc_max'] < len(argv):
                argc_max = cmd['argc_max']
                if cmd['status']:
                    ret = cmd['func'](*argv[:argc_max], **self.status_value)
                else:
                    ret = cmd['func'](*argv[:argc_max])
                if ret:
                    return self.run(argv[argc_max], argv[argc_max+1:])
                return False
            else:
                print(name + "参数个数错误")
                return False
        elif self.exist_status(name):
            save_status_value = self.copy_value(self.get_status_value(name))
            if self.get_status(name)["value_type"] == bool:
                self.set_status_value(name, not self.get_status_value(name))
            elif self.get_status(name)["value_type"] == str:
                if len(argv) > 0:
                    self.set_status_value(name, argv[0])
                    argv = argv[1:]
                else:
                    print(name + "参数个数错误")
                    return False
            elif self.get_status(name)["value_type"] == list:
                if len(argv) > 0:
                    self.set_status_value(name, argv[0].split(","))
                    argv = argv[1:]
                else:
                    print(name + "参数个数错误")
                    return False
            else:
                print("run 识别类型错误")
                return False
            if len(argv) == 0:
                ret = self.run()
            else:
                ret = self.run(argv[0], argv[1:])
            self.copy_value = save_status_value
            return ret
        else:
            print("错误命令")
            return False

    def add_run_hook(self, func):
        self.run_hook.append(func)
        return True

    def add_run_hook_exclude_cmd(self, cmd):
        self.run_hook_exclude_cmd.append(cmd)
        return True


class RunCommand(object):
    def __init__(self, help_cmd=None, test=False):
        self.command = Command(help_cmd)
        self.cwd = os.getcwd()
        if test:
            self.__run_test()

    def run(self, args):
        if len(args) == 0:
            self.command.run()
        else:
            self.command.run(args[0], args[1:])
        os.chdir(self.cwd)

    def add(self, *info, **info_dict):
        if len(info) < 4:
            return False
        two_arg = info[1]
        if callable(two_arg):
            return self.command.add(*info, **info_dict)
        else:
            return self.command.add_status(*info, **info_dict)

    def __run_test(self):
        self.add("test", self.__test, 0, 2,
                    "test [arg1] [arg2]", "测试函数", "测试函数详细信息", True)
        self.add("true", False, "true", "设置为true， 默认为false")

    def __test(self, arg1=None, arg2=None, **status):
        if arg1 is None:
            print("您没有输入参数1")
        else:
            print("您输入的参数1是: " + arg1)
        if arg2 is None:
            print("您没有输入参数2")
        else:
            print("您输入的参数2是: " + arg2)
        if status["true"]:
            print("当前状态是true")
        else:
            print("当前状态是false")


if __name__ == "__main__":
    rc = RunCommand(True, True)
    rc.run(sys.argv[1:])
