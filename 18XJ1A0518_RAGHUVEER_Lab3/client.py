import socket,time,os,_thread


PORT = 5000
HOST = '127.0.0.1'

ADDR = (HOST,PORT)  

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(ADDR) 

def message_sever():
    while True:
            message = user.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)

_thread.start_new_thread(message_sever, ( ))
print("Format to select a person is by the number of the person seperated by '-' EX- 1-hello\n")
print("to quit enter exit\n")
while True:
    
    message = input()
    user.sendall(message.encode())
    if message == "exit":
        quit()

