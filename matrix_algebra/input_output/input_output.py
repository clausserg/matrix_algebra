"""
Module:
input_output.py

This module contains functions that take input from user and
functions that arrange, in a user-friendly manner, output data for user.
"""


def mat_operations(operations):
    """
    This function presents the user with indexed capabilities of the program,
    e.g. it shows what matrix algebra it is capable of performing.
    Then, it requests the user to insert the 'int' index for the operation
    wished to be performed.

    :param operations: python dictionary, 'key' is the matrix operation index,
    'value' is the matrix operation name. User will request a matrix operation by its 'key'
    :return: 'int' index, matrix operation to be performed
    """

    print("Welcome buddy! I am capable of doing the following:\n")
    for key, value in operations.items():
        print("Type {} for {}".format(key, value))

    # ask user what operation to be done
    while True:
        op_idx = input("\nWhat do you want me to do?")
        if op_idx in operations.keys():
            print("Alright, I will do a {} for you!".format(operations[op_idx]))
            break
        else:
            print("Requested operation unknown.\nChoose from the list of operations presented above!")
    return op_idx


def mat_out(my_mat):
    """
    This function prints a python list of lists, row-by-row,
     i.e. in matrix-like format

    :param my_mat: a python list of lists or some string
    :return: prints a list-per-row from the input list of lists, or some string
    """

    # check if what is passed is a list of lists, i.e. a matrix
    # if yes, print it row by row, otherwise print whatever it is passed to standard output
    if any(isinstance(a_list, list) for a_list in my_mat):
        for row in my_mat:
            print(row)
    else:
        print(my_mat)


def get_mat(nr_mat):
    """
    This function takes a matrix input from the user, i.e. a python list of lists

    :param nr_mat: int index, number of the inserted matrix, e.g. this is matrix number 1.
    :return: a python list of lists, mimics a Numpy array
    """

    # tell user that he is about to set up a matrix
    print("\nLet's setup matrix number {}".format(nr_mat))

    # ask user the dimension of the matrix to be defined
    while True:
        try:
            my_rows = int(input("How many rows:"))
            break
        except ValueError as error:
            print(error)
            print("It must be an integer. Try again!")

    while True:
        try:
            my_cols = int(input("How many columns:"))
            break
        except ValueError as error:
            print(error)
            print("It must be an integer. Try again!")

    # initialize resulting matrix with zeroes
    my_mat = [[0.0 for col in range(my_cols)] for row in range(my_rows)]

    # start filling result matrix with elements from the user
    for row in range(my_rows):
        for col in range(my_cols):
            # be sure user inserts right value types, 'int' or 'floats'
            while True:
                try:
                    my_mat[row][col] = float(input("row = {} col = {}, value = ".format(row, col)))
                    break
                except ValueError as error:
                    print(error)
                    print("Please insert either 'int' or 'float':")
    return my_mat

