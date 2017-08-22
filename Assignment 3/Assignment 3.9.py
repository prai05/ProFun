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

# Input the integer to Array
list_number = []
x = int(input('Enter how many element in Array: '))
count = 0
mem = 0

def input_num(list_number, x):
    for n in range(x):
        num = int(input('Enter Integer: '))
        list_number.append(num)

    print('\nElement in Array: ', list_number)

# For find Even number in Array
def find_even(x, list_number, count, mem):
    for i in range(0, x):
        if list_number[mem] % 2 == 0:
            count += 1
        mem = mem + 1
    print('How many Even-number in list: ', count)

input_num(list_number, x)
find_even(x, list_number, count, mem)
