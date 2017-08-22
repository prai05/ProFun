# Assignment 3
# 010123102 Computer Programming Fundamental
#
# Assignment 3.2
# Giving a day in week encoded as 0 = Sun, 1 = Mon, ....., 6 = Sat, And a boolean indicating if we are on vacation
# Return a string when the alarm clock should ring.
# Weekdays, the alarm should be "7:00"
# And on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off"
#
# Phattharanat Khunakornophat
# ID 5901012610091
# SEP 1 2016
# Due Date SEP. 6 2016

day = int(input('''0 = Sun, 1 = Mon, 2 = Tue, 3 = Wed, 4 = Thu, 5 = Fri, 6 = Sat
Enter day: '''))
vacation = input('Today is your vacation? Y/N: ')
#week = [1, 2, 3, 4, 5]
#weekend = [0, 6]

# Default Alarm
def d_alarm(day):
    if day == 0 or day == 6:
        print('Alarm time = 10:00')
    elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
        print('Alarm time = 7:00')

# Vacation Alarm
def v_alarm(day):
    if day == 0 or day == 6:
        print('Alarm off')
    elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
        print('Alarm time = 10:00')

# Check vacation day
if vacation == 'Y':
    v_alarm(day)
elif vacation == 'N':
    d_alarm(day)

# Note: or .....repeat.expression.again....  NOT  expression ....or .... or ....
