#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    mean = 0
    weight = 0
    for item in my_list:
        mean += (item[0] * item[1])
        weight += item[1]
    return (mean / weight)
