import os


class Php:
    config_dir = '/etc/php-fpm.d'
    """
    :param _domain: cli/lib/Domain
    """
    _domain = None

    def __init__(self, domain):
        """
        :param domain: cli/lib/Domain
        """
        self._domain = domain

    def configure_domain(self):
        config_file = self.config_dir + '/' + self._domain.domain_name + '.conf'
        config = str.join("\n", [
            "[" + self._domain.domain_name + "]",
            "chdir = /",
            "user = " + self._domain.ftp_username,
            "group = " + self._domain.ftp_username,
            "listen = /run/php-fpm/" + self._domain.domain_name + ".sock",
            "listen.acl_users = apache,nginx",
            "listen.allowed_clients = 127.0.0.1",
            "listen.owner = apache",
            "listen.group = apache",
            "pm = dynamic",
            "pm.max_children = 50",
            "pm.start_servers = 5",
            "pm.min_spare_servers = 5",
            "pm.max_spare_servers = 35",
            "slowlog = /domains/" + self._domain.domain_name + "/logs/php-slow.log",
            "php_admin_value[disable_functions] = exec,passthru,shell_exec,system",
            "php_admin_value[open_basedir] = /home/" + self._domain.ftp_username + "/" + self._domain.domain_name + ":/domains/" + self._domain.domain_name,
            "php_admin_value[upload_tmp_dir] = /domains/" + self._domain.domain_name + "/tmp",
            "php_admin_value[error_log] = /domains/" + self._domain.domain_name + "/logs/php-error.log",
            "php_admin_value[sendmail_path] = /usr/sbin/sendmail -t -i -f" + self._domain.ftp_username + "@ardynamics.eu",
            "php_admin_flag[log_errors] = on",
            "php_admin_flag[allow_url_fopen] = off",
            "php_value[session.save_handler] = files",
            "php_value[session.save_path] = /domains/" + self._domain.domain_name + "/tmp",
            "php_value[soap.wsdl_cache_dir] = /domains/" + self._domain.domain_name + "/tmp"
        ])
        f = open(config_file, "w")
        f.write(config)
        f.close()

    @staticmethod
    def restart_service():
        os.system('/bin/systemctl restart php-fpm.service')
