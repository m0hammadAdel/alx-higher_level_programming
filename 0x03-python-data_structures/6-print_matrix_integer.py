#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for sub_mat in matrix:
        if len(sub_mat) == 0:
            print()

        for i in range(len(sub_mat)):
            print("{:d}".format(sub_mat[i]),
                  end='\n' if i is len(sub_mat) - 1 else ' ')

#    for i in range(len(matrix)):
#        for j in range(len(matrix[i])):
#            print("{:d}".format(matrix[i][j]), end=' ')
#        print()
