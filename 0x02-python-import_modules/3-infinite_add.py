#!/usr/bin/python3

if __name__ == "__main__":
    import sys

     arguments = sys.argv[1:]
     sum_total = sum(int(argument) for argument in arguments)

     print(sum_total)
