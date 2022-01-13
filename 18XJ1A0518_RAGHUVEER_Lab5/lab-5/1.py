from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
process_number = comm.Get_rank()

# print("process_number is {}".format(process_number))
# print("size is {}".format(size))

if process_number == 0:
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    final_list = []
    for i in range(len(matrix1)):
        f = 0
        if(i+1) % (size-1) == 0:
            f = size-1
        else:
            f = (i+1) % (size-1)
        comm.send(matrix1[i], dest=f, tag=1)
        comm.send(matrix2[i], dest=f, tag=2)
        print("sent data of the matrix")

        final_list.append(comm.recv(source=f, tag=3))
    print("final_matrix= ", final_list)

else:
    row1 = comm.recv(source=0, tag=1)
    row2 = comm.recv(source=0, tag=2)
    print("process_number or rank = ", process_number)
    print("row1= ", row1)
    print("row2= ", row2)

    temp = []
    for k in range(len(row1)):
        temp.append(row1[k]+row2[k])

    comm.send(temp, dest=0, tag=3)
