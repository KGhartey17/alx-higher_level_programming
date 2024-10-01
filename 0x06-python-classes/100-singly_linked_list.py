#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets or sets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets or sets the next_node of the Node."""
      
