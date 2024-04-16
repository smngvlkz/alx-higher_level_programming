#!/usr/bin/python3
import sys
import signal

def print_stats(status_codes, file_size):
    """
    Prints the statistics of the file.

    Args:
        status_codes: Dictionary status of codes and their counts.
        file_size: Total size of the file.
    """
    print("File size: {:d}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """
    Handles the signal interruption (CTRL + C).

    Args:
        sig: Signal number
        frame: Current stack frame
    """
    print_stats(status_codes, file_size)
    sys.exit(0)

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        data = line.split()
        status_code = data[-2]
        file_size += int(data[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
        if i % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    pass
finally:
    print_stats(status_codes, file_size)
