from os.path import exists, join, abspath, expanduser, expandvars
import os
from sys import stderr
from configobj import ConfigObj
import requests
from sge_client.client_config import ClientConfig
from sge.io.config import load_config

from sge.util.arg_parser import ArgParser
try:
    import requests_unixsocket
    from urllib.parse import quote
    UNIX_SOCKETS_FOUND = True
except ModuleNotFoundError:
    UNIX_SOCKETS_FOUND = False
    print("requests_unixsocket is not installed.  Try installing it to be able to test socket" +
          "connectivity.", file=stderr)

class NotFound(Exception):
    pass

CONFIGDIR_HELP = """The location of the config files.  Probably either ~/.config/remote_sge,
or /etc/remote_sge."""

def check_socket(config):
    requests_unixsocket.monkeypatch()
    socket = config.get('wsgi_binding').split(":")[1]

    response = requests.get("http+unix://%s/" % quote(socket, safe=""))
    if response.status_code == 200:
        print("Socket connection successful at " + config.get('wsgi_binding'))
        return True
    else:
        print("Gunicorn responded with HTTP %s instead of 200." % response.status_code, file=stderr)
        print("Response body: " + response.text, file=stderr)
        print("Please restart Gunicorn with `/etc/init.d/remote_sge restart`")
        return False

def test_url(path, success, fail, config):
    url = "https://%s:%s%s" % (config.host, config.port, path)
    print(" Checking " + url)
    response = requests.get(url, **config.ssl_config)
    if response.status_code == 200:
        print(success)
        return True
    else:
        print("Server responded with HTTP %s instead of 200." % response.status_code, file=stderr)
        print("Response body: " + response.text, file=stderr)
        print(fail, file=stderr)
        return False

def parse_args():

    parser = ArgParser(prog="remote_sge")
    parser.add_argument('test_server', help="Command to run")
    parser.add_argument('endpoint', help="endpoint for server to contact, as given in config file " +
                        "or 'default' for default server.  Default is to use default server.",
                        default="default", nargs="?")
    parser.add_argument('-r', '--remote',
                        help="Only check basic SSL connectivity on remote server.",
                        action="store_true")
    return parser.parse_args()

def check_archivedir(args, server_config, client_config):
    archivedir = server_config.get("completed_files_root")
    test_file = join(archivedir, "12345.text")
    open(test_file, 'w+').write("This is for sure a test file.")
    try:
        return test_url("/jobs/complete/12345.text",
            "Successfully downloaded a file from the archive directory.",
            "Error downloading file from archive directory.  The most common reason for this" +
            " Is a permissions issue.  Default permission setup for this installer is to put" +
            " the nginx user into your user's primary group.  In order for nginx to read " +
            "from %s, it needs to be able to traverse from / and read/execute " % archivedir +
            "directories all the way down the tree.  You can use `namei -om %s`" % archivedir +
            " as a way to check and see what the permissions are like all the way to this " +
            " directory.", client_config)
    except Exception as ex:
        print(ex)
        return False
    finally:
        os.remove(test_file)

def main():
    args = parse_args()
    server_config = load_config()
    client_config = ClientConfig(load_config(), endpoint=args.endpoint)
    result = test_url("/", "Basic nginx connectivity works.",
        "Failed connecting to nginx.  Check to make sure service is running." +
        "If the response was 502 Bad Gateway, it's likely that Gunicorn is not " +
        "running or that nginx can't access the socket.  Make sure that nginx has " +
        "access to the socket, and that Gunicorn is running.  Check the Gunicorn log for" +
        "errors.", client_config)

    if 'server' in server_config.sections and not args.remote:
        if UNIX_SOCKETS_FOUND:
            result = result and check_socket(server_config['server'])
        result = result and check_archivedir(args, server_config['server'], client_config)

    if result:
        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    main()
