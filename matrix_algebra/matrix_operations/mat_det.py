"""
Module:
mat_det.py

This module contains functions to calculate the determinant of any given NxN matrix.
Matrix here is a python list of lists.
"""

import copy


def sub_mat(in_mat, my_row, my_col):
    """
    This function returns a sub-matrix of 'my_mat', by eliminating the
    'my_row' and 'my_col' elements.

    :param in_mat: a list of lists i.e., a matrix
    :param my_row: int
    :param my_col: int
    :return: list of lists, i.e. a matrix
    """

    # use deepcopy to leave untouched the original matrix
    my_mat = copy.deepcopy(in_mat)

    trash_row = my_mat.pop(my_row)  # remove the my_row first
    trash_col = [col.pop(my_col) for col in my_mat]  # remove the my_col column

    return my_mat


def get_mat(in_mat):
    """
    This function generates a list of factors and a list of sub-matrices

    :param in_mat: python list of lists, one or a list of them
    :return: tuple, list of pre-factors and list of sub-matrices
    """

    mat_out = []  # holds (N-1)x(N-1) sub-matrices from a NxN matrix by eliminating 'ith' row and 'jth' col.
    fact_out = []  # holds the factors attached to the sub-matrices: (-1)^{i+j} * a_{ij}

    for mat in in_mat:  # iterate through input matrices
        for idx in range(len(mat)):  # iterate through rows of this matrix
            for jdx in range(len(mat[0])):  # iterate through all columns of this matrix
                fact = mat[idx][jdx] * (-1)**(idx+jdx)  # calculates the pre-factor of element a_{ij}
                fact_out.append(fact)  # store factor for output
                mat_out.append(sub_mat(mat, idx, jdx))  # store sub-matrix for output
            break  # we don't need to iterate for other rows in this matrix, go to next one or return
    return fact_out, mat_out


def mat_det(in_mat):
    """
    This function returns a matrix determinant using Leibniz formula

    :param in_mat: list of lists, i.e. a matrix
    :return: float, matrix determinant
    """

    # define some miscellaneous
    factors = {}  # dictionary holding factors
    iter_count = 0  # iteration count for getting from a NxN matrix to a 1x1 matrix

    user_mat = [in_mat]  # we store the in_mat in a list for a easier call to get_mat
    while iter_count < len(in_mat):
        iter_count += 1
        iter_fact, iter_mat = get_mat(user_mat)
        factors[str(iter_count)] = iter_fact  # store the factors at each iteration
        user_mat = iter_mat

    # bottom-up product and summation to get the determinant
    my_det = [1 for x in range(len(factors[str(len(in_mat))]))]
    # we go through the dictionary layers in descending order
    for layer in range(len(in_mat), 0, -1):
        ratio = len(my_det) // len(factors[str(layer)])
        if ratio == 1:
            my_det = [x[0]*x[1] for x in zip(my_det, factors[str(layer)])]
        elif 1 < ratio <= len(in_mat)-1:
            # sum elements in my_det according to the ratio
            my_det = [sum(my_det[x:x+ratio]) for x in range(len(my_det)) if x % ratio == 0]
            # carry out the product with next layer
            my_det = [x[0] * x[1] for x in zip(my_det, factors[str(layer)])]
    return sum(my_det)

