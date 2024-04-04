#!/usr/bin/python3
"""
SinglyLinkedList module.

Defines the Node and SinglyLinkedList classes for a singly linked.
"""

class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): data value stored in the node.
            next_node (Node, optional): next node in linked list.
                Default to None.

        Raises:
            TypeError:
                - data if not an integer.
                - next_node is not a Node or None.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not (isinstance(next_node, Node) or next_node is None):
            raise TypeError("next_node must be a Node object")

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data attribute.

        Returns:
            int: data value stored in node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data attribute.

        Args:
            value (int): new data value for node.

        Raises:
            TypeError: value if not integer
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node attribute.

        Args:
            value (Node, optional): new next_node for current node.
                Can be None if it's the last node.

        Raises:
            TypeError: vallue is not a Node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node attribute.

        Args:
            value (Node, optional): new next node for current node.
                Can be None if it's last node.

        Raises:
            TypeError: value if not a Node or None.
        """

        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

class SinglyLinkedList:
    """
    Represenets a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList object.
        """

        self.head = None

    def __str__(self):
        """
        String representation of linked list (one node per line).

        Returns:
            str: String representation of linked list.
        """

        current = self.head
        output = ""
        while current:
            output += str(current.data) + "\n"
            current = current.next_node
        return output[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value in correct sorted piosition
        (ascending order).

        Args:
            value (int): value to insert linked list.
        """

        new_node = Node(value)
        current = self.head
        prev = None

        while current and current.data < value:
            prev = current
            current = current.next_node

        if not prev:
            self.head = new_node
        else:
            prev.next_node = new_node

        if current:
            new_node.next_node = current
