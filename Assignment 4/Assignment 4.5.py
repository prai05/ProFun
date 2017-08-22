# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.5
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive --
# then that value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016

def fix_teen(n):
  if (13 <= n and n <= 19 and (n != 15 or n != 16)):
    return 0 # 0 is multiplier for teen used to change teen number to 0
  else:
    return 1

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

def no_teen_sum(a, b, c):
  print(a * fix_teen(a) + b * fix_teen(b) + c * fix_teen(c))

no_teen_sum(a, b, c)
