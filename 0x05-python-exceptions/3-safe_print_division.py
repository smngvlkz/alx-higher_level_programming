#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: Division by zero")
    finally:
        print("Inside result: {}".format(result))
        return result
