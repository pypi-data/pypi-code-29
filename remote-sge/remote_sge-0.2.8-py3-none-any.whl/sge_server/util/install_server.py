import os
from configobj import ConfigObj
import sys
import string
from string import Template
from os.path import join, abspath, expandvars, expanduser, exists
from tempfile import NamedTemporaryFile
from io import StringIO
from argparse import RawTextHelpFormatter
from sge.util.arg_parser import ArgParser

YUM_PACKAGES = ['nginx', 'sqlite-devel', 'readline-devel', 'bzip2-devel',
                'git', 'gcc', 'gcc-c++', 'kernel-devel', 'make',
                'zlib-devel', 'openssl-devel']

# CONFIG_DIR = 'etc'
CONFIG = {
    'EDITOR' : None,
    'use_sudo' : False
}
DEFAULT_EDITOR = 'vim'
DESCRIPTION = """SGE Server Installer.

This script will make changes to your system, a number of which require
sudo priveleges.  Be warned.

You'll be prompted to edit/view configuration files created.  Make sure that
your editor of choice is properly configured.  See -e option for detail.

if the -i option is given, the following changes will be made to your system:

    * You'll be prompted to modify / verify various configuration settings.
    * nginx server will be configured as a proxy for the wsgi server.
    * It will NOT change existing nginx configuration, so if you want
        to turn off the default nginx server you'll have to do that yourself.
    * An upstart script will be installed, to control the wsgi server.
    * A certificate authority and self-signed server key will be created.

if -a is given, script YUM will be invoked to install nginx sqlite-devel
    readline-devel bzip2-devel git gcc gcc-c++ kernel-devel make zlib-devel
    openssl-devel
"""


ALINUX_ARG_TEXT = """Amazon Linux only, installs requirements via YUM.
Installs the following: nginx sqlite-devel readline-devel bzip2-devel
git gcc gcc-c++ kernel-devel make zlib-devel openssl-devel

This is enough to ensure that Python will build without warnings, and
that C extensions for required libraries will all compile.

TODO: verify that there are no unneeded dependencies listed here.
"""

EDITOR_TEXT = """Select an editor, such as pico.  Defaults to vim,
unless $EDITOR is set. If $EDITOR is set then this
option can be omitted, but specifying -e will overwrite
the settings from $EDITOR.
"""

ROOT_DESCRIPTION = """Where to place configs. Defaults to "$HOME/.config/remote_sge".
The main readon for changing this would be if you want place
the configuration into /etc/remote_sge.

Be sure that you take note of the access controls on whatever
location you specify.  If writing to that location requires
sudo privileges, be sure to specify the -s parameter."""

SYSTEMD_HELP = """Specify this if your system uses systemd.  Otherwise upstart will
be assumed.  This affects how gunicorn is installed, and how the
installer will restart services."""

FINAL_MESSAGE = """\n*\n*\n*\n********    FINISHED!!    **********\n
Installation seems to be successful.

You'll want to do a final check using test_remote_sge_server utility which is provided
to you, just to ensure connectivity.

I've packaged your client certificates into $HOME/remote_sge_client_certs.tgz.
Please copy that file to your client machine, you'll need them for client setup.

The client key I created was deleted from here.  Don't email it around.  You can use
the `remote_sge cert_req` workflow to generate certificates in a secure fashion.

Now, ssh to the client machine, and begin there.  Toodles!

"""

LOGFILE = expanduser(expandvars("~/remote_sge_server_install.log"))

def system(command):
    open(LOGFILE, 'a+').write(" >>>>>>>>> " + command + "\n")
    os.system(command + " >> " + LOGFILE + " 2>&1")

def sudo(command):
    system("sudo %s" % command)

def maybe_sudo(command):
    if CONFIG['use_sudo']:
        sudo(command)
    else:
        system(command)

parser = ArgParser(prog="remote_sge install_server",
                   formatter_class=RawTextHelpFormatter)

def get_editor(args):
    if args.editor:
        print("Given in params")
        return args.editor
    elif 'EDITOR' in os.environ:
        print("Environ")
        return os.environ['EDITOR']
    else:
        print("DEFAULT:")
        print(DEFAULT_EDITOR)
        return DEFAULT_EDITOR

def install_base_dir(loc):
    if CONFIG.get('development', None):
        return join(os.environ.get('PYTHONPATH') or os.getcwd(), loc)
    else:
        return "%s/%s" % (sys.prefix, loc)

def edit_config_file(name, filename, dest=None, loc='etc/remote_sge',
                     func=None, editor=None, unattended=False, **substitutions):
    if not editor:
        editor = CONFIG['EDITOR']
    source = join(install_base_dir(loc), filename)
    if dest:
        substitutions['dest_path']=expandvars(dest)
    with NamedTemporaryFile(mode='w') as temp_file:
        template = string.Template(open(source).read())
        temp_file.write(expandvars(template.substitute(**substitutions)))
        temp_file.flush()
        if not unattended and not CONFIG.get('UNATTENDED', False):
            print("Press enter to edit %s in your favorite editor." % name)
            sys.stdin.flush()
            sys.stdin.read(1)
            os.system(editor + " " + temp_file.name)
        if func:
            func(temp_file.name)
        elif dest:
            maybe_sudo("cp " + temp_file.name + " " + join(dest, filename))
        else:
            return open(temp_file.name).read()


