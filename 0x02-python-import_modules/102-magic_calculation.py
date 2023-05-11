#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        sum_total = add(a, b)
        for i in range(4, 6):
            sum_total = add(sum_total, i)
        return (sum_total)
    else:
        return(sub(a, b)
