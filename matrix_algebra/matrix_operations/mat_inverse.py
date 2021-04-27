"""
Module:
mat_inverse.py

This module finds the inverse of a matrix by the Gauss-Jordan method
"""

from copy import deepcopy
from mat_lu import swap_rows


def pivot(mat_in, idx):
    """
    This function transforms the elements in a row of matrix such as to create
    a pivot, i.e. a unit matrix elemnt, in a specified index position along the
    main diagonal.

    :param mat_in: list of lists, i.e. a matrix
    :param idx: int
    :return: list of lists, i.e. a matrix
    """

    mat_in[idx] = [x/mat_in[idx][idx] for x in mat_in[idx]]
    return mat_in


def row_operation(mat_in, rows, scalar):
    """
    This function performs an operation involving one or two rows of a matrix.

    :param rows: list, one or two row indexes
    :param scalar: int or float
    :param operation: char
    :return: list of lists, i.e. a matrix
    """

    # work with a deepcopy of the input matrix
    new_mat = deepcopy(mat_in)

    if len(rows) == 1:
        # alter a row by a scalar if only one row index is given
        new_mat[rows[0]] = [idx * scalar for idx in mat_in[rows[0]]]
    else:
        # alter a row by a scalar and add/subtract it to/from another row
        # addition vs. substraction will be defined by the sign of the scalar
        new_mat[rows[1]] = list(map(lambda x, y: scalar*x + y, mat_in[rows[0]], mat_in[rows[1]]))

    # return matrix with the altered row(s)
    return new_mat


def mat_inv(in_mat):
    """
    This function returns the a matrix inverse by Gauss-Jordan approach

    :param in_mat: list of lists i.e., a matrix
    :return: list of lists, i.e. a matrix inverse
    """

    # define miscellaneous
    nr_rows = len(in_mat)
    nr_cols = len(in_mat[0])

    # initialize the matrix inverse as an identity matrix
    # used to build the augmented matrix
    my_inv = [[1 if idx==jdx else 0 for idx in range(nr_rows)] for jdx in range(nr_cols)]

    # transform the input matrix in the augmented matrix to work with
    [in_mat[row].extend(my_inv[row]) for row in range(nr_rows)]

    for col in range(nr_cols):
        # swap rows if zero prevents making the pivot
        in_mat = swap_rows(in_mat, col, col)[0]
        # make pivot
        in_mat = pivot(in_mat, col)
        # eliminate the column
        for row in range(nr_rows):
            if row == col:
                continue  # skip the row with the pivot
            else:
                in_mat = row_operation(in_mat, [col, row], (-1) * in_mat[row][col])

    # return the final inverse matrix
    inverse = [[in_mat[row][col] for row in range(nr_rows)] for col in range(nr_cols+1, 2*nr_cols)]
    return inverse
