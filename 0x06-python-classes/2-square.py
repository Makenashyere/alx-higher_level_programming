#!/usr/bin/python3

"""Define a class square."""


class Square:
   """Represent a square."""

def __init(self,size=0):
"""Initialize a new square.

Args:
size (int):The size of the new square.
"""
if not isinstance(size, int):
    raise TypeError("size must be an integer")
elif size < 0:
    raise valueError("size ust be >= 0")
self.__size = size
