#!/usr/bin/python3
"""
Define a MagicClass.

Matching exactly a bytcode provided by Holberton.
"""

import math

class MagicClass:
    """
    MagicClass defines a circle with radius attribute.
    """

    def __init__(self, radius):
        """
        Intiialize a new MagicClass object.

        Args:
            radius (number): Radius of circle.

        Raises:
            TypeError: radius if not a number (int or float).
    """

    if not isinstance(radius, (int, flaot)):
        raise TypeError("raidus must be a number")

    self.MagicClass__radius = radius

    def area(self):
        """
        Calculates and returns circle area.

        Returns:
            float: circle area.
        """

        return math.pi * (self._MagicClass__radius ** 2)

    def circumference(self):
        """
        Calculates and returns circle circumference.

        Returns:
            float: The circle circumference.
        """

        return 2 * math.pi * self._MagicClass__radius

