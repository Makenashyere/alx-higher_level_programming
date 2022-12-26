#!/usr/bin/python3

"""Print the numbers from 1 to 100 seoarated by a space.
  For multiples of three, print fizz instead of the number.
  For multiples of five, print Buzz instead of thr number.
  For multiples of three and five, print fizzbuzz insteda od the number.
  """


  def fizzbuzz():
      for number in range(1, 101):
          if number % 3 == 0 and number % 5 == 0:
              print("FizzBuzz ", end="")
          elif number % 3 == 0:
              print("Fizz ", end="")
          elif number % 5 == 0:
              print("Buzz ", end="")
          else:
              print("{} ".format(number), end="")

