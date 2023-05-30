#!/usr/bin/python3
"""Definition of a square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a square side
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a square side
        Returns: None
        """
        self.__size = size
