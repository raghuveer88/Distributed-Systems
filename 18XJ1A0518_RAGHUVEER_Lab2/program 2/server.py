import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

# for starting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print("Running on host: ",HOST)
print("Running on port: ",PORT)
# server listening
server.listen()

# two arrays for storing clients and there usernames
usernames = []
persons = []

def sendMsgAll(msg):    #this funtio is to send message to all the clients 
    for person in persons:
        person.send(msg)



def control(person): # To control the messages
    while True:
        try:
            msg = person.recv(1024)     #message recived from the client    
            # i = persons.index(person)
            # username = usernames[i]
            print("new message {}".format((msg).decode()))  #messge displayed on the server terminal
            sendMsgAll(msg) # send message to all the clients
        except:
            i = persons.index(person)     #this exception case is for removing both person and username from the respective array to maintain the indexes
            persons.remove(person)
            person.close()
            username = usernames[i]
            sendMsgAll("{} has left".format(username).encode())  #send to all the clients that someone exitted from the chat
            usernames.remove(username)
            break


def run():  #this is continetion to the main funtion
    while True:
        person, address = server.accept()    #server to accept the client
        person.send('USER'.encode())        
        username = person.recv(1024).decode()
        usernames.append(username)  #adding new users to the list
        persons.append(person)      #adding new clients to the list
        print("New Connection Username: ",username)
        sendMsgAll("New person joined the room {}".format(username).encode())  #sendign the msg to everyone that someone new joined the chat

        new_thread = threading.Thread(target=control, args=(person,)) #creating threads
        new_thread.start()


run()