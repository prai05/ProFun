# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.2
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7). Return 0 for no numbers
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 10 2016
# Due Date SEP. 14 2016


cnt = int(input('How many element in Array: ')) # Ask for how many element
num = []
for i in range(cnt):
  x = int(input('Enter Number: '))
  num.append(x)
  i += 1
print('Array = ', num)

def not67(cnt, num):
  i = 0
  sum = 0
  while (i < cnt):
    if (num[i] == 6):
      # While ..True.. if False then get out the loop this while.....go to else
      while (i < cnt and num[i] != 7):
        i += 1
    else:
      sum += num[i]
    i += 1
  print(sum)

not67(cnt, num)
