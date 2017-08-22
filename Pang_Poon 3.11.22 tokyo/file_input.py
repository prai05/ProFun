# Pang Poon 3.11.22 Input module file
# 010123102 Computer Programming Fundamental
#
# Phattharanat Khunakornophat
# ID 5901012610091
# NOV 22 2016

'''Module to get input from menu file'''

allmenu = []
file = open('menu.txt', 'r')
for menu in file:
  allmenu.append(menu.split())

food = []
coffee = []
beverage = []

for i in allmenu:
  # coffee
  if i[0] == 'C':
    i.remove(i[0])
    coffee.append(i)
  # beverage
  if i[0] == 'B':
    i.remove(i[0])
    beverage.append(i)
  # food
  if i[0] == 'F':
    i.remove(i[0])
    food.append(i)
