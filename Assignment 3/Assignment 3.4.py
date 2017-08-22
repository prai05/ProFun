# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.4
# Given a string, return a string where for every char in the original, there are two chars.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

print('Double every character')
char = str(input('Enter String: '))
length = len(char)
D_char = ''

def Double_Char(length, D_char):
    for i in range(length):
        D_char = D_char + (2 * char[i])  # Double every character
    print(D_char)

Double_Char(length, D_char)

# Character index start = 0
