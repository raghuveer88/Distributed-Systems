import socket,struct,sys
message = 'TESTING MULTICAST DATA'
port = 10000
mult_cast_members = ('224.3.29.71', port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


sock.settimeout(0.2)

time_to_live = struct.pack('b', 1)

sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL, time_to_live)

while True:
    try:
        sent = sock.sendto(message.encode(),mult_cast_members)
        port = port + 1
        mult_cast_members = ('224.3.29.71', port)
        continue
    except:
        break

while True:
    try:
        data, server = sock.recvfrom(16)
        print ('received "%s" from %s' %(data, server))
        continue
    except Exception as e:
        break
print ('closing socket')
sock.close()