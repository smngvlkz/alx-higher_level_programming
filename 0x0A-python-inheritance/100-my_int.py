#!/usr/bin/python3
class MyInt(int):
    """
    Class inherits from int and inverts the '==' and '=' operators.

    Methods:
        __eq__: Overrides the '==' operator
        __ne__: Overrides the '!=' operator
    """

    def __eq__(self, other):
        """
        Overrides the '==' operator

        Args:
            other: Integer to compare with

        Returns:
            bool: True if self and other are not equal, otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the '!=' operator

        Args:
            other: Integer to compatre with

        Returns:
            bool: True if self and other equal, False otherwise.
        """
        return super().__eq__(other)
