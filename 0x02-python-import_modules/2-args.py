#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_args = len(sys.argv) - 1
    if total_args == 0:
        print('0 arguments.')
    elif total_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total_args))
    for i in range(total_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
