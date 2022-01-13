import threading
import socket


PORT = 5000     #port and host numbers of the server
HOST = '127.0.0.1'

username = input("Enter username --> ")   #take input username
ADDR = (HOST,PORT)  #making hostt and port in a tuple

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket creating
user.connect(ADDR)#connection

def run():  # this function is for server listening 
    while True:
            msg = user.recv(1024).decode()     
            if msg == 'USER':     #if the msg is user it sends the username to the server and let everyone a new person joined
                user.send(username.encode())    #encode the msg while sending to the server
            else:
                print(msg)   #prints the given message

def write():    #this function is for user writing the message
    while True:
        msg = '{} - {}'.format(username, input(''))    #take user input as message
        user.send(msg.encode())
        

thread_recived = threading.Thread(target=run)   #thread creation
thread_recived.start()    
thread_write = threading.Thread(target=write)   #thread creation
thread_write.start()