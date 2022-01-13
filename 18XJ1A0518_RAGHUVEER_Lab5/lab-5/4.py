from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    input_array = np.arange(10.0)

    # determine the size of each sub-task
    b, result = divmod(input_array.size, size)
    numbers = [b + 1 if i < result else b for i in range(size)]

    # determine the starting and ending indices of each sub-task
    # begin = [sum(numbers[:i]) for p in range(size)]
    begin = []
    for i in range(size):
        begin.append(sum(numbers[:i]))

    last = []
    # last = [sum(numbers[:i+1]) for i in range(size)]
    for i in range(size):
        last.append(sum(numbers[:i+1]))

    # converts input_array into a list of arrays
    input_array = [input_array[begin[i]:last[i]] for i in range(size)]

else:
    input_array = None

input_array = comm.scatter(input_array, root=0)

print('array in Rank or process {} is'.format(rank), input_array)

sum = 0
for i in input_array:
    sum = sum+i

res = comm.gather(sum, root=0)


if rank == 0:
    print('Gathering the sums of each processors and the result is {}'.format(res))
