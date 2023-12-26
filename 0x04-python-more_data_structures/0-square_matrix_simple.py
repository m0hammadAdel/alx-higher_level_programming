#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda one_d_list: list(map(lambda x: x ** 2), one_d_list)), matrix)
