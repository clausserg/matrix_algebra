"""
Unit and regression test for the matrix_algebra package.
"""


# Import package, test suite, and other packages as needed
from matrix_algebra.matrix_operations.mat_add import *
from matrix_algebra.matrix_operations.mat_diff import *
from matrix_algebra.matrix_operations.mat_mul import *
from matrix_algebra.matrix_operations.mat_det import *


def test_mat_add():
    """Test that the mat_add() function returns correctly"""

    mat_1 = [[1, 2], [3, 4]]
    mat_2 = [[1, 2], [3, 4]]

    expected_sum = [[2, 4], [6, 8]]
    calculated_sum = mat_add(mat_1, mat_2)

    assert calculated_sum == expected_sum


def test_mat_diff():
    """Test that the mat_diff() function returns correctly"""

    mat_1 = [[1, 2], [3, 4]]
    mat_2 = [[1, 2], [3, 4]]

    expected_diff = [[0, 0], [0, 0]]
    calculated_diff = mat_diff(mat_1, mat_2)

    assert calculated_diff == expected_diff


def test_mat_mul():
    """Test that the mat_mul() function returns correctly"""

    mat_1 = [[1, 2], [3, 4]]
    mat_2 = [[1, 2], [3, 4]]

    expected_mul = [[7, 10], [15, 22]]
    calculated_mul = mat_mul(mat_1, mat_2)

    assert calculated_mul == expected_mul


def test_det_tt():
    """Test that the det_tt() function returns correctly"""

    my_mat = [[1, 2], [3, 4]]

    expected_det = -2
    calculated_det = det_tt(my_mat)

    assert calculated_det == expected_det


def test_sub_mat():
    """Test that the sub_mat() function returns correctly"""

    my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    expected_mat = [[1, 2], [4, 5]]
    calculated_mat = sub_mat(my_mat, 2, 2)

    assert calculated_mat == expected_mat

