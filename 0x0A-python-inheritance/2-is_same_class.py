#!/usr/bin/python3
"""
This module returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