def parse_args():
    parser.description = """
    Installs a working remote SGE server component.
    """
    parser.add_argument('install_server', help='Command.')
    parser.add_argument('-e', '--editor', help=EDITOR_TEXT, default=DEFAULT_EDITOR)
    parser.add_argument('-i', '--install',
                        help="Perform the installation.",
                        action="store_true")
    parser.add_argument('-u', '--unattended',
                        help="Unattended installation",
                        action="store_true")
    parser.add_argument('-r', '--root',
                        help=ROOT_DESCRIPTION,
                        default="$HOME/.config/remote_sge")
    parser.add_argument('-s', '--sudo',
                        help="Use sudo for placing config files (e.g. if installing into /etc).",
                        action="store_true")
    parser.add_argument('-a', '--alinux',
                        help="""Installs system components on Amazon Linux.""",
                        action="store_true")
    parser.add_argument('-d', '--development',
                        help="Development mode.  Install from PYTHONPATH.",
                        action="store_true")
    parser.add_argument('--systemd',
                        help=SYSTEMD_HELP,
                        action="store_true")
    parser.description = DESCRIPTION
    return parser.parse_args()

# https://stackoverflow.com/questions/21297139
class SslKeyCommands(object):
    CA = ("req -x509 -config ${conf_file} -newkey rsa:4096 " +
          "-sha256 -nodes -out ${certs_path}/ca/cacert.pem -outform PEM -subj " +
          "\"/C=${country_code}/ST=${state}/L=${city}/O=${org}/OU=${org_unit}/CN=${cname}\"" +
          " -keyout ${certs_path}/ca/cakey.pem")
    SRV_CSR = ("req -config ${conf_file} -newkey rsa:2048 -sha256 -nodes -out ${certs_path}" +
               "/servercert.csr -outform PEM -keyout ${certs_path}/serverkey.pem -subj " +
               "\"/C=${country_code}/ST=${state}/L=${city}/O=${org}/OU=${org_unit}/CN=${cname}\"")
    SRV_CRT = ("ca -batch -config ${conf_file} -policy signing_policy -extensions signing_req " +
               "-out ${certs_path}/servercert.pem -infiles ${certs_path}/servercert.csr")
    CLI_CSR = ("req -config ${conf_file} -keyout ${certs_path}/clientkey.pem -newkey rsa:2048 " +
               "-sha256 -nodes -out ${certs_path}/clientcert.csr -outform PEM -subj " +
               "\"/C=${country_code}/ST=${state}/L=${city}/O=${org}/OU=${org_unit}/CN=${cname}\"")
    CLI_CRT = ("ca -batch -config ${conf_file} -policy signing_policy -extensions signing_req " +
               "-out ${certs_path}/clientcert.pem -infiles ${certs_path}/clientcert.csr")

def make_client_csr(args, ssl_config=None):
    conf_path = expanduser(expandvars(args.root))
    certs_path = join(conf_path, 'certs')
    maybe_sudo("mkdir -p %s" % certs_path)
    if not ssl_config:
        ssl_config = load_config(
            string=edit_config_file("SSL Certificate details", 'ssl_config.ini'),
            name='ssl')
    # print(ssl_config['General'].dict())
    edit_config_file('CA Config File', 'openssl-client.ini', args.root, unattended=True,
                    cname=ssl_config['Client Cert']['common_name'],
                    **ssl_config['General'].dict())
    print("Creating Client key and CSR.")
    templ = Template(SslKeyCommands.CLI_CSR)
    command = "openssl " + templ.substitute(certs_path=certs_path,
                                            conf_file=join(args.root, 'openssl-client.ini'),
                                            cname=ssl_config['Client Cert']['common_name'],
                                            **ssl_config['General'].dict())
    maybe_sudo(command)

