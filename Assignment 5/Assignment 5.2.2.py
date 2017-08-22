# Assignment 5
# 010123102 Computer Programming Fundamental
#
# Assignment 5.2
# Write a program that first displays a simple cafe menu (see example below), asks the user to enter the number of a choice,
# and either prints the appropriate action OR prints an error message that their choice was not valid.

# 5.2.2 Create a new file rps.py that will generate the outcome of the rock, scissors, paper game.
# The program should ask the user for input and display the answer
# The only valid inputs are rock, paper, and scissors. If the user enters anything else, your program
# should output 'This is not a valid object selection'
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 20 2016
# Due Date SEP. 20 2016


check = ['rock', 'paper', 'scissors'] # To check valid input from both player

P1 = input('Player 1? ')
P2 = input('Player 2? ')

# --------Check input--------
if P1 not in check:
  print('P1 is not a valid object selection')
if P2 not in check:
  print('P2 is not a valid object selection')

# --------Game-----------
if (P1 and P2) in check and P1 == P2:
  print('Tie')

# P1 win
elif P1 == check[0] and P2 == check[2]:
  print('Player 1 wins')
elif P1 == check[1] and P2 == check[0]:
  print('Player 1 wins')
elif P1 == check[2] and P2 == check[1]:
  print('Player 1 wins')

# P2 win
elif P1 == check[0] and P2 == check[1]:
  print('Player 2 wins')
elif P1 == check[1] and P2 == check[2]:
  print('Player 2 wins')
elif P1 == check[2] and P2 == check[0]:
  print('Player 2 wins')
else:
  print('Invalid input')
