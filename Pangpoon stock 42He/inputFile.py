foodList = []
coffeeList = []


foodF = open('food.txt', 'r')
for food in foodF:
  foodList.append(food.split())

coffeeF = open('coffee.txt', 'r')
for coffee in coffeeF:
  coffeeList.append(coffee.split())
