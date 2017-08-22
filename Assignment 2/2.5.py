# Assignment 2
# 010123102 Computer Programming Fundamental
#
# Assignment 2.5
# Volume of a Cylinder
#
# Phattharanat Khunakornophat
# ID 5901012610091
# AUG 29 2016
# Due Date Aug. 30 2016


import math
# Import math for Pi constant
print('Assignment 1.5')
R = float(input('Enter Cylinder Radius: '))
H = float(input('Enter Cylinder Height: '))
Pi = math.pi # Math module for pi constant
# Pi = 3.14159265358979323846....
Volume = float(Pi * (R ** 2) * H)
print('Volume = {0:.3f}'.format(Volume))
