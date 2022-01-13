import socket


HOST = '127.0.0.1'
PORT = 3000
Addr = (HOST, PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# client.connect(Addr)
client.sendto(b'hello this is UDP echo client and server program',Addr)
data = client.recvfrom(1024)
client.close()
print("recived data from server is ",data[0])