#!/usr/bin/python3
def no_c(my_string):
    new_str = [elem for elem in my_string if elem != 'c' or elem != 'C']
    return ("".join(new_str))
