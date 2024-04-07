#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of list of int or flaot): First matrix.
        m_b: Second matrix.

    Returns:
        list of list of int or float: Product of matrix multiplication.

    Raises:
        TypeError: either input if not a list of lists, contains non-numeric elements, or not a rectangle.
        ValueError: either input if empty or matrices cannoct be multiplied.
    """
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if m_a.dtype not in [np.int64, np.float64] or m_b.dtype not in [np.int64, np.float64]:
        raise TypeError("m_a and m_b should contain only integers or floats")

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b).tolist()
