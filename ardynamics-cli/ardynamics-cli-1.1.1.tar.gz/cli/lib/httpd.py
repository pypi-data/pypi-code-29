import os


class Httpd:
    config_dir = '/etc/httpd/conf.sites.d'
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
            "<VirtualHost *:8080>",
            "  ServerName " + self._domain.domain_name,
            "  ServerAdmin info@ardynamics.eu",
            "  DocumentRoot /domains/" + self._domain.domain_name + "/public_html",
            "  ErrorLog /domains/" + self._domain.domain_name + "/logs/error.log",
            "  CustomLog /domains/" + self._domain.domain_name + "/logs/access.log combined",
            "  <Directory /domains/" + self._domain.domain_name + "/public_html>",
            "    Options +FollowSymLinks",
            "    AllowOverride All",
            "    Order allow,deny",
            "    Allow from all",
            "    Require all granted",
            "  </Directory>",
            "  <FilesMatch \.php$>",
            "    SetHandler \"proxy:unix:/run/php-fpm/" + self._domain.domain_name + ".sock|fcgi://localhost\"",
            "  </FilesMatch>",
            "</VirtualHost>"
        ])
        f = open(config_file, "w")
        f.write(config)
        f.close()

    @staticmethod
    def restart_service():
        os.system('/bin/systemctl restart httpd.service')
