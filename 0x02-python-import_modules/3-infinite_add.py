#!/usr/bin/python3
import sys

if __name__ == "___main__":
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print(sum)
