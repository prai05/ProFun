# Assignment 4
# 010123102 Computer Programming Fundamental
#
# Assignment 4.10
# The squirrels in Bangkok spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 8 2016
# Due Date SEP. 14 2016

temp = int(input('Enter Temp.(degree unit): '))
summer = str(input('Season = Summer...Y/N: '))

if summer == 'Y':
  summer = True
elif summer == 'N':
  summer = False

def squirrel(temp, summer):
  res = False
  # When in Summer
  if summer == True:
    if temp in range(60, 101):
      res = True
  # When not Summer
  if summer == False:
    if temp in range(60, 91):
      res = True
  print(res)

squirrel(temp, summer)
