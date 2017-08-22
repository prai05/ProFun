import inputFile

food = inputFile.foodList
coffee = inputFile.coffeeList

def takeOrder():
  orderID = input('Enter ORDER ID: ')
  if len(orderID) == 3:
    for i in range (len(food)):
      if orderID == food[i][0]:
        print(food[i][1])
        qty = int(input('Enter Qty: '))
        print('BUY: {}  QTY: {}  COST: {}'.format(food[i][1], qty, (qty*int(food[i][2]))))
        food[i][3] = str(int(food[i][3]) - qty)

        foodF = open('food.data', 'wb')
        for i in food:
          foodF.write('{}\t{}\t{}\t{}\n'.format(i[0], i[1], i[2], i[3]))
    return True
  else:
    print('Hello pangpoon')
    return False

while takeOrder():
  pass


