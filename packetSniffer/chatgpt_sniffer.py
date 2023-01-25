from scapy.all import *

def packet_callback(packet):
    print(packet.show())

sniff(prn=packet_callback, count=1)

sniff(filter="tcp and host 192.168.1.1", prn=packet_callback, count=1)
