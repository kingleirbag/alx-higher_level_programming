#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_obj = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
count = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = count
            if tokens[-2] in status_obj:
                status_obj[tokens[-2]] += 1
                count += 1
            try:
                file_size += int(tokens[-1])
                if a == count:
                    count += 1
            except FileNotFoundError:
                if a == count:
                    continue
        if count % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_obj.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_obj.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_obj.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
