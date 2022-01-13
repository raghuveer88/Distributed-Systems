import socket


HOST = '127.0.0.1'
PORT = 3000
Addr = (HOST,PORT)

print("server starting")
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(Addr)
# server.listen()
print('UDP server listening')
# conn,addr = server.accept()
# print('connected by', addr)
while True:
    data = server.recvfrom(1024)
    if not data:
        break
    msg = data[0]
    addr = data[1]
    print("Data recived from the client is ",msg)
    print("client address is ",addr)
    server.sendto(msg,addr)
server.close
# print(f"disconnected {addr}")