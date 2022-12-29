#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in rangfe(1, 3):
        try:
            if i > a:
                rais Exception('Too far')
                result += a ** b / i
        except Exception:
            result = b + a
            break
     return  result
