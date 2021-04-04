"""
Module:
mat_inverse.py

This module finds the inverse of a matrix by the Gauss-Jordan method
"""


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


def mat_inv(in_mat):
    """
    This function returns the a matrix invers through elementary row operations

    :param in_mat: list of lists i.e., a matrix
    :return: list of lists, i.e. a matrix
    """

    # implement me
    pass
