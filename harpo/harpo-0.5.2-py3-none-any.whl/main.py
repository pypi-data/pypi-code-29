# Copyright 2018 Behavox Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gnupg

from harpo.domains import *
from harpo.groups import *
from harpo.users import *

class Harpo(object):
    """harpo main class"""

    def __init__(self, base_path, gpg_home_sys):
        """
        :param base_path: path to the root of the repository
        :param gpg_home_sys: path to user's GPG dir to import keys from
        """
        self.base_path = base_path
        self.path = os.path.join(base_path, '.harpo')
        self.access_dir = os.path.join(self.path, 'access')
        self.domains_dir = os.path.join(self.path, 'domains')

        self.gpg_home = os.path.join(self.path, 'keychain')
        self.gpg = gnupg.GPG(gnupghome=self.gpg_home)
        self.gpg_home_sys = gpg_home_sys
        self.gpg_sys = gnupg.GPG(gnupghome=self.gpg_home_sys, use_agent=True)

        self.domains = DomainManager(self.path)
        self.users = UserManager(self.path, self.gpg, self.gpg_sys)
        self.groups = GroupManager(self.path)

    def is_initialized(self):
        """
        Check if harpo is initialized
        :return: bool
        """
        return os.path.exists(self.path)

    def initialize(self):
        """
        Create harpo directory structure
        :return: True on success, False on failure
        """
        if self.is_initialized():
            logging.warning("Already initialized at %s", self.path)
            return False

        logging.info("Initializing at %s", self.path)

        # make dirs
        dirs = [
            self.access_dir,
            self.domains_dir
        ]
        for directory in dirs:
            mkdir_p(directory)

        logging.info("OK")
        return True

    # Domains -------------------------------------------------------
    def add_domain(self, domain_name):
        domain = self.domains.create(domain_name)
        return domain

    def remove_domain(self, domain_name):
        domain = self.domains.remove(domain_name)
        return domain

    def list_domains(self):
        return [d.name for d in self.domains]

    def show_domain(self, domain):
        if not self.domains[domain].exists:
            raise HarpoException("Domain doesn't exist: {}".format(domain))
        return {
            "access": {
                "users": self.domains[domain].recipients['users'],
                "groups": self.domains[domain].recipients['groups'],
            }
        }

    # Users ---------------------------------------------------------
    def add_user(self, user_name):
        user = self.users.create(user_name)
        self.reencrypt_all()
        return user

    def remove_user(self, user_name):
        user = self.users.remove(user_name)
        self.reencrypt_all()
        return user

    def list_users(self):
        return [d.uid for d in self.users]

    def show_user(self, user_name):
        user = self.users[user_name]
        if user.exists:
            return {
                "key": user.key,
                "access": {
                    "groups": [g for g in self.groups if self.groups[g].has_user(user.uid)]
                }
            }
        else:
            raise HarpoUserDoesntExist(user_name)

    # Groups --------------------------------------------------------
    def add_group(self, group_name):
        group = self.groups.create(group_name)
        return group

    def remove_group(self, group_name):
        group = self.groups.remove(group_name)
        self.reencrypt_all()
        return group

    def list_groups(self):
        return [group for group in self.groups]

    def add_user_to_group(self, user_name, group_name):
        user = self.users[user_name]
        if user.exists:
            group = self.groups[group_name]
            logging.info("Add user '%s' to group '%s'", user.uid, group_name)
            group.add_user(user.uid)
            self.groups.save()
            self.reencrypt_all()
            return group

    def remove_user_from_group(self, user_name, group_name):
        user = self.users[user_name]
        if user.exists:
            group = self.groups[group_name]
            logging.info("Remove user '%s' from group '%s'", user.uid, group_name)
            group.remove_user(user.uid)
            self.groups.save()
            self.reencrypt_all()
            return group

    def show_group(self, group_name):
        return self.groups[group_name].data

    # Crypto --------------------------------------------------------
    def get_key_by_uids(self, uid):
        return self.gpg.list_keys(keys=uid)

    def encrypt(self, domain, key, value):
        """
        Encrypt given string with a key of each user in a given domain + with admins' keys
        :param domain: domain name
        :param key: secret name
        :param value: secret value
        :return: path to encrypted secret
        """
        recipients = []
        recipients_users = self.domains[domain].recipients['users']
        recipients += recipients_users
        recipients_groups = self.domains[domain].recipients['groups']
        for group in recipients_groups:
            recipients += self.groups[group].data['users']

        recipients = list_uniq(recipients)
        recipients_fps = [self.users[u].fingerprint for u in recipients]
        logging.debug("Encrypt %s/%s. Recipients: %s", domain, key, recipients_fps)

        if len(recipients) == 0:
            raise HarpoException("No valid recipients (users) found for domain '{}'".format(domain))

        encrypted_ascii_data = self.gpg.encrypt(value, recipients, always_trust=True)
        if encrypted_ascii_data.ok:
            logging.debug("Successfully encrypted %s. Writing...", key)
        else:
            logging.error("Error encrypting %s", key)

        secret_file_path = self.domains[domain].store_encrypted_data(key, encrypted_ascii_data)
        logging.debug("Done.")
        return secret_file_path

    def decrypt(self, domain, key):
        """
        Decrypt specified secret in a given domain
        :param domain: domain name
        :param key: secret name
        :return: decrypted secret
        """
        logging.debug("Decrypt %s/%s", domain, key)
        encrypted_ascii_data = self.domains[domain].read_encrypted_data(key)
        result = self.gpg_sys.decrypt(encrypted_ascii_data)
        if result.ok:
            return str(result)
        else:
            raise HarpoException("Decryption failed for {}/{}:\n{}".format(domain, key, result.stderr))

    def reencrypt(self, domain):
        """
        Reencrypt all secrets in a given domain
        :param domain: domain name
        :return: None
        """
        for key in self.domains[domain].secrets:
            logging.debug("Reencrypt %s/%s", domain, key)
            value = self.decrypt(domain, key)
            self.encrypt(domain, key, value)

    def reencrypt_all(self):
        """
        Reencrypt all secrets in harpo
        :return: None
        """
        logging.info("Reencrypting everything!")
        for domain in self.list_domains():
            try:
                self.reencrypt(domain)
            except HarpoException as e:
                logging.warning("%s, skipping...", e)

    def remove_secret(self, domain, key):
        """
        Remove specified secret in a given domain
        :param domain: domain name
        :param key: secret name
        :return: removed secret path
        """
        return self.domains[domain].remove_encrypted_data(key)
