import socket,time,os,_thread



HOST = '127.0.0.1'
PORT = 5000
t = {"count":0}
usernames = []
relatations = {}
addr = (HOST,PORT)

    

def connection(relate, person,number):
    for re in relatations.keys():    
        relatations[re].sendall(f"New person joined the room {person}.\nPresently active persons:{[x for x in usernames]}".encode())
    sent_user = ''
    sent_message = ''
    while True:
        store = relate.recv(1024).decode()
        if not store: break
        if store == "exit":
            del relatations[person]
            usernames.remove(person)
            for re in relatations.keys():    
                relatations[re].sendall(f"{person} has left the room.\nPresently active persons:{[x for x in usernames]}".encode())
        if store == "/update":
            relate.sendall(f"Presently active persons:{[x for x in usernames]}".encode())
        store = store.split('-')
        sent_user = "User" + store[0]
        sent_message = f"User{number}: {store[1]}".encode()
        relatations[sent_user].sendall(sent_message)
        print(f"{sent_message.decode()} \n>")

    relate.close()

    

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen(5)
print("waiting for a client...")

while True:
    connect, addresses = server.accept()
    print(f"{addresses} is now connected at {HOST}")
    name = "User" + str(t["count"])
    usernames.append(name)
    relatations[name] = connect
    _thread.start_new_thread(connection, (connect,name,t["count"], ))
    t["count"] = t["count"] + 1
    

server.close()