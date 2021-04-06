"""
Module:
mat_inverse.py

This module finds the inverse of a matrix by the Gauss-Jordan method
"""

from copy import deepcopy


def swap_rows(mat_in, row_a,  row_b):
    """
    This function swaps a matrix row with another row.

    :param mat_in: list of lists, i.e. a matrix
    :param row: int
    :param col: int
    :return: list of lists, i.e. a matrix
    """

    mat_in[row_a], mat_in[row_b] = mat_in[row_b], mat_in[row_a]
    return mat_in


def pivot(mat_in, row_idx,  col_idx):
    """
    This function creates pivot in a given row/col position of the input matrix

    :param mat_in: list of lists, i.e. a matrix
    :param row_idx: int
    :param col_idx: int
    :return: list of lists, i.e. a matrix
    """

    mat_in[row_idx] = [x/mat_in[row_idx][col_idx] for x in mat_in[row_idx]]
    return mat_in


def row_operation(mat_in, rows, scalar, operation):
    """
    This function performs an operation involving one or two rows of a matrix.

    :param rows: list, one or two row indexes
    :param scalar: int or float
    :param operation: char
    :return: list of lists, i.e. a matrix
    """

    # work with a deepcopy of the input matrix
    new_mat = deepcopy(mat_in)

    # alter a row by a scalar if only one row index is given
    if len(rows) == 1 and operation == '*':
        new_mat[rows[0]] = [idx / scalar for idx in mat_in[rows[0]]]

    # alter a row by a scalar and add/subtract it to/from another row if two row indexes are given
    if len(rows) == 2 and operation == "+":
        new_mat[rows[1]] = list(map(lambda x, y: scalar*x + y, mat_in[rows[1]], mat_in[rows[0]]))
    elif len(rows) == 2 and operation == "-":
        new_mat[rows[1]] = list(map(lambda x, y: scalar*x - y, mat_in[rows[1]], mat_in[rows[0]]))

    # return the altered matrix
    return new_mat


def mat_inv(in_mat):
    """
    This function returns the a matrix invers through elementary row operations

    :param in_mat: list of lists i.e., a matrix
    :return: list of lists, i.e. a matrix
    """

    # define miscellaneous
    nr_rows = len(in_mat)
    nr_cols = len(in_mat[0])

    # initialize the matrix inverse as an identity matrix with dimension of the original matrix
    # used to build the augmented matrix
    my_inv = [[1 if idx==jdx else 0 for idx in range(nr_rows)] for jdx in range(nr_cols)]
    pass


# my_mat = [[3, 1, 2], [2, 0, -2], [0, 1, 1]]
# nr_rows = len(my_mat)
# nr_cols = len(my_mat[0])
#
# abc = pivot(my_mat, 0, 0)
# print(abc)
