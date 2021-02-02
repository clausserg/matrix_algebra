"""
Module:
mat_det.py

This module contains a function that calculates the determinant of a matrix
represented as python list of lists.
"""

import copy


def det_tt(my_mat):
    """
    This function implements the determinant of a 2x2 matrix given by the Leibniz formula, i.e.
    the difference between the product of the main diagonal elements and
    the product of the second diagonal elements.

    :return: float, determinant of a two-by-two matrix
    """
    return my_mat[0][0] * my_mat[1][1] - my_mat[0][1] * my_mat[1][0]


def sub_mat(in_mat, my_row, my_col):
    """
    This function returns a sub-matrix of 'my_mat' resulting from the
    elimination of the 'my_row' and 'my_col' elements.

    :param my_mat: a list of lists i.e., a matrix
    :param my_row: int, the row of 'my_mat' to be eliminated
    :param my_col: int, the column of 'my_mat' to be eliminated
    :return: a python list of lists
    """

    my_mat = copy.deepcopy(in_mat)
    trash_row = my_mat.pop(my_row)  # remove the my_row first
    trash_col = [col.pop(my_col) for col in my_mat]  # remove the column

    return my_mat

