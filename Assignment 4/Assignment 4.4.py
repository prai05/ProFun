# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.4
# Given 3 int values, a b c, return their sum.
# However, if one of the values is the same as another of the values, it does not count towards the sum.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016

def lone_sum():
  mark = [1, 1, 1] # Multiplier for change same sumber to zero ...if lone mutiplier is 1

  a = int(input('First number = '))
  b = int(input('Second number = '))
  c = int(input('Third number = '))
  if (a == b):
    mark[0] = mark[1] = 0
  if (a == c):
    mark[0] = mark[2] = 0
  if (b == c):
    mark[1] = mark[2] = 0

  print('SUM = ', a * mark[0] + b * mark[1] + c * mark[2])

lone_sum()
