import socket
import sys
import struct

multi_cast_members = '224.3.29.71'
port = 10000
serve_addr = ('', port) 
socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    try:
        socks.bind(serve_addr)
        break
    except:
        port = port + 1
        serve_addr = ('', port)
        continue


members = socket.inet_aton(multi_cast_members)

re = struct.pack('4sL', members, socket.INADDR_ANY)

socks.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP, re)

while True:
    print('\n waiting to receive message')
    data, port = socks.recvfrom(1024)
    print('received %s bytes from %s' % (len(data), port))
    print(data)
    print('sending acknowledgement (ack) to', port)
    socks.sendto(b'ack', port)