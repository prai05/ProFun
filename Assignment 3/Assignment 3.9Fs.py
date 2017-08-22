# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.9
# Return the number of even integer in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 2 2016
# Due Date SEP. 6 2016

# DEF input Array
def _array():
    mem = int(input('How many element in Array: ')) # Ask for how many  element
    global  num
    num = []
    for i in range(mem):
        x = int(input('Enter Number: '))
        num.append(x)
        i += 1
def find_Even(num):
    count = 0
    for x in num:
        if x % 2 == 0:
            count += 1
    print(count)

while True:
    _array()
    find_Even(num)
