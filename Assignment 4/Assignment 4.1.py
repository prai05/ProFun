# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.1
# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016

def _array():
  mem = int(input('How many element in Array: ')) # Ask for how many element
  global num
  num = []
  for i in range(mem):
    x = int(input('Enter Number: '))
    num.append(x)
    i += 1
  print('Array = ', num)

def Sum(num):
  sum = 0
  for i in num:
    if i != 13:
      sum += i
    # If num = 13 then does not count and number that come after 13 not count
    elif i == 13:
      break
    i += 1
  print(sum)


_array()
Sum(num)
