#! /usr/bin/env python
# coding: utf-8
import os
import ConfigParser
import ldap
from ldap_user.util.config import load_config
from ldap_user import LDAPUser

__author__ = '鹛桑够'


class OpenLDAPConfig(object):
    ldap_option_dict = dict(TLS_CACERTDIR=ldap.OPT_X_TLS_CACERTDIR, TLS_CACERTFILE=ldap.OPT_X_TLS_CACERTFILE)
    conf_path = "/etc/openldap/ldap.conf"

    @classmethod
    def read_and_load(cls, conf_path=None):
        if conf_path is None or len(conf_path) == 0:
            conf_path = cls.conf_path
        c_values = load_config(conf_path)
        for ok in cls.ldap_option_dict.keys():
            if ok in c_values:
                ldap.set_option(cls.ldap_option_dict[ok], c_values[ok])
        return c_values


class LDAPConfig(object):

    SECTION_NAME = "ldap"

    @staticmethod
    def load(config_path, section_name=None, section_index=None, **kwargs):
        if os.path.isfile(config_path) is False:
            return None
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        _section_name = LDAPConfig.SECTION_NAME
        if section_name is not None:
            _section_name = section_name
        elif section_index is not None:
            _section_name = config.sections()[section_index]

        init_kwargs = dict()
        if config.has_option(_section_name, "ldap_config") is True:
            sys_config = OpenLDAPConfig.read_and_load(config.get(_section_name, "ldap_config"))
            if "URI" in sys_config:
                init_kwargs["ldap_uri"] = sys_config["URI"]
            if "BASE" in sys_config:
                init_kwargs["base_dn"] = sys_config["BASE"]

        init_keys = ["ldap_uri", "base_dn", "admin_user", "admin_password", "home_base_directory", "group_id"]
        for key in init_keys:
            if config.has_option(_section_name, key):
                init_kwargs[key] = config.get(_section_name, key)
        if config.has_option(_section_name, "creator") is True:
            LDAPUser.CREATOR = config.get(_section_name, "creator")
        if config.has_option(_section_name, "login_shell") is True:
            LDAPUser.LOGIN_SHELL = config.get(_section_name, "login_shell")
        ldap_com = LDAPUser(**init_kwargs)
        return ldap_com

    @staticmethod
    def create(conf_path=None, ldap_uri=None, base_dn=None, admin_user="", admin_password="", home_base_directory=None,
               group_id=None, creator="", login_shell=None, ldap_config="", section_name=None):
        if login_shell is None:
            login_shell = "/bin/bash"
        if section_name is None:
            section_name = LDAPConfig.SECTION_NAME
        config_content = "[%s]\n" % section_name
        if group_id is None:
            group_id = os.getgid()
        kwargs = dict(ldap_uri=ldap_uri, base_dn=base_dn, admin_user=admin_user, admin_password=admin_password,
                      home_base_directory=home_base_directory, group_id=group_id, creator=creator,
                      login_shell=login_shell, ldap_config=ldap_config)
        for key in kwargs:
            if kwargs[key] is not None:
                config_content += "%s: %s\n" % (key, kwargs[key])
        if conf_path is None:
            print(config_content)
        else:
            with open(conf_path, "w") as w:
                w.write(config_content)
        return True


if __name__ == "__main__":
    c = OpenLDAPConfig()
    vs = c.read_and_load()
    print(vs)
    LDAPConfig.create()
