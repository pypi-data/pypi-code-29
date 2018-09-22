#!/usr/bin/ python3

# Copyright (C) 2018  leviathan0992 <leviathan0992@gmail.com>

import fileinput
import sys
import os
import paramiko
import getpass
from plumbum import cli, colors
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

default_path = "/usr/local/pyessh.conf"
version = "v0.1.3"
project = "Pyessh"
description = "A tool for easy to execute commands at multiserver"
session = PromptSession()


class SSHManager(object):
    def __init__(self):
        self.__path = default_path
        self.__ip = []
        self.__port = 22
        self.__username = ""
        self.__password = ""
        self.__clients = {}

    def _do_parse(self, path):
        self.__path = path
        if not os.path.isabs(self.__path):
            self.__path = os.getcwd() + "/" + self.__path

        if not os.path.exists(self.__path):
            print("The configuration is not exists")

        # Parsing from configuration
        with open(self.__path) as config:
            for line in config:
                self.__ip.append(str(line).strip())

        print("Config:")
        for i in range(len(self.__ip)):
            print("   %s" % self.__ip[i])

    def _connect(self):
        print("Connect to the remote servers")

        user = getpass.getuser()
        self.__username = input("Username [%s]: " % user)
        self.__password = getpass.getpass()

        print("Connecting..")
        for ip in self.__ip:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname=ip,
                               port=self.__port,
                               username=self.__username,
                               password=self.__password)
            except Exception as e:
                print(colors.red | "Connect to %s failed. [%s]" % (ip, str(e)))
            else:
                print(colors.green | "Connect to %s success." % ip)
                self.__clients[ip] = client

    def _execute_command(self, command):
        print(colors.red | "Command: %s\n" % command)
        for ip, client in self.__clients.items():
            try:
                stdin, stdout, stderr = client.exec_command(command, get_pty=True)
                stdin.write(self.__password + "\n")
                stdin.flush()
            except Exception as e:
                print(colors.blue | "%s:" % ip)
                print(colors.red | "%s" % str(e))
            else:
                print(colors.blue | "%s:" % ip)
                for line in stdout:
                    print(line, end='', flush=True)
                for line in stderr:
                    print(line, end='', flush=True)
                print("")

    def _close_client(self):
        for ip, client in self.__clients.items():
            client.close()


class Pyessh(cli.Application):
    PROGNAME = colors.green | project
    VERSION = colors.blue | version
    DESCRIPTION = colors.red | description
    _path = default_path

    @cli.switch(["-c", "--config"])
    def configuration(self, filename):
        """The configuration [default: /usr/local/pyessh.conf]"""
        self._path = filename

    def _print_info(self):
        print("%s %s\n%s" % (self.PROGNAME, self.VERSION, self.DESCRIPTION))

    def main(self):
        self._print_info()

        sm = SSHManager()
        print("-----config-----")
        sm._do_parse(self._path)
        print("-----config-----")

        sm._connect()

        while True:
            command = session.prompt(">>> ", mouse_support=True, auto_suggest=AutoSuggestFromHistory())
            if command.upper() == "EXIT":
                sm._close_client()
                print("Bye Bye")
                return
            else:
                sm._execute_command(command)


if __name__ == '__main__':
    Pyessh.run()
