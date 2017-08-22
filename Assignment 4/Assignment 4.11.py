# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.11
# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6.
# Note: the function abs(num) computes the absolute value of a number.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

def true6():
  if a != b and (a == 6 or b == 6):
    return True
  elif abs(a - b) == 6 or (a + b) == 6:
    return True
  else:
    return False

print(true6())
