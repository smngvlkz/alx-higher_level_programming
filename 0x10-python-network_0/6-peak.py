#!/usr/bin/python3
"""Module to find a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    
    Args:
    list_of_integers (list): A list of unsorted integers.
    
    Returns:
    int or None: A peak element from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return list_of_integers[left]
