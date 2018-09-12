#! /usr/bin/env python
# coding: utf-8

import os
import re
import datetime
import ldap
from ldap import SCOPE_SUBTREE as LDAP_SCOPE_SUBTREE
from ldap.ldapobject import ReconnectLDAPObject
from ldap import modlist, LDAPError
from ldap_user.util.string_tool import encode
from ldap_user.util.verify_secret import verify, SUPPORT_METHOD

__author__ = '鹛桑够'


class LDAPUser(object):

    EPOCH_DATE = datetime.datetime.fromtimestamp(0)
    LOGIN_SHELL = "/bin/bash"
    HOME_BASE_DIRECTORY = "/home"
    GROUP_ID_NUMBER = None
    CREATOR = None
    VERIFY_CREATOR = True

    password_compile = re.compile("^{(%s)}(\S+)$" % "|".join(SUPPORT_METHOD))

    def __init__(self, ldap_uri, base_dn, admin_user, admin_password, home_base_directory=None, group_id=None):
        self.ldap_uri = ldap_uri
        self.ldap_com = ReconnectLDAPObject(ldap_uri, retry_max=10, retry_delay=3)
        # self.ldap_com = ldap.initialize(ldap_uri)
        self.ldap_base_dn = base_dn
        if home_base_directory is not None:
            self.HOME_BASE_DIRECTORY = home_base_directory
        if group_id is not None:
            self.GROUP_ID_NUMBER = "%s" % group_id
        self.ldap_admin = "cn=%s,%s" % (admin_user, self.ldap_base_dn)
        self.people_base_cn = "ou=People,%s" % self.ldap_base_dn
        self.ldap_com.bind_s(self.ldap_admin, admin_password)

    def __get_next_uid_number(self):
        filter_str = "uid=*"
        attributes = ["uidNumber", "gidNumber"]
        items = self.ldap_com.search_s(self.people_base_cn, LDAP_SCOPE_SUBTREE, filter_str, attributes)
        max_number = 1000
        for item in items:
            if "uidNumber" in item[1]:
                u_number = int(item[1]["uidNumber"][0])
                if max_number < u_number:
                    max_number = u_number
        return max_number + 1

    def delete_user(self, user_name):
        if self.exist(user_name) is None:
            return True
        dn = "uid=%s,%s" % (user_name, self.people_base_cn)
        return self.ldap_com.delete_s(dn)

    def add_user(self, user_name, uid_number=None, gid_number=None, home_directory=None):
        dn = "uid=%s,%s" % (user_name, self.people_base_cn)
        attributes = dict()
        for key in ("uid", "cn", "sn"):
            attributes[key] = encode(user_name)
        attributes["objectClass"] = ["top", "person", "inetOrgPerson", "posixAccount", "organizationalPerson",
                                     "shadowAccount"]
        if uid_number is None:
            attributes["uidNumber"] = encode(self.__get_next_uid_number())
        else:
            attributes["uidNumber"] = encode(uid_number)
        if gid_number is None:
            attributes["gidNumber"] = encode(self.GROUP_ID_NUMBER)
        else:
            attributes["gidNumber"] = encode(gid_number)
        if attributes["gidNumber"] is None:
            raise LDAPError("please set gidNumber")
        if home_directory is None:
            home_directory = os.path.join(self.HOME_BASE_DIRECTORY, user_name)
        attributes["homeDirectory"] = encode(home_directory)
        attributes["loginShell"] = encode(self.LOGIN_SHELL)
        if self.CREATOR is not None:
            attributes["givenName"] = encode(self.CREATOR)
        mod_list = ldap.modlist.addModlist(attributes)
        self.ldap_com.add_s(dn, mod_list)

    def expire_user(self, user_name, shadow_expire=None):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        old_attributes = user_entry[1]
        attributes = dict(**old_attributes)
        if shadow_expire is None:
            attributes["shadowExpire"] = ["%s" % (datetime.datetime.now() - self.EPOCH_DATE).days]
        else:
            attributes["shadowExpire"] = ""
        mod_list = ldap.modlist.modifyModlist(old_attributes, attributes)
        return self.ldap_com.modify_s(user_entry[0], mod_list)

    def block_user(self, user_name):
        return self.expire_user(user_name)

    def unlock_user(self, user_name):
        user_entry = self.exist(user_name, "pwdAccountLockedTime", "shadowExpire")
        if user_entry is None:
            return False
        old_attributes = user_entry[1]
        attributes = dict(**old_attributes)
        if "pwdAccountLockedTime" in attributes:
            attributes["pwdAccountLockedTime"] = ""
        if "shadowExpire" in attributes:
            attributes["shadowExpire"] = ""
        mod_list = ldap.modlist.modifyModlist(old_attributes, attributes)
        return self.ldap_com.modify_s(user_entry[0], mod_list)

    def _verify_creator(self, user_entry):
        if self.CREATOR is None or self.VERIFY_CREATOR is False:
            return True
        if "givenName" not in user_entry:
            return False
        return self.CREATOR in user_entry["givenName"]

    def exist(self, user_name, *attributes):
        l_attributes = set(attributes)
        sr = self.ldap_com.search_s(self.ldap_base_dn, LDAP_SCOPE_SUBTREE, "uid=%s" % user_name, l_attributes)
        if len(sr) <= 0:
            return None
        return sr[0]

    def verify_password(self, password, ldap_password):
        match_r = self.password_compile.match(ldap_password)
        if match_r is not None:
            method = match_r.groups()[0]
            cipher_text = match_r.groups()[1]
            return verify(method, password, cipher_text)
        return password == ldap_password

    def login(self, user_name, password):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        attr = user_entry[1]
        if "userPassword" not in attr:
            return False
        ldap_password = attr["userPassword"][0]
        return self.verify_password(password, ldap_password)

    def login2(self, user_name, password):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        attr = user_entry[1]
        if "userPassword" not in attr:
            return False
        try:
            self.ldap_com.simple_bind_s(user_entry[0], password)
            return True
        except ldap.INVALID_CREDENTIALS:
            return False

    def set_password(self, user_name, new_password):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        if self._verify_creator(user_entry) is False:
            return False
        pr = self.ldap_com.passwd_s(user_entry[0], None, new_password)
        if pr[0] is None and pr[1] is None:
            return True
        return False
