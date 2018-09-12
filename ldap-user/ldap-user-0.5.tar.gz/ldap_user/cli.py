#! /usr/bin/env python
# coding: utf-8
import os
import sys
import argparse
from ldap_user import LDAPConfig

__author__ = '鹛桑够'


def set_env(env_name, value):
    code1 = os.system('sed -i "/^export %s=.*/d" $HOME/.bash_profile' % env_name)
    code2 = os.system('echo "export %s=%s" >> $HOME/.bash_profile' % (env_name, value))
    if code1 == code2 == 0:
        print("SET %s=%s" % (env_name, value))


def create_config():
    args_man = argparse.ArgumentParser()
    args_man.add_argument("--admin-user", dest="admin_user", metavar="user_name", help="LDAP admin user", required=True)
    args_man.add_argument("--admin-password", dest="admin_password", metavar="password", help="LDAP admin user password",
                          required=True)
    args_man.add_argument("-e", dest="env_name", metavar="env_name", default="LDAP_USER_CONF", help="set environment, "
                                                                                                    "the env name")
    args_man.add_argument("config_path", metavar="path", nargs="?", help="where to save. default is stdout.")
    if len(sys.argv) <= 1:
        sys.argv.append("-h")
    args = args_man.parse_args()
    LDAPConfig.create(args.config_path, admin_user=args.admin_user, admin_password=args.admin_password)
    if args.config_path is not None:
        value = os.path.abspath(args.config_path)
        set_env(args.env_name, value)

if __name__ == "__main__":
    sys.argv.extend(["--admin-user", "root", "--admin-password", "123456", "ldap_user.conf"])
    create_config()
