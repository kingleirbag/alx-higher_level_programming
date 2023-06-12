#!/usr/bin/python3
"""
Module that check if is instance obj
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
