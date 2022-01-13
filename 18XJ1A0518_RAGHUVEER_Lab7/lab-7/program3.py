import multiprocessing

def sender(connection, messages):
	for message in messages:
		connection.send(message)
		print("message sent: ",message)
	connection.close()

def receiver(connection):
	while 1:
		message = connection.recv()
		if message == "Break":
			break
		print("Message Recived: ",message)

if __name__ == "__main__":
	messages = ["how are you?", "what is your name?", "what do you do?", "Break"]
	top_connection, bottom_connection = multiprocessing.Pipe()
	process1 = multiprocessing.Process(target=sender, args=(top_connection,messages))
	process2 = multiprocessing.Process(target=receiver, args=(bottom_connection,))
	process1.start()
	process2.start()
	process1.join()
	process2.join()
