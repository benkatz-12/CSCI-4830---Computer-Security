from scapy.all import *
import sys

pcap = sys.argv[1]
IP_SYN_SYN_ACK = dict()
packets = PcapReader(pcap)

for packet in packets:
    if(packet.haslayer('Ether') & packet.haslayer('IP') & packet.haslayer('TCP')):
        if(packet.getlayer('TCP').getfieldval('flags').value == 2):
            if(packet.getlayer('IP').getfieldval('src') not in IP_SYN_SYN_ACK):
                new_entry = {packet.getlayer('IP').getfieldval('src') : [1,0]}
                IP_SYN_SYN_ACK.update(new_entry)
            else:
                IP_SYN_SYN_ACK[packet.getlayer('IP').getfieldval('src')][0]+=1
        elif(packet.getlayer('TCP').getfieldval('flags').value == 18):
            if(packet.getlayer('IP').getfieldval('dst') not in IP_SYN_SYN_ACK):
                new_entry = {packet.getlayer('IP').getfieldval('dst') : [0,1]}
                IP_SYN_SYN_ACK.update(new_entry)
            else:
                IP_SYN_SYN_ACK[packet.getlayer('IP').getfieldval('dst')][1]+=1
new_dict = dict(filter(lambda elem: elem[1][0] >= 3*elem[1][1], IP_SYN_SYN_ACK.items()))
for a in new_dict.keys():
    print(a)