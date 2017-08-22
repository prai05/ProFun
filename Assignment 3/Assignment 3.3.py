# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.3
# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

num = int(input('Enter the integer: '))
outsideMode = str(input('Enable Outside Mode? Y/N: '))

def checkRange(num, outsideMode):
    i = True
    if outsideMode == 'Y' and  num not in range(2, 10):
        print(i)
    elif outsideMode == 'N' and num in range(1, 11):
        print(i)
    else:
        print(not i)

checkRange(num, outsideMode)

