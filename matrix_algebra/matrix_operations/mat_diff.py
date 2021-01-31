"""
Module:
mat_diff.py

This module contains a function that adds two  matrices
represented as python list of lists.
"""


def mat_diff(mat_a, mat_b):
    """
    Function that subtracts two matrices: mat_a and mat_b. The
    subtraction can be carried out if the two matrices have same
    dimension, i.e. same number of rows and columns. The elements of
    the resulting matrix, mat_c, are c_ij = a_ij - b_ij

    :param mat_a: list of lists with user defined a_ij elements
    :param mat_b: list of lists with user defined b_ij elements
    :return: mat_c = mat_a - mat_b, list of lists with elements c_ij = a_ij - b_ij
    """

    # check if operation can be done
    if len(mat_a) == len(mat_b) and len(mat_a[0]) == len(mat_b[0]):
        print("The subtraction of the two matrices is:")
        pass
    else:
        return "You cannot subtract these matrices! They need to have same dimensions!\n"

    # contain number of rows and columns
    nr_rows = len(mat_a)
    nr_cols = len(mat_a[0])

    # initialize the resulting mat_c
    mat_c = [[0.0 for idx in range(nr_cols)] for jdx in range(nr_rows)]

    # update elements of mat_c: c_ij = a_ij + b_ij
    for row in range(nr_rows):
        mat_c[row] = [(elements[0]-elements[1]) for elements in zip(mat_a[row], mat_b[row])]
    return mat_c

