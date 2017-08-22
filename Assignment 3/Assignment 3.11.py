# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.11
# Difference between largest and smallest number
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 2 2016
# Due Date SEP. 6 2016


list_number = []  # Array name list_number
x = int(input('Enter how many element in Array: '))

def input_num(list_number, x):
    for n in range(x):
        num = int(input('Enter Number: '))
        list_number.append(num)
    print('Member in Array: ', list_number)

def find_diff(list_number):
    large = max(list_number)
    small = min(list_number)
    print('\nThe largest number and the smallest number in list: {}, {}'.format(large, small))
    print('The difference between the largest and smallest number: {}'.format(large - small))

input_num(list_number, x)
find_diff(list_number)
