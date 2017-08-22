# Assignment 5
# 010123102 Computer Programming Fundamental
#
# Assignment 5.3
# Write a function list intersection that takes two lists as parameters. Return a list that gives the
# intersection of the two lists- i.e, a list of elements that are common to both lists. Run the following test
# cases and make sure your results are the same (note: the ordering of your outputs does not matter -
# [3,2] is the same as [2,3]):
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 26 2016
# Due Date SEP. 27 2016

# Function for intersec two list
def list_intersection(list_a, list_b):
  print('\nlist_A = ', list_a)
  print('list_B = ', list_b)
  intersecAB = []
  for i in list_a:
    if i in list_b and i not in intersecAB :
      intersecAB.append(i)
  return(intersecAB)

# Test case
print(list_intersection([1, 3, 5], [5, 3, 1]))
print(list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9]))
print(list_intersection([2, 3], [3, 3, 3, 2, 10]))
print(list_intersection([2, 4, 6], [1, 3, 5]))
print('\n')

# Input two list
list_a = []
cnt = int(input('How many element in list_A: ')) # Ask for how many element
for i in range(cnt):
  x = int(input('Enter Number: '))
  list_a.append(x)

list_b = []
cnt = int(input('\nHow many element in list_B: ')) # Ask for how many element
for i in range(cnt):
  x = int(input('Enter Number: '))
  list_b.append(x)

print(list_intersection(list_a, list_b))
