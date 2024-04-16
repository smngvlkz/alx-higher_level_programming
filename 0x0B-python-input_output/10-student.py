#!/usr/bin/python3
class Student:
    """
    Defines a student by public instance attributes:
    first_nme, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.

        Args:
            first_name: Student's first name
            last_name: Student's last name
            age: Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: List of attribute name of retrieve.

        Returns:
            dict: Disctionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
