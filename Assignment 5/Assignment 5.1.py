# Assignment 5
# 010123102 Computer Programming Fundamental
#
# Assignment 5.1
# Write a program that first displays a simple cafe menu (see example below), asks the user to enter the number of a choice,
# and either prints the appropriate action OR prints an error message that their choice was not valid.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 20 2016
# Due Date SEP. 20 2016

print('''\
1. Soup and salad
2. Pasta with meat sauce
3. Chef's special\
''')

def menu():
  menu = ['Soup and salad', 'Pasta with meat sauce', 'Chef\'s special']
  check = [1, 2, 3] # Valid input list to check the input
  num = int(input('\nWhich number would you like to order? ')) # Ask for number

  # If the number in the check input list then print menu
  if num in check:
    print('{} coming right up!'.format(menu[num-1]))
  else:
    print('Invalid Input')

while True:
  menu()
