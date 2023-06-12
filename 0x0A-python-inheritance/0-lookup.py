#!/usr/bin/python3
"""
A function that looks the list of available attributes and methods
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
