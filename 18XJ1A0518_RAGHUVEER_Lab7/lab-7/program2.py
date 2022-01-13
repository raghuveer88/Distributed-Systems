import multiprocessing

def add_ten(input_list, que):
    for i in input_list:
        number = i + 10
        que.put(number)

def que_print(que):
	print("The elements in the queue are :")
	while not que.empty():
		print(que.get())
	print("All the elements are popped. Queue is empty now")

if __name__ == "__main__":
	input_list = [5,6,7,8,9]
	que = multiprocessing.Queue()
	process1 = multiprocessing.Process(target=add_ten, args=(input_list, que))
	process2 = multiprocessing.Process(target=que_print, args=(que,))
	process1.start()
	process1.join()
	process2.start()
	process2.join()
