# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.3
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

def input_array():
  global mem
  mem = int(input('How many element in Array: ')) # Ask for how many  element
  global array
  array = []
  for i in range(mem):
    num = int(input('Enter Number: '))
    array.append(num)
    i += 1
  print('Array = ', array)

def has22(array, mem):
  i = 0
  x = False
  while i < mem:
    if array[i] == 2 and (i + 1) < mem and array[i + 1] == 2:
      x = True
    i += 1
  print(x)

input_array()
has22(array, mem)
