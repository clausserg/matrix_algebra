"""
Module:
mat_det.py

This module contains functions to calculate the determinant of any given NxN
matrix, i.e. a python list of lists. The implementation here is brute-force,
using the Leibniz formula and following the steps taught in school. The approach
is simple, given a sq. matrix A(NxN), get layers of (-1)^{i+j} * a_{ij} factors
times the determinant of a sub_A(N-1 x N-1) resulted from the elimination of the
ith row and jth column, until the aub_A matrix is 1x1 dimension. Store the factors
for each iteration then proceed in adding and/or multiplying them to get the determinant.


Do not use this to calculate the determinant of a very large matrix, for that
I will implement a LU decomposition approach.
"""

import copy


def sub_mat(in_mat, my_row, my_col):
    """
    This function returns a sub-matrix of 'my_mat', by eliminating the
    'my_row' and 'my_col' elements.

    :param in_mat: list of lists i.e., a matrix
    :param my_row: int
    :param my_col: int
    :return: list of lists, i.e. a matrix
    """

    # use deepcopy to leave untouched the original matrix
    my_mat = copy.deepcopy(in_mat)

    my_mat.pop(my_row)  # remove the my_row first
    [col.pop(my_col) for col in my_mat]  # remove the my_col column

    return my_mat


def get_mat(in_mat):
    """
    This function generates a list of factors and a list of sub-matrices from in_mat

    :param in_mat: list of lists, one matrix or a list of matrices
    :return: tuple, list of pre-factors and list of sub-matrices
    """
    # holds (N-1)x(N-1) sub-matrices from a NxN matrix by eliminating 'ith' rows and 'jth' cols.
    mat_out = []
    # holds the factors attached to the sub-matrices: (-1)^{i+j} * a_{ij}
    fact_out = []

    for mat in in_mat:  # iterate through input matrices in in_mat
        for idx in range(len(mat)):  # iterate through 1st row of this matrix
            for jdx in range(len(mat[0])):  # iterate through all columns of this matrix
                fact = mat[idx][jdx] * (-1)**(idx+jdx)  # get the pre-factor
                fact_out.append(fact)  # store the pre-factor
                mat_out.append(sub_mat(mat, idx, jdx))  # store sub-matrix associated with the stored pre-factor
            break  # we don't need to iterate for other rows in this matrix, go to next matrix or return
    return fact_out, mat_out


def mat_det(in_mat):
    """
    This function returns a matrix determinant using Leibniz formula

    :param in_mat: list of lists, i.e. a matrix
    :return: float or int, matrix determinant
    """
    
    # check if operation can be done
    if len(in_mat) == len(in_mat[0]):  # this is not a square matrix
        print("The matrix determinant is:")
        pass
    else:
        return "You cannot calculate the determinant of this matrix!\n" \
               "The matrix must be a square matrix!\n"

    # define some miscellaneous
    factors = {}  # dictionary with iteration count as key and list of factors as values
    iter_count = 0  # iteration count, getting from a NxN matrix to a 1x1 matrix
    # we store the in_mat in a list for a easier initial call to get_mat
    user_mat = [in_mat]

    while iter_count < len(in_mat):  # e.g. given a 4x4 matrix, takes exactly 3 steps to get to 1x1
        iter_count += 1
        iter_fact, iter_mat = get_mat(user_mat)
        factors[str(iter_count)] = iter_fact  # store the factors at each iteration
        user_mat = iter_mat  # update user_mat

    # bottom-up product and summation to get the determinant
    my_det = [1 for x in range(len(factors[str(len(in_mat))]))]
    # we go through the dictionary layers in descending order
    for layer in range(len(in_mat), 0, -1):
        ratio = len(my_det) // len(factors[str(layer)])  # e.g. these ratio's will be 1, 2, 3 for a 4x4 matrix and so on
        if ratio == 1:  # we do the element-by-element product of the factors list into the determinant list
            my_det = [x[0]*x[1] for x in zip(my_det, factors[str(layer)])]
        elif 1 < ratio <= len(in_mat)-1:
            # sum elements in my_det according to the ratio
            my_det = [sum(my_det[x:x+ratio]) for x in range(len(my_det)) if x % ratio == 0]
            # carry out the product with next layer
            my_det = [x[0] * x[1] for x in zip(my_det, factors[str(layer)])]
    return sum(my_det)

