#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    arguments = sys.argv[1:]
    sum_total = 0

    for argument in arguments:
        sum_total += int(argument)

    print(sum_total)
