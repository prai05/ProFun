# Assignment 2
# 010123102 Computer Programming Fundamental
#
# Assignment 2.6
# Num in range 2000-3500 divisible by 7 but are not a multiple of 5 ,comma-separated sequence on a single line
#
# Phattharanat Khunakornophat
# ID 5901012610091
# AUG 29 2016
# Due Date Aug. 30 2016

print('Assignment 1.6')
number = ''
for num in range(2000, 3201):
    if num % 5 != 0:
        if num % 7 == 0:
            number += str(num) + ","
print(number[0:-1])
