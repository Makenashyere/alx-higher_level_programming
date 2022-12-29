#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer w "{:d}".format().

    If a ValueError message is caught, a correspnding
    message is printe to stderr

    Args:
      value (int): The integer to print

    Returns:
      If a TypeError of ValueError occurs - False.
      otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

