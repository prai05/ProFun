
def fac(num):
  if num == 1:
    return 1
  else:
    return(num * fac(num-1))

while True:
  num = int(input('Enter Number: '))
  print(fac(num))
