#!/usr/bin/python3
print("".join(chr(122 - i + i % 2 * 32) for i in range(26)))
