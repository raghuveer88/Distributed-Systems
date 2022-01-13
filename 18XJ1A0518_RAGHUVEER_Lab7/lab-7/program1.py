import multiprocessing
import math

def add_ten(input_array, final, mul_value):
    for i in range(len(input_array)):
        final[i] = input_array[i]+10

    mul_value.value = math.prod(final)
    print("In process1 final values are - ",final[:])

    print("multiplication of all numbers in the final array in process1 - ",mul_value.value)




if __name__ == "__main__":
	input_list = [5,6,7,8,9]
	final = multiprocessing.Array('i', 5)
	mul_value = multiprocessing.Value('i')
	process1 = multiprocessing.Process(target=add_ten, args=(input_list, final, mul_value))
	process1.start()
	process1.join()
	print("In main program final values are - ",final[:])
	print("multiplication of all numbers in main program - ",mul_value.value)
