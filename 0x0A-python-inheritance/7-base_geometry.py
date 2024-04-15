#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry with methods area and integer_validator.
    """

    def area(self):
        """
        Method that calculate area of a shape.
        Since method is not implemented in the BaseGeometry class,
        it will raise an Exception when called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validate value.

        Args:
            name: Name of the value.
            value: Value to validate.

        Raises:
            TypeError: Value if not an integer
            ValueError: Value if less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
