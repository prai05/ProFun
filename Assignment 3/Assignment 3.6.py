# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.6
# Return True if the given string contains an appearance of "xyz"
# Where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

def find_xyz():
    string = str(input('Enter string: '))
    ans = False

    for i in range(int(len(string))):
        if string[i] != '.' and string[i + 1: i + 4] == 'xyz':
            ans = True
        elif i == 0 and string[i: i + 3] == 'xyz':
            ans = True
        i += 1
    print(ans)

while True:
    find_xyz()
