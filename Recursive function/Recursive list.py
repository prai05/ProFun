list = [1, 2, 3, 4, 5]
n = len(list)

def SUM(list, n):
  if n - 1 == 0:
    return list[0]
  else:
    return (list[n - 1] + SUM(list, n - 1))

print(SUM(list, n))
