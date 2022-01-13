from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# print("rank is {}".format(rank))
# print("size is {}".format(size))

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = comm.bcast(matrix2, root=0)

if rank == 0:
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix2 = [[1, 2], [4, 5]]

    final_result = []
    for i in range(len(matrix1)):
        d = 0
        if(i+1) % (size-1) == 0:
            d = size-1
        else:
            d = (i+1) % (size-1)
        comm.send(matrix1[i], dest=d, tag=1)
        # comm.send(matrix2, dest=d, tag=2)

        print("matrix data sent")

        final_result.append(comm.recv(source=d, tag=3))
    print("final_matrix= ", final_result)

else:
    part1 = comm.recv(source=0, tag=1)
    # part2 = comm.recv(source=0, tag=2)
    print("rank = ", rank)
    print("p1= ", part1)
    print("broadcast= ", matrix2)

    temp = []
    if (rank == 1):
        for i in range(len(part1)):
            a = 0
            for j in range(len(matrix2)):
                a = a + part1[j] * matrix2[j][i]
            temp.append(a)
        # a = part1[0] * matrix2[0][0]
        # b = part1[1] * matrix2[1][0]
        # g = part1[2] * matrix2[2][0]
        # temp.append(a+b+g)
        # c = part1[0] * matrix2[0][1]
        # e = part1[1] * matrix2[1][1]
        # h = part1[1] * matrix2[2][1]
        # temp.append(c+e+h)
    if (rank == 2):
        for i in range(len(part1)):
            a = 0
            for j in range(len(matrix2)):
                a = a + part1[j] * matrix2[j][i]
            temp.append(a)
        # a = part1[0] * matrix2[0][0]
        # b = part1[1] * matrix2[1][0]
        # temp.append(a+b)
        # c = part1[0] * matrix2[0][1]
        # e = part1[1] * matrix2[1][1]
        # temp.append(c+e)

    if (rank == 3):
        for i in range(len(part1)):
            a = 0
            for j in range(len(matrix2)):
                a = a + part1[j] * matrix2[j][i]
            temp.append(a)

    # for k in range(len(part1)):
    #     temp.append(part1[k]+part2[k])

    comm.send(temp, dest=0, tag=3)
