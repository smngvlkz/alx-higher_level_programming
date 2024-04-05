#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    function takes a matrix of numbers and a divisor, and returns a new
    matrix where each element is divided by divisor, rounded
    to 2 decimal

    Args:
        matrix (list of list of (int or float)): matrix to be divided.
        div (int or float): number by which to divide

    Returns:
        list of list of float: new matrix with elements divided.

    Raises:
        TypeError: matrix if not a list of lists(int or float), each row matrix if not same size, or div if not a number.
        ZeroDivisionError: div if zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) and
            all(isinstance(item, (int, float)) for item in row) for
            row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
