# Assignment 5
# 010123102 Computer Programming Fundamental
#
# Assignment 5.2
# Write a program that first displays a simple cafe menu (see example below), asks the user to enter the number of a choice,
# and either prints the appropriate action OR prints an error message that their choice was not valid.

# 5.2.3 Recall how we define a function using def, and how we pass in parameters.
# Transform your code from exercise 5.2 (the rock, paper, scissors game) into a function that takes parameters,
# instead of asking the user for input. Make sure to return your answer, rather than printing it.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 20 2016
# Due Date SEP. 20 2016

def roc_pap_sci(P1, P2):
  check = ['rock', 'paper', 'scissors'] # To check valid input from both player

  print('Player 1 = {}'.format(P1))
  print('Player 2 = {}'.format(P2))

  # --------Check input--------
  if P1 not in check:
    print('P1 is not a valid object selection')
  if P2 not in check:
    print('P2 is not a valid object selection')

  # --------Game-----------
  if (P1 and P2) in check and P1 == P2:
    return('Tie\n')

  # P1 win
  elif P1 == check[0] and P2 == check[2]:
    return('Player 1 wins\n')
  elif P1 == check[1] and P2 == check[0]:
    return('Player 1 wins\n')
  elif P1 == check[2] and P2 == check[1]:
    return('Player 1 wins\n')

  # P2 win
  elif P1 == check[0] and P2 == check[1]:
    return('Player 2 wins\n')
  elif P1 == check[1] and P2 == check[2]:
    return('Player 2 wins\n')
  elif P1 == check[2] and P2 == check[0]:
    return('Player 2 wins\n')
  else:
    return('Invalid input\n')

# Tie
print(roc_pap_sci('rock', 'rock'))
print(roc_pap_sci('paper', 'paper'))
print(roc_pap_sci('scissors', 'scissors'))
# P1 wins
print(roc_pap_sci('rock', 'scissors'))
print(roc_pap_sci('paper', 'rock'))
print(roc_pap_sci('scissors', 'paper'))
# P2 wins
print(roc_pap_sci('rock', 'paper'))
print(roc_pap_sci('paper', 'scissors'))
print(roc_pap_sci('scissors', 'rock'))
# Invalid
print(roc_pap_sci('rat', 'cat'))
print(roc_pap_sci('fat', 'scissors'))
print(roc_pap_sci('scissors', 'rat'))
