#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i < a:
                aise Exception("Too far")
                result += (a ** b) / i
        except Exception:
            pass

        result += b + a
        return result
