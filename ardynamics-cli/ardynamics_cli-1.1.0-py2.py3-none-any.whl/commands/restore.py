# cli/commands/restore.py

import os
import sys
import tarfile

from .base import Base


class Restore(Base):
    single_domain = False
    config = None
    backup_file = None
    backup_folder = None

    def run(self):
        self._load_config()
        self._download_db_backups()
        self._restore_domains()
        self._restart_services()

    def _load_config(self):
        from cli.lib import Config
        config_file = self.get_location('backup.cfg')
        self.bucket.download_file('backup/backup.cfg', config_file)
        self.config = Config(config_file)

    def _download_db_backups(self):
        backup_file = self.get_location('/root/mysqldump.tgz')
        backup_folder = self.get_location('/root/mysqldump')
        if not os.path.isdir(backup_folder):
            print('  - Downloading database backups...')
            self.bucket.download_file(self.config.get_backup_folder() + '/mysqldump.tgz', backup_file)
            print('  - Extracting database backups...')
            tar = tarfile.open(backup_file)
            tar.extractall(path=self.get_location('/root/'))
            tar.close()

    def _restore_domains(self):
        domains = []
        if self.options['--domain']:
            domains.append(self.options['--domain'])
            self.single_domain = True
        else:
            domains = self.config.get_domains()
        for domain_name in domains:
            self._restore_domain(domain_name)

    def _restore_domain(self, domain_name):
        try:
            from cli.lib import Domain
            domain = Domain(domain_name, self.config)
            print('Restoring domain ' + domain_name + ':')
            self._restore_domain_ftp_user(domain)
            self._restore_domain_symbolic_link(domain)
            self._restore_domain_download_backup(domain)
            self._restore_domain_extract_backup(domain)
            self._restore_domain_create_database(domain)
            self._restore_domain_configure_httpd(domain)
            self._restore_domain_configure_php(domain)
        except:
            print('Unexpected error when parsing domain ' + domain_name + ':', sys.exc_info()[0])
            if self.options['--debug']:
                raise

    def _restore_domain_ftp_user(self, domain):
        print('  - Restore user ' + domain.ftp_username)
        from cli.lib import User
        user = User(domain.ftp_username)
        user.create_account()
        user.set_password(domain.ftp_password)

    def _restore_domain_symbolic_link(self, domain):
        print('  - Linking into domains...')
        if not os.path.isdir('/domains'):
            os.system('mkdir /domains')
        if not os.path.exists('/domains/' + domain.domain_name):
            os.system('ln -s /home/' + domain.ftp_username + '/' + domain.domain_name + '/ /domains/' + domain.domain_name)

    def _restore_domain_download_backup(self, domain):
        self.backup_file = self.get_location(domain.get_archive_name())
        if not os.path.isfile(self.backup_file):
            print('  - Downloading backup...')
            self.bucket.download_file(self.config.get_backup_folder() + '/' + domain.get_archive_name(), self.backup_file)

    def _restore_domain_extract_backup(self, domain):
        self.backup_folder = self.get_location('/home/' + domain.ftp_username + '/' + domain.domain_name)
        if not os.path.isdir(self.backup_folder) or self.single_domain:
            print('  - Extracting backup...')
            tar = tarfile.open(self.backup_file, mode="r:gz")
            updated = []
            for m in tar.getmembers():
                m.name = unicode(m.name, 'utf-8')
                updated.append(m)
            tar.extractall(members=updated, path=self.get_location('/home/' + domain.ftp_username + '/'))
            tar.close()
            print('  - Restore permissions...')
            os.system('chown -R ' + domain.ftp_username + ':' + domain.ftp_username + ' /home/' + domain.ftp_username)

    def _restore_domain_create_database(self, domain):
        print('  - Restoring database...')
        backup_file = self.get_location('/root/mysqldump/' + domain.db_username + '.sql')
        from cli.lib import MariaDB
        mariadb = MariaDB(self.config)
        mariadb.create_database(domain.db_username, domain.db_password)
        mariadb.import_database(domain.db_username, backup_file)

    def _restore_domain_configure_httpd(self, domain):
        print('  - Configuring HTTP server...')
        from cli.lib import Httpd
        httpd = Httpd(domain)
        httpd.configure_domain()

    def _restore_domain_configure_php(self, domain):
        print('  - Configuring PHP...')
        from cli.lib import Php
        php = Php(domain)
        php.configure_domain()

    def _restart_services(self):
        print('Restarting services...')
        from cli.lib import Httpd, Php
        Httpd.restart_service()
        Php.restart_service()
