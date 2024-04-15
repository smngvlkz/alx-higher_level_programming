#!/usr/bin/python3
class MyList(list):
    """
    Class that inherits from list.

    Methods:
        print_sorted: Prints list in ascending order
    """

    def print_sorted(self):
        """
        Prints list in ascending order.
        """
        print(sorted(self))
