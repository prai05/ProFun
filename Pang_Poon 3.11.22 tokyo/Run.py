# Pang Poon 3.11.22 Program file
# 010123102 Computer Programming Fundamental
#
# Phattharanat Khunakornophat
# ID 5901012610091
# NOV 22 2016

import UI
import file_input
import time

menu = file_input.allmenu
coffee = file_input.coffee
beverage = file_input.beverage
food = file_input.food
order = []
Cash = 0


def login():
  '''This is Login Menu
  Press m to go to main menu'''
  log_in = ''
  UI.UI.login()
  # input to go to main menu
  while log_in == '':
    log_in = input('Press m to enter to mainmenu: ')
    if log_in == 'm':
      UI.UI.mainmenuHead()
      _mainmenu()
      log_in == ''
    else:
      log_in == ''
      UI.UI.login()
      login()


def _mainmenu():
  '''This is Main menu
  Press c/b/f to go to Coffee Beverage Food
  Press q to go to Confirm Order
  Press e to edit order'''
  # print order
  cnt = 0
  cost = 0
  for i in range(len(order)):
    orderx = '+' + '   ' + str(i + 1) + (2 - len(str(i + 1)))*' ' + '  ' + order[i][1] + (20 - len(order[i][1]))*' ' + '   ' + order[i][2] + (2 - len(order[i][2]))*' ' + 46*' ' + '+'
    cost += int(order[i][2])
    print(orderx)
    cnt += 1
    # fill blankline
  for i in range(16 - cnt):
    UI.UI.whiteline()
  print('+   Total = {} +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'.format(str(cost) + (4 - len(str(cost)))*' '))
  # get input to go to f/ b/ c
  _menu = ''
  while _menu == '':
    _menu = input('Main menu: Press any shortcut: ')
    if _menu == 'f':
      UI.UI.foodmenuHead()
      food_UI()
    elif _menu == 'b':
      UI.UI.bevmenuHead()
      beverage_UI()
    elif _menu == 'c':
      UI.UI.cofmenuHead()
      coffee_UI()
    elif _menu == 'e':
      UI.UI.editOrderHead()
      edit_UI()
    elif _menu == 'q':
      cash = int(input('Pay = '))
      UI.UI.confirmOrderHead()
      confirm_UI(cash, order)
    else:
      _menu = ''
      UI.UI.mainmenuHead()
      _mainmenu()

