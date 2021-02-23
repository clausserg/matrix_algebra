"""
Unit and regression test for the matrix_algebra package.
"""


# Import package, test suite, and other packages as needed
import numpy as np
from matrix_algebra.matrix_operations.mat_add import *
from matrix_algebra.matrix_operations.mat_diff import *
from matrix_algebra.matrix_operations.mat_mul import *
from matrix_algebra.matrix_operations.mat_det import *
from matrix_algebra.matrix_operations.mat_lu import *


def test_mat_add():
    """Test that the mat_add() function returns correctly"""
    mat_1 = np.array([[1, 2], [3, 4]])
    mat_2 = np.array([[1, 2], [3, 4]])
    expected_sum = np.add(mat_1, mat_2)
    calculated_sum = np.array(mat_add(mat_1, mat_2))
    assert (calculated_sum - expected_sum).any() == False


def test_mat_diff():
    """Test that the mat_diff() function returns correctly"""
    mat_1 = np.array([[1, 2], [3, 4]])
    mat_2 = np.array([[1, 2], [3, 4]])
    expected_diff = np.subtract(mat_1, mat_2)
    calculated_diff = np.array(mat_diff(mat_1, mat_2))
    assert (calculated_diff - expected_diff).any() == False


def test_mat_mul():
    """Test that the mat_mul() function returns correctly"""
    mat_1 = np.array([[1, 2], [3, 4]])
    mat_2 = np.array([[1, 2], [3, 4]])
    expected_mul = np.matmul(mat_1, mat_2)
    calculated_mul = np.array(mat_mul(mat_1, mat_2))
    assert (calculated_mul - expected_mul).any() == False


def test_sub_mat():
    """Test that the sub_mat() function returns correctly"""
    my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_mat = [[1, 2], [4, 5]]
    calculated_mat = sub_mat(my_mat, 2, 2)
    assert calculated_mat == expected_mat


def test_get_mat():
    """Test that the get_mat() function returns correctly"""
    my_mat = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected_facts = [1, -2, 3]
    expected_mats = [[[5, 6], [8, 9]], [[4, 6], [7, 9]], [[4, 5], [7, 8]]]
    calculated_facts, calculated_mats = get_mat(my_mat)
    assert calculated_mats == expected_mats and calculated_facts == expected_facts


def test_mat_det():
    """Test that the mat_det() function returns correctly"""
    my_mats = [
    [[2, 4, 6, 8], [1, 9, 2, 0], [7, 1, 2, 3], [8, 11, 3, 2]],
    [[3, 6, 3], [8, 2, 1], [5, 3, 2]],
    [[4, 1], [3, 2]],
    [[0, 3, 2, 1], [0, 0, 3, 6], [0, 0, 0, 18], [0, 0, 0, 12]],
    [[9, 2, 1, 6, 2], [6, 3, 9, 0, 1], [3, 1, 9, 2, 2], [8, 2, 3, 1, 0], [9, 2, 2, 2, 0]],
    [[0, 0], [0, 0]]
    ]
    expected_dets = [round(np.linalg.det(np.array(my_mat)), 12) for my_mat in my_mats]
    calculated_dets = [round(mat_det(my_mat), 12) for my_mat in my_mats]
    assert calculated_dets == expected_dets


def test_fail_mat_det():
    """Test that the mat_det() function fails correctly"""
    my_mat = [[1, 2, 3], [4, 5, 6]]
    expected_det = 0
    calculated_det = mat_det(my_mat)
    assert calculated_det != expected_det


def test_mat_lu_det():
    """Test that the mat_lu() function returns correctly a matrix determinant"""
    my_mats = [
    [[2, 4, 6, 8], [1, 9, 2, 0], [7, 1, 2, 3], [8, 11, 3, 2]],
    [[3, 6, 3], [8, 2, 1], [5, 3, 2]],
    [[4, 1], [3, 2]],
    [[0, 3, 2, 1], [0, 0, 3, 6], [0, 0, 0, 18], [0, 0, 0, 12]],
    [[9, 2, 1, 6, 2], [6, 3, 9, 0, 1], [3, 1, 9, 2, 2], [8, 2, 3, 1, 0], [9, 2, 2, 2, 0]],
    [[0, 0], [0, 0]]
    ]
    expected_dets = [round(np.linalg.det(np.array(my_mat)), 9) for my_mat in my_mats]
    calculated_dets = [round(mat_lu(my_mat)[2], 9) for my_mat in my_mats]
    assert calculated_dets == expected_dets
