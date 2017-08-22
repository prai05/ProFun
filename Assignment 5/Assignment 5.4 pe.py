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
# SEP 27 2016
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

# Function for group people by age
def people(comb_naa, Age):
  res = []
  if Age in AGES:
    for name, age in comb_naa.items():
      if Age == age:
        res.append(name)
    return res
  else:
    return('Not Yet Implemented')

combine_list(NAMES, AGES)

# Test case
print('18 =', people(comb_naa, 18))
print('19 =', people(comb_naa, 19))
print('20 =', people(comb_naa, 20))
print('21 =', people(comb_naa, 21))
print('22 =', people(comb_naa, 22))
print('23 =', people(comb_naa, 23))
print('\n')
print('Dan' in people(comb_naa, 18) and 'Cathy' in people(comb_naa, 18))
print ('Ed' in people(comb_naa, 19) and 'Helen' in people(comb_naa, 19) and 'Irene' in people(comb_naa, 19)
       and 'Jack' in people(comb_naa, 19) and 'Larry' in people(comb_naa, 19))
print ('Alice' in people(comb_naa, 20) and 'Frank' in people(comb_naa, 20) and 'Gary' in people(comb_naa, 20))

# Input
while True:
  Age = int(input('\nEnter Age: '))
  print(people(comb_naa, Age))
