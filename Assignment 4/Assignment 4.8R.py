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

# Rodchananat Khunakornophat
small = int(input('How many small bar(1 kg) we have: '))
big = int(input('How many big bar(5 kg) we have: '))
goal = int(input('How many kilo per package: '))

def choc(small, big, goal):
  bigCnt = 0 # Used big bar
  # Check big
  if (big * 5 <= goal): # not sufficient big
    goal -= big * 5  # Used small
    bigCnt = big # Use all big that we have
  else : # Sufficient big
    bigCnt += goal//5 # find max big to use
    goal %= 5 # find small to use
  # Check small
  if (small <= goal): #
    print('-1 Impossible')
  else:
    print('Use {} big bar, {} small bar'.format(bigCnt, goal))

choc(small, big, goal)
