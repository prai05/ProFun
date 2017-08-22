# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.8
# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

small = int(input('How many small bar(1 kg) we have: '))
big = int(input('How many big bar(5 kg) we have: '))
goal = int(input('How many kilo per package: '))

def choc(small, big, goal):
  w_big = goal // 5 # Find big bar that we want to pack

  # When have enough big bar
  if w_big <= big:
    goal = goal - (w_big * 5) # small
    if small >= goal:
      return('True, {} big bar, {} small bar'.format(w_big, goal))
    elif small < goal:
      return -1

  # When not enough big bar
  elif w_big > big:
    goal = goal - (big * 5)
    if small >= goal:
      return('True, {} big bar, {} small bar'.format(big, goal))
    elif small < goal:
      return -1

print(choc(small, big, goal))
