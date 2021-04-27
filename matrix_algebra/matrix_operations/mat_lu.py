"""
Module:
mat_lu.py

This module implements functions needed  to perform a LU factorization
of a square matrix using Gaussian elmination.
"""


from functools import reduce


def swap_rows(mat_in, row,  col):
    """
    This function swaps a matrix row with another row.
    Swaping will be done if the element at the position specified by the user
    via the 'row' and 'col' variables, is zero. Swaping occurs with a row that
    has a non-zero element in the same 'col'. If all rows contain a
    zero at the 'row', 'col' position, the original input matrix is returned.

    :param mat_in: list of lists, i.e. a matrix
    :param row: int, row index in a matrix
    :param col: int, column index in a matrix
    :return: tuple, a list of lists and a multiplier that is either 1 if no
    swapping has been done, or -1 if swapping was done.
    """

    if mat_in[row][col] != 0:
        # return the original matrix if the matrix element at the
        # input [row][col] position is not zero
        multiplier = 1
        return mat_in, multiplier
    else:
        # find a row with non-zero matrix element in the same [col] position
        # and swap. If swaping is done, the matrix determinant should be multiplied
        # by -1, therefore a multiplier = -1 is returned togeteher with the matrix with
        # swapped rows.
        for idx in range(row+1, len(mat_in)):
            if mat_in[idx][col] != 0:
                mat_in[row], mat_in[idx] = mat_in[idx], mat_in[row]
                multiplier = -1
                return mat_in, multiplier
        # if the if-else block is skipped, means all rows have a zero
        # matrix element along the [col], in this case we return the original matrix
        multiplier = 1
        return mat_in, multiplier


def mat_lu(in_mat):
    """
    This functions perform a LU factorization of a square matrix using
    Gaussian elmination. It is also returning the matrix determinant.

    :param in_mat: list of lists, i.e. a matrix
    :return: tuple of U, L, and matrix determinant; U is the upper
    triangular matrix and L is the lower triangular matrix.
    """

    # initialize wiht zeroes the L and U matrices
    upper_mat = [[0.0 for idx in range(len(in_mat))] for idx in range(len(in_mat))]
    lower_mat = [[0.0 for idx in range(len(in_mat))] for idx in range(len(in_mat))]
    # initialize a container for the determinant
    my_det = 1

    # check if the input matrix contains a 0 on the first row first column.
    # if true, swap the row with another row that does not contain a 0 element
    # and alter the determinant by a (-1) factor.
    in_mat, swapped = swap_rows(in_mat, 0, 0)
    my_det *= swapped

    # we work on building the upper matrix meanwhile updating the lower matrix
    # zero the first column w.r.t. first row
    for idx in range(len(in_mat)):
        for jdx in range(len(in_mat[0])):
            if idx >= 1 and in_mat[idx][0] != 0:
                # factor to be multiplied with first row element and added to next rows
                factor = (-1) * in_mat[idx][0] * (1/in_mat[0][0])
                upper_mat[idx][jdx] = in_mat[idx][jdx] + factor * in_mat[0][jdx]
                # update the lower triangular matrix with the factor
                lower_mat[idx][0] = (-1) * factor
            else:
                # keep elements as they are
                upper_mat[idx][jdx] = in_mat[idx][jdx]

    # zero beyond the first column
    for idx in range(len(upper_mat)):
        # initialize a count for the row of reference for the elimination
        # it will always be equal to the column index, jdx, and we contain it here
        # in a 'ref_line_count' variable to keep it constant per "idx" row iteration
        ref_line_count = -1
        for jdx in range(len(upper_mat[0])):  # iterate through columns
            # increment reference row count: for col 1 will be ref row 1, etc.
            ref_line_count += 1
            # we only need to start from second row and go between column 1 and
            # below the main diagonal
            if idx >= 2 and 1 <= jdx < idx and upper_mat[idx][jdx] != 0:
                # check if reference element is zero, swap rows if true
                # and factor a (-1) in the matrix determinant
                upper_mat, swapped = swap_rows(upper_mat, ref_line_count, jdx)
                my_det *= swapped
                # calculate the factor w.r.t. the reference row counter (will always be equal to jdx=column index)
                factor = (-1) * upper_mat[idx][jdx] * (1 / upper_mat[ref_line_count][jdx])
                upper_mat[idx][jdx] = upper_mat[idx][jdx] + factor * upper_mat[ref_line_count][jdx]
                # add the factor to the L matrix
                lower_mat[idx][jdx] = (-1) * factor
                # go on and update the remainder of this row
                for zdx in range(jdx+1, len(upper_mat[0])):
                    upper_mat[idx][zdx] = upper_mat[idx][zdx] + factor * upper_mat[ref_line_count][zdx]

    upper_main_diagonal = [upper_mat[idx][idx] for idx in range(len(upper_mat))]
    my_det *= reduce((lambda x, y: x * y), upper_main_diagonal)

    # return the upper and lower triangular matrices
    return upper_mat, lower_mat, my_det
