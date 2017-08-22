# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.12
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

string = str(input('Enter string: '))

def checkCATDOG(string):
  i = 0
  n = 0
  cat = 0
  dog = 0
  x = False
  # Loop check CAT
  while i < len(string):
    if string[i: i + 3] == 'cat':
      cat += 1
    i += 1
  # Loop check DOG
  while n < len(string):
    if string[n: n + 3] == 'dog':
      dog += 1
    n += 1
  # If cat = dog then True
  if cat == dog and cat != 0 and dog != 0:
    x = True

  print(x)


checkCATDOG(string)
