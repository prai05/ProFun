# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.8
# Given a string of even length, return the first half.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016
string = str(input('Enter the string: '))
length = int(len(string))

def halfString(string, length):
    print(string[0: int(length / 2)])

halfString(string, length)
