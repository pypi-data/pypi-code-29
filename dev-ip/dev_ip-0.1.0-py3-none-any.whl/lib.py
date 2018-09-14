from netifaces import interfaces, ifaddresses, AF_INET


def get_ip_addresses(loopback=False):
    addresses = []
    for name in interfaces():
        af = ifaddresses(name).get(AF_INET)
        if af:
            addresses.extend([i.get('addr') for i in ifaddresses(name).get(AF_INET)])
    if not loopback and '127.0.0.1' in addresses:
        addresses.remove('127.0.0.1')
    return addresses
