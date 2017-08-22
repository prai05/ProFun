import time


def fib(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return (fib(num-1) + fib(num-2))


# while True:
# num = int(input('Enter number: '))
start = time.time()
print(fib(50))
print(" {0:.50f} seconds" .format(time.time()-start))
