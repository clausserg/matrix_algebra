from functools import reduce


def mat_lu(in_mat):
    """
    This functions
    :param in_mat:
    :return:
    """
    upper_mat = [[0.0 for idx in range(len(in_mat))] for idx in range(len(in_mat))]
    lower_mat = [[0.0 for idx in range(len(in_mat))] for idx in range(len(in_mat))]

    # zero the first column w.r.t. first row
    for idx in range(len(in_mat)):
        for jdx in range(len(in_mat[0])):
            if idx >= 1:
                factor = (-1) * in_mat[idx][0] * (1/in_mat[0][0])
                upper_mat[idx][jdx] = in_mat[idx][jdx] + factor * in_mat[0][jdx]
                lower_mat[idx][0] = (-1) * factor
            else:
                upper_mat[idx][jdx] = in_mat[idx][jdx]

    # zero lines
    for idx in range(len(upper_mat)):
        ref_line_count = -1
        for jdx in range(len(upper_mat[0])):
            ref_line_count += 1
            if idx >= 2 and 1 <= jdx < idx:
                factor = (-1) * upper_mat[idx][jdx] * (1 / upper_mat[ref_line_count][jdx])
                upper_mat[idx][jdx] = upper_mat[idx][jdx] + factor * upper_mat[ref_line_count][jdx]
                lower_mat[idx][jdx] = (-1) * factor
                for zdx in range(jdx+1, len(in_mat[0])):
                    upper_mat[idx][zdx] = upper_mat[idx][zdx] + factor * upper_mat[ref_line_count][zdx]

    upper_main_diagonal = [upper_mat[idx][idx] for idx in range(len(upper_mat))]
    my_det = reduce((lambda x, y: x * y), upper_main_diagonal)

    # return the upper and lower triangular matrices
    return upper_mat, lower_mat, my_det


# my_mat = [[1, 2, 3, 6, 2], [4, 2, 1, 7, 3], [6, 3, 2, 5, 5], [8, 3, 1, 7, 3], [3, 8, 2, 3, 2]]

