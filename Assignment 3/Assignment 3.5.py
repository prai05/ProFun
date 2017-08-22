# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.5
# find 'hi' in the string
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

def find_hi():
    string = str(input('Enter string: '))
    x = 0

    for i in range(len(string)):
        if i != int(len(string)-1): # The last letter of string is (len-1) because index-count start at 0
            if string[i] == 'h':
                if string[i + 1] == 'i':
                    x += 1
        i += 1
    print(x)

find_hi()
