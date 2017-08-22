# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.1
# 1. You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value:
# 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

speed = float(input('Enter your speed: '))
birthday = input("Today is you birthday? ... Y/N: ")

# Function check speed
def nbd_speed(speed):
    if speed >= 81:
        print('Big ticket') # 2
    elif speed >= 61:
        print('Small ticket') # 1
    else:
        print('No ticket') # 0

# Check birthday
if birthday == 'N':
    speed = speed
    print("Today isn't your birthday")
    print('Your speed is {}'.format(speed))
    nbd_speed(speed)
elif birthday == 'Y':
    speed = speed - 5
    print("Today is your birthday")
    print('Your speed is {}'.format(speed + 5))
    nbd_speed(speed)
