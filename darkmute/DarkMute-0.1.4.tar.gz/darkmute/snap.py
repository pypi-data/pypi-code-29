from zeroconf import ServiceBrowser, Zeroconf
import snapcast.control
import ipaddress
import netifaces


class Scanner:

    services = []

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        self.services.append(info)


def get_snapcast_server(loop):
    '''Scan for services then find snapcast server.'''
    zeroconf = Zeroconf()
    listener = Scanner()
    ServiceBrowser(zeroconf, "_snapcast._tcp.local.", listener)

    while listener.services == []:
        pass

    server_ip_bytes = listener.services[0].address
    server_ip = str(ipaddress.ip_address(server_ip_bytes))
    # Snapserver.__init__ does not work in snapcast==2.0.8
    # Use create_server instead as recommended in:
    # https://github.com/happyleavesaoc/python-snapcast/issues/12
    # https://github.com/happyleavesaoc/python-snapcast/issues/19
    create_server_coroutine = snapcast.control.create_server(
        loop, server_ip, reconnect=True)
    server = loop.run_until_complete(create_server_coroutine)

    return server


def get_mac_addresses():
    '''Get list of all IPv4 MAC addresses for this device.'''
    def contains_loopback(af_inet_addresses):
        '''Check if list of IPv4 addresses contains loopback.'''
        for ip in af_inet_addresses:
            if ipaddress.IPv4Address(ip['addr']).is_loopback:
                return True
        return False

    mac_addresses = []
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        # Skip interfaces without an IPv4 address
        if netifaces.AF_INET not in addresses:
            continue
        if contains_loopback(addresses[netifaces.AF_INET]):
            continue
        for mac in addresses[netifaces.AF_LINK]:
            # Add to list if address has 'addr' key
            if mac['addr']:
                mac_addresses.append(mac['addr'])
    return mac_addresses


def get_snapcast_client(loop):
    '''Scan through list of clients to find correct one.'''
    server = get_snapcast_server(loop)
    mac_addresses = get_mac_addresses()
    for client in server.clients:
        # print(client.identifier)
        if client.identifier in mac_addresses:
            return client
