#!/usr/bin/python3
def uniq_add(my_list=[]):
    added_result = 0
    for uniq_int in set(my_list):
        added_result += uniq_int
    return added_result