def coffee_UI():
  '''This is Coffee menu
  Press b to back to main menu'''
  # print Coffee and order
  cnt = 0
  if len(coffee) > len(order):
    for i in range(len(coffee)):
      try:
        id = coffee[i][0]
        menu = '+   ' + id + '   ' + coffee[i][1] + (20 - len(coffee[i][1]))*' ' + coffee[i][2] + (2 - len(coffee[i][2]))*' ' + '      |'
        orderx = '   ' + str(i + 1) + (2 - len(str(i + 1)))*' ' + '  ' + order[i][1] + (20 - len(order[i][1]))*' ' + '   ' + order[i][2] + (2 - len(order[i][2]))*' ' + 8*' ' + '+'
        printcof = menu + orderx
        print(printcof)
      except:
        menu = '+   ' + id + '   ' + coffee[i][1] + (20 - len(coffee[i][1]))*' ' + coffee[i][2] + (2 - len(coffee[i][2]))*' ' + '      |'
        printcof = menu + 40*' ' + '+'
        print(printcof)
      cnt += 1
  else:
    for j in range (len(order)):
      try:
        id = coffee[j][0]
        menu = '+   ' + id + '   ' + coffee[j][1] + (20 - len(coffee[j][1]))*' ' + coffee[j][2] + (2 - len(coffee[j][2]))*' ' + '      |'
        orderx = '   ' + str(j + 1) + (2 - len(str(j + 1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printcof = menu + orderx
        print(printcof)
      except:
        orderx = '   ' + str(j + 1) + (2 - len(str(j + 1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printcof = '+' + 37*' ' + '|' + orderx
        print(printcof)
      cnt += 1

  # fill blankline/ 3.head/ 1.bot/ 1.command
  for i in range(20 - cnt):
    UI.UI.whiteline()
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

  # input
  key = ''
  while key == '':
    key = input('Coffee: Press any shortcut: ')
    if key == 'b':
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    if len(key) == 3:
      menu = file_input.allmenu
      for z in range (len(menu)):
        if key == menu[z][0] and len(order) < 15:
          order.append(menu[z])
          key = ''
      UI.UI.cofmenuHead()
      coffee_UI()
    else:
      key = ''
      continue


def beverage_UI():
  '''This is Beverage menu
  Press b to back to main menu'''
  # print Beverage and order
  cnt = 0
  if len(beverage) >= len(order):
    for i in range(len(beverage)):
      try:
        id = beverage[i][0]
        menu = '+   ' + id + '   ' + beverage[i][1] + (20 - len(beverage[i][1]))*' ' + beverage[i][2] + (2 - len(beverage[i][2]))*' ' + '      |'
        orderx = '   ' + str(i + 1) + (2 - len(str(i + 1)))*' ' + '  ' + order[i][1] + (20 - len(order[i][1]))*' ' + '   ' + order[i][2] + (2 - len(order[i][2]))*' ' + 8*' ' + '+'
        printbev = menu + orderx
        print(printbev)
      except:
        menu = '+   ' + id + '   ' + beverage[i][1] + (20 - len(beverage[i][1]))*' ' + beverage[i][2] + (2 - len(beverage[i][2]))*' ' + '      |'
        printbev = menu + 40*' ' + '+'
        print(printbev)
      cnt += 1
  else:
    for j in range (len(order)):
      try:
        id = beverage[j][0]
        menu = '+   ' + id + '   ' + beverage[j][1] + (20 - len(beverage[j][1]))*' ' + beverage[j][2] + (2 - len(beverage[j][2]))*' ' + '      |'
        orderx = '   ' + str(j + 1) + (2 - len(str(j + 1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printbev = menu + orderx
        print(printbev)
      except:
        orderx = '   ' + str(j + 1) + (2 - len(str(j+1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printbev = '+' + 37*' ' + '|' + orderx
        print(printbev)
      cnt += 1

  # fill blankline/ 3.head/ 1.bot/ 1.command
  for i in range(20 - cnt):
    UI.UI.whiteline()
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

  # input
  key = ''
  while key == '':
    key = input('Beverage: Press any shortcut: ')
    if key == 'b':
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    if len(key) == 3:
      menu = file_input.allmenu
      for z in range (len(menu)):
        if key == menu[z][0] and len(order) < 15:
          order.append(menu[z])
          key = ''
      UI.UI.bevmenuHead()
      beverage_UI()
    else:
      key = ''
      continue


def food_UI():
  '''This is Food menu
  Press b to back to main menu'''
  # print Food and order
  cnt = 0
  if len(food) > len(order):
    for i in range(len(food)):
      try:
        id = food[i][0]
        menu = '+   ' + id + '   ' + food[i][1] + (20 - len(food[i][1]))*' ' + food[i][2] + (2 - len(food[i][2]))*' ' + '      |'
        orderx = '   ' + str(i + 1) + (2 - len(str(i + 1)))*' ' + '  ' + order[i][1] + (20 - len(order[i][1]))*' ' + '   ' + order[i][2] + (2 - len(order[i][2]))*' ' + 8*' ' + '+'
        printfood = menu + orderx
        print(printfood)
      except:
        menu = '+   ' + id + '   ' + food[i][1] + (20 - len(food[i][1]))*' ' + food[i][2] + (2 - len(food[i][2]))*' ' + '      |'
        printfood = menu + 40*' ' + '+'
        print(printfood)
      cnt += 1
  else:
    for j in range (len(order)):
      try:
        id = food[j][0]
        menu = '+   ' + id + '   ' + food[j][1] + (20 - len(food[j][1]))*' ' + food[j][2] + (2 - len(food[j][2]))*' ' + '      |'
        orderx = '   ' + str(j + 1) + (2 - len(str(j + 1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printfood = menu + orderx
        print(printfood)
      except:
        orderx = '   ' + str(j + 1) + (2 - len(str(j + 1)))*' ' + '  ' + order[j][1] + (20 - len(order[j][1]))*' ' + '   ' + order[j][2] + (2 - len(order[j][2]))*' ' + 8*' ' + '+'
        printfood = '+' + 37*' ' + '|' + orderx
        print(printfood)
      cnt += 1

  # fill blankline/ 3.head/ 1.bot/ 1.command
  for i in range(20 - cnt):
    UI.UI.whiteline()
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

  # input
  key = ''
  while key == '':
    key = input('Food: Press any shortcut: ')
    if key == 'b':
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    if len(key) == 3:
      menu = file_input.allmenu
      for z in range (len(menu)):
        if key == menu[z][0] and len(order) < 15:
          order.append(menu[z])
          key = ''
      UI.UI.foodmenuHead()
      food_UI()
    else:
      key = ''
      continue


def edit_UI():
  ''' This is Edit Order
  Press d+No to delete Order
  Press b to back to main menu'''
  # print order
  cnt = 0
  cost = 0
  for i in range (len(order)):
    orderx = '+' + '   ' + str(i + 1) + (2 - len(str(i+1)))*' ' + '  ' + order[i][1] + (20 - len(order[i][1]))*' ' + '   ' + order[i][2] + (2 - len(order[i][2]))*' ' + 46*' ' + '+'
    cost += int(order[i][2])
    print(orderx)
    cnt += 1

  # fill blankline
  for i in range(19-cnt):
    UI.UI.whiteline()
  print('+   Press d+NO to delete order                                                 +')
  print('+   Total = {} +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'.format(str(cost) + (4 - len(str(cost)))*' '))

  # input
  key = ''
  while key == '':
    key = input('Edit order: Press any shortcut: ')
    if key == 'b':
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    elif len(key) == 3 and key[0] == 'd' and len(order) > 0 and int(key[1:3]) <= len(order):
      del order[int(key[1:3]) - 1]
      UI.UI.editOrderHead()
      edit_UI()
      key = ''
    else:
      key = ''
      continue

class write_file():
  '''This is write order file class'''
  def __init__(self):
    self.order = order
  def write_order(self, cost, cash, change):
    timex = time.strftime('%a, %d %b %Y %H:%M:%S')
    file = open('order.txt', 'a')
    file.write('_ {}\n'.format(timex))
    for i in range (len(order)):
      file.write(order[i][1] + (20 - len(order[i][1]))*' ' + order[i][2] + '\n')
    file.write('total = {}  cash = {}  change = {}  \n'.format(cost, cash, change))
    file.close()

def confirm_UI(cash, order):
  '''This is Confirm Order
  Press c to Confirm Order It will set Order to []'''
  # Print Total cash cost
  cost = 0
  for i in range (len(order)):
    cost += int(order[i][2])
  if cash - cost < 0:
    change = 'not enough money'
  else:
    change = cash - cost
  print('''+      Total   = {}'''.format(str(cost) + (62 - len(str(cost)))*' ' + '+'))
  print('''+      Cash    = {}'''.format(str(cash) + (62 - len(str(cash)))*' ' + '+'))
  print('''+      Change  = {}'''.format(str(change) + (62 - len(str(change)))*' ' + '+'))
  for i in range(12):
    UI.UI.whiteline()
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# input
  key = ''
  while key == '':
    key = input('Confirm Order: Press any shortcut: ')
    if key == 'b':
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    elif key == 'c':
      write_file.write_order(order, cost, cash, change)
      del order[:]
      UI.UI.mainmenuHead()
      _mainmenu()
      key = ''
    else:
      key = ''
      continue


login()
