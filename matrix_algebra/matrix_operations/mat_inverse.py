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
    if len(rows) == 1 and operation == '/':
        new_mat[rows[0]] = [idx / scalar for idx in mat_in[rows[0]]]
        return new_mat
    elif len(rows) == 1 and operation == '*':
        new_mat[rows[0]] = [idx * scalar for idx in mat_in[rows[0]]]
        return new_mat

    # alter a row by a scalar and add/subtract it to/from another row if two row indexes are given
    if len(rows) == 2 and operation == "+":
        new_mat[rows[1]] = list(map(lambda x, y: scalar*x + y, mat_in[rows[1]], mat_in[rows[0]]))
        return new_mat
    elif len(rows) == 2 and operation == "-":
        new_mat[rows[1]] = list(map(lambda x, y: scalar*x - y, mat_in[rows[1]], mat_in[rows[0]]))
        return new_mat


def mat_inv(in_mat):
    """
    This function returns the a matrix invers through elementary row operations

    :param in_mat: list of lists i.e., a matrix
    :return: list of lists, i.e. a matrix
    """

    # implement me
    pass
