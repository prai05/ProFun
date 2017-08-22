# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.7
# Given three ints, a b c, return True if one of b or c is "close"
# (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
print('{}, {}, {}'.format(a, b, c))

def close_far(a, b, c):
  x = False
  if abs(b - a) <= 1 and abs(b - a) != abs(c - a):
    if abs(c - b) >= 2 and abs(c - a) != 0:
      x = True
  elif abs(c - a) <= 1 and abs(c - a) != abs(b - a):
    if abs(b - c) >= 2 and abs(b - c) != 0:
      x = True
  print(x)

close_far(a, b, c)
