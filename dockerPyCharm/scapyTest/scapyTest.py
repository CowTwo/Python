"""
Test myMBSSID packet
Mapping to Packet #1 of Network_Join_Nokia_Mobile.pcap
"""
from scapy.all import *

dot11 = Dot11(type='Management', subtype=8, addr1='ff:ff:ff:ff:ff:ff',
addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33', SC=0xf010)
# Fixed IE in beacon (timestamp, beacon_interval, cap)
beacon = Dot11Beacon(timestamp=0x00000002691a2184, cap='ESS+privacy+short-slot')
# TLV IE in beacon
netSSID="martinet3"
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))
supRates=Dot11Elt(ID='Rates', info=(
'\x82\x84\x8b\x96\x24\x30\x48\x6c'
))
dsSetIe=Dot11Elt(ID='DSset', info=(
'\x0b'
))
timIe=Dot11Elt(ID='TIM', info=(
'\x00\x01\x00\x00'
))
erpIe1=Dot11Elt(ID=0x2a, info=(
'\x04'
))
erpIe2=Dot11Elt(ID=0x2f, info=(
'\x04'
))
esRateIe=Dot11Elt(ID='ESRates', info=(
'\x0c\x12\x18\x60'
))

frame = dot11/beacon/essid/supRates/dsSetIe/timIe/erpIe1/erpIe2/esRateIe
frame.show()
hexdump(frame)

# Write frame to PCAP file
pktdump = PcapWriter("./banana.pcap", append=False, sync=True)
pktdump.write(frame)
beacon = Dot11Beacon(timestamp=(0x00000002691a2184+100), cap='ESS+privacy+short-slot')
frame = dot11/beacon/essid/supRates/dsSetIe/timIe/erpIe1/erpIe2/esRateIe
pktdump.write(frame)