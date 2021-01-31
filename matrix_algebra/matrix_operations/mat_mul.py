"""
Module:
mat_mul.py

This module contains a function that multiplies two matrices,
represented as python list of lists.
"""


def mat_mul(mat_a, mat_b):
    """
    Function that multiplies two matrices, mat_a and mat_b. Each entry of
    the resulting matrix, mat_c, is a "dot-product" of a row of mat_a with
    a column of mat_b, i.e. C_{ij} = Sum_{k} A_{ik} * B_{kj}, where index
    {i} iterates through rows of mat_a, index {j} iterates through columns
    of mat_b, and pivot index {k} iterates through columns/rows of mat_a/mat_b.

    :param mat_a: list of lists with user defined a_ij elements
    :param mat_b: list of lists with user defined b_ij elements
    :return: mat_c = mat_a x mat_b, a list of lists with c_{ij} = Sum_{k} a_{ik} * b_{kj} elements
    """

    # check if operation can be done
    if len(mat_a[0]) == len(mat_b):
        print("The product of the two matrices is:")
        pass
    else:
        return "You cannot multiply these matrices!\n" \
               "The number of columns in first matrix should equal " \
               "the number of rows in second matrix!\n"

    # the number of rows in matrix mat_c equals the number of rows in mat_a
    # the number of columns in matrix mat_c equals the number of columns in mat_b
    mat_c_row = len(mat_a)
    mat_c_col = len(mat_b[0])

    # initialize mat_c with zeroes
    mat_c = [[0 for idx in range(mat_c_col)] for jdx in range(mat_c_row)]

    for idx in range(mat_c_row):  # index going through rows of mat_c
        for jdx in range(mat_c_col):  # index going through columns of mat_c
            for kdx in range(len(mat_a[0])):  # index going through columns/rows of mat_a/mat_b
                mat_c[idx][jdx] += (mat_a[idx][kdx] * mat_b[kdx][jdx])
    return mat_c

