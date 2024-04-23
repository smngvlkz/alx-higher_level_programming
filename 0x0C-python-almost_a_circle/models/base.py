#!/usr/bin/python3
"""
Base Class module.
"""
import json
import os
import csv
import turtle

class Base():
    """
    Base class module.

    Attributes:
        __nb_objects: Number of Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        New Base Constructor.

        Args:
            id: Id of the Base instance. If None, id set to the number of Base objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries returned.

        if `list_dictionaries` is None or empty, return an empty string.

        Parameters:
            list_dictionaries: List of dictionaries to convert to a JSON string.

        Returns:
            str: JSON string epresentantion of `list_dictionaries`.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        JSON string representation json_string returned.

        Args:
            json_string: JSON string.

        Returns:
            list: List of dictionaries. Returns an empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return[]
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        All rectangles and squares drawn using turtle module.

        Args:
            list_rectangles: List of Rectangle instance.
            list_squares: List of Square instances.
        """
        window = turtle.Screen()
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

        t.penup()
        t.goto(0, 0)
        t.pendown()

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        window.mainloop()

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_obj to a file written.

        Args:
            list_objs: List of instances that inherits from Base.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Load instance from file returned.

        Returns:
            list: List of instances that inherits from Base.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all dictionary attribute already set.

        Args:
            **dictionary: Dictionary of key-value pairs of attributes.

        Returns:
            Base: An instance of Base class.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise TypeError("Cannot create instance for this class name")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Instance to save as a CSV file.

        Args:
            list_objs: List of instances that inherits from Base.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Instance from a CSV file to load returned.

        Returns:
            list: List of instances that inherits from Base.
        """
        filename = f"{cls.__name__}.csv"
        list_objs = []
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]), "height": int(row[2]), "x": int(row[3]), "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(row[1]), "x": int(row[2]), "y": int(row[3])}
                    list_objs.append(cls.create(**dictionary))
        return list_objs
