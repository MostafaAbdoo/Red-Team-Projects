from scapy.all import *
# an ARP requests scrip
# Example of usage: python3 scanner.py eth0 192.168.1.0/24
import sys
interface = sys.argv[1]
rangee = sys.argv[2]
broadcastMac = "ff:ff:ff:ff:ff:ff"
packet =Ether(dst=broadcastMac)/ARP(pdst=rangee)
ans, unans = srp(packet,timeout=2,iface=interface,inter=0.1)
for send, recieve in ans:
    print(recieve.sprintf(r"%Ether.src% - %ARP.psrc%"))
