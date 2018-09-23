import os
import mysql.connector as mariadb


class MariaDB:
    _config = None
    _connection = None

    def __init__(self, config):
        """
        :type config: Config
        """
        self._config = config
        db_hostname = 'localhost'
        db_username = 'root'
        db_password = config.get_secret('db_root_password', True)
        self._connection = mariadb.connect(host=db_hostname, user=db_username, passwd=db_password)

    def create_database(self, username, password):
        statements = [
            str.join("", ['CREATE DATABASE IF NOT EXISTS ', username]),
            str.join("", ['CREATE USER IF NOT EXISTS \'', username, '\'@\'localhost\' IDENTIFIED BY \'', password, '\'']),
            str.join("", ['GRANT ALL PRIVILEGES ON ', username, '.* TO \'', username, '\'@\'localhost\''])
        ]
        cursor = self._connection.cursor()
        for query in statements:
            print('    ' + query)
            cursor.execute(query)

    def import_database(self, database_name, backup_file):
        print('    Importing SQL dump file... ' + database_name)
        if not os.path.isfile(backup_file):
            from cli.lib import InputError
            raise InputError('Unable to find dump file: ' + backup_file)
        db_password = self._config.get_secret('db_root_password', True)
        os.system('mysql -u root -p' + db_password + ' ' + database_name + ' < ' + backup_file)
