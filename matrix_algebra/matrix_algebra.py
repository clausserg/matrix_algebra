"""
This is a program dealing with matrix algebra. The functions defined herein mimic Numpy functions.
I decided to build this in order to practice what I've learned during Udemy courses.

This program is intentionally made without OBJECT ORIENTATION.
Please checkout my other packages for an implementation of this program using object orientation.
"""


from matrix_operations.mat_add  import *
from matrix_operations.mat_diff import *
from matrix_operations.mat_mul  import *
from input_output.input_output import *


if __name__ == '__main__':

    operations = {
        '1': 'matrix addition',
        '2': 'matrix subtraction',
        '3': 'matrix multiplication'
    }

    # flag to break out of the while loop
    operating = True

    while operating:
        # ask user what matrix operation to be done
        to_do = mat_operations(operations)
        global a_mat, b_mat
        # set up the matrices
        if to_do in ['1', '2', '3']:
            a_mat = get_mat(1)
            b_mat = get_mat(2)
            print("Matrix number 1 is:")
            mat_out(a_mat)
            print("Matrix number 2 is:")
            mat_out(b_mat)

        # let's do the requested operation
        if to_do == '1':
            c_mat = mat_add(a_mat, b_mat)
            mat_out(c_mat)
            operating = False
        elif to_do == '2':
            c_mat = mat_diff(a_mat, b_mat)
            mat_out(c_mat)
            operating = False
        elif to_do == '3':
            c_mat = mat_mul(a_mat, b_mat)
            mat_out(c_mat)
            operating = False

