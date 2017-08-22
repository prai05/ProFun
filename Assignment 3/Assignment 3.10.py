# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.10
# Return the "centered" average of an array of ints,
# which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
# Use int division to produce the final average. You may assume that the array is length 3 or more.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 2 2016
# Due Date SEP. 6 2016

# Mean except ignore one large and small

list_number = [] # Array name list_number
x = int(input('Enter how many element in Array: '))
sum = 0
mem = 0 # Index of list element

def input_num(list_number, x):
    for n in range(x):
        num = int(input('Enter Number: '))
        list_number.append(num)
    print('Element in Array: ', list_number)

def center_avg(list_number, x, sum, mem):
    large = max(list_number)
    small = min(list_number)
    for i in range(0, x):
        sum = sum + list_number[mem]
        mem = mem + 1
    print('\nSUM of all number except largest and smallest = ', sum - large - small)
    print('\nCentered AVG = ', int((sum - large - small) / (x - 2)))


input_num(list_number, x)
center_avg(list_number, x, sum, mem)

# sum += ...list element... is sum of element in list
# but sum += ...list name ....  <<< Error
