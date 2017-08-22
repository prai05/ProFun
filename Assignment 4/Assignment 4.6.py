# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.6
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
# Given 3 ints, a b c, return the sum of their rounded values.
# To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
# Write the helper entirely below and at the same indent level as round_sum().
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016

def round(n):
  if (n % 10 >= 5):
    n = n + 10 - (n % 10)
  else:
    n = n - (n % 10)
  return n

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def round_sum(a, b, c):
  print('SUM = ', round(a) + round(b) + round(c))

round_sum(a, b, c)