def install_server_keys(args):
    certs_path = join(args.root, 'certs')
    ca_path = join(certs_path, 'ca')
    maybe_sudo("mkdir -p %s" % certs_path)
    maybe_sudo("mkdir -p %s" % ca_path)
    maybe_sudo("touch " + join(ca_path, 'index.txt'))
    maybe_sudo("echo '01' | tee " + join(ca_path, 'serial.txt'))
    # Next step is to configure the openssl config files.
    ssl_config = load_config(string=edit_config_file("SSL Certificate details", 'ssl_config.ini'),
                             name='ssl')
    edit_config_file('CA Config File', 'openssl-ca.ini', args.root, unattended=True,
                     cname=ssl_config['CA Cert']['common_name'],
                     **ssl_config['General'].dict())
    edit_config_file('CA Config File', 'openssl-server.ini', args.root, unattended=True,
                     cname=ssl_config['Server Cert']['common_name'],
                     **ssl_config['General'].dict())
    server_cfg = ConfigObj(infile=join(expanduser(expandvars(args.root)), 'openssl-server.ini'))
    server_cfg['alternate_names'] = ssl_config['Server Cert']['Alternate Names'].dict()
    server_cfg.write()
    def make_key(templ_str, message, cname, conf_file, index):
        print("Creating " + message)
        maybe_sudo("echo '%s' | tee " % index + join(ca_path, 'serial.txt'))
        maybe_sudo("openssl " + Template(templ_str).substitute(certs_path=certs_path,
                                                               conf_file=conf_file,
                                                               cname=cname,
                                                               **ssl_config['General'].dict()))
    make_key(SslKeyCommands.CA, "Certificate authority key and certificate.",
             ssl_config['CA Cert']['common_name'], join(args.root, 'openssl-ca.ini'), '01')
    make_key(SslKeyCommands.SRV_CSR, "Server key and CSR.",
             ssl_config['Server Cert']['common_name'], join(args.root, 'openssl-server.ini'), '02')
    make_key(SslKeyCommands.SRV_CRT, "Trusted TLS Server Certificate.",
             None, join(args.root, 'openssl-ca.ini'), '03')
    make_client_csr(args, ssl_config)
    make_key(SslKeyCommands.CLI_CRT, "Trusted TLS Client Certificate.",
             None, join(args.root, 'openssl-ca.ini'), '04')
    print("\n\nOkay, I placed your certificates in " + certs_path)

def load_config(file=None, string=None, name=None):
    if file:
        config = ConfigObj(infile=expanduser(expandvars(file)))
    else:
        config = ConfigObj(infile=StringIO(string))
    if name:
        CONFIG[name] = config
    return config

def setup_gunicorn(args):
    script="/etc/init.d/remote_sge"
    def copy_gunicorn(f):
        sudo("cp %s %s" % (f, script))
        sudo("chown root %s" % script)
        sudo("chgrp $USER %s" % script)
        sudo("chmod 750 %s" % script)
    edit_config_file("Gunicorn Init Script", "gunicorn_init.d.sh",
        loc='bin', dest=args.root, func=copy_gunicorn, **CONFIG['main']['server'])
    edit_config_file("Gunicorn Config File", "gunicorn_config.py", args.root, **CONFIG['main']['server'])
    # edit_config_file("Gunicorn Upstart Config", "gunicorn_upstart.conf", args.root, **CONFIG['main']['server'])
    edit_config_file("Gunicorn Logging Config", "logging.conf", args.root, **CONFIG['main']['server'])
    sudo(script + " restart")


def setup_nginx(args):
    config = load_config(file=join(args.root, "config.ini"), name="main")
    maybe_sudo("mkdir -p " + config["server"]["work_root"])
    maybe_sudo("mkdir -p " + config["server"]["completed_files_root"])
    edit_config_file("Web Server Configuration", "nginx.conf", args.root, **config['server'])
    sudo_rm_symlink("/etc/nginx/conf.d/remote_sge.server.conf")
    sudo("ln -s %s /etc/nginx/conf.d/remote_sge.server.conf" % expandvars(join(args.root, "nginx.conf")))
    sudo("usermod -aG $USER nginx")
    sudo("chkconfig nginx on")
    restart_service('nginx')

def sudo_rm_symlink(f):
    system("if [[ -L '%s' ]]; then sudo rm '%s'; fi" % (f, f))

def do_install(args):
    os.system("if [[ -e %s ]]; then rm %s; fi" % (LOGFILE, LOGFILE))
    CONFIG['EDITOR'] = args.editor
    CONFIG['UNATTENDED'] = args.unattended
    if args.alinux:
        sudo("yum -y install " + " ".join(YUM_PACKAGES))
    CONFIG['development'] = args.development
    maybe_sudo("mkdir -p %s" % args.root)
    edit_config_file("Main config file", "config.ini", args.root)
    install_server_keys(args)
    setup_nginx(args)
    setup_gunicorn(args)
    system("tar -cvf $HOME/remote_sge_client_certs.tar " +
              "-C %s clientkey.pem clientcert.pem" % join(args.root, 'certs'))
    system("tar -vuf $HOME/remote_sge_client_certs.tar " +
              "-C %s cacert.pem" % join(args.root, 'certs', 'ca'))
    system("gzip $HOME/remote_sge_client_certs.tar")
    system("mv $HOME/remote_sge_client_certs.tar.gz $HOME/remote_sge_client_certs.tgz")
    system("rm %s/certs/*.csr" % args.root)
    system("rm %s/certs/clientkey.pem" % args.root)
    print(FINAL_MESSAGE)

def restart_service(name):
    print("Restarting " + name)
    if CONFIG['loader'] == 'upstart':
        command = "service %s restart"
    else:
        command = "systemctl restart %s"
    sudo(command % name)

def set_system_loader(args):
    if args.systemd:
        CONFIG['loader'] = 'systemd'
    else:
        CONFIG['loader'] = 'upstart'

def main():
    args = parse_args()
    set_system_loader(args)
    if args.sudo:
        CONFIG['use_sudo'] = True
    if args.install:
        do_install(args)
    else:
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    main()


