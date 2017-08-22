# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.9
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

while True:
  num = int(input('Enter number: '))

  def near_ten(num):
    if num % 10 <= 2 or num % 10 >= 8 :
      return  True
    else:
      return False

  print(near_ten(num))
