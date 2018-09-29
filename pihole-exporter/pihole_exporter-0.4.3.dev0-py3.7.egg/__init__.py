name = 'pihole_exporter'
__VERSION__ = '0.4.2'

import argparse
import pihole_exporter


def get_authentication_token():
    token = None
    filename = '/etc/pihole/setupVars.conf'
    try:
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('WEBPASSWORD'):
                    token = line.split('=')[1]
                    return token
            return None
    except (FileNotFoundError):
        print("Unable to find: %s" % filename)


def main():
    parser = argparse.ArgumentParser(
        description='pihole_exporter')
    parser.add_argument('-o', '--pihole',
        help='pihole adress',
        default='pi.hole')
    parser.add_argument('-p', '--port', type=int,
        help='port pihole_exporter is listening on',
        default=9311)
    parser.add_argument('-i', '--interface',
        help='interface pihole_exporter will listen on',
        default='0.0.0.0')
    parser.add_argument('-a', '--auth',
        help='Pihole password hash',
        default=None)
    args = parser.parse_args()

    auth_token = args.auth
    if auth_token == None:
        auth_token = get_authentication_token()


    exporter = pihole_exporter.pihole_exporter(args.pihole, auth_token)
    exporter.make_server(args.interface, args.port)


if __name__ == '__main__':
    main()
