#!/usr/bin/python3
def magic_string():
    magic_string.r = getattr(magic_string, 'r', -1) + 1
    return "BestSchool, " * magic_string.r + "BestSchool"
