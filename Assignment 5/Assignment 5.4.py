# Assignment 5
# 010123102 Computer Programming Fundamental
#
# Assignment 5.4
# In this exercise, there are two lists.
# NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
# AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
# These lists match up, so Alice’s age is 20, Bob’s age is 21, and so on. Write a function combine lists
# that combines these lists into a dictionary (hint: what should the keys, and what should the values, of
# this dictionary be?). Then, write a function people that takes in an age and returns the names of all
# the people who are that age.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 24 2016
# Due Date SEP. 27 2016

import collections

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Function used to combine name and age to dictonary
def combine_list(NAMES, AGES):
  global comb_naa
  comb_naa = {} # Combine Name and Age
  for i in range(len(NAMES)):
    comb_naa[NAMES[i]] = AGES[i]
  print(comb_naa)

# Function used to print NAME that in input AGE
def take_age(comb_naa):
  Age = int(input('Enter Age: '))
  for name, age in comb_naa.items():
    if Age == age:
      print(name)
  else:
    print('Not Yet Implemented')

combine_list(NAMES, AGES)
while True:
  take_age(comb_naa)


