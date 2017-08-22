
def pwr(x, n):
  if (n == 0):
    return 1
  elif (n == 1):
    return x
  elif (n == 2):
    return x*x
  else:
    pass
    y = pwr(x, n//2)
    if (n%2 == 1):
      return x*y*y
    else:
      return y*y

# print(pwr(20,100000))
ans = 1
for i in range(100000):
  ans *= 20
print(ans)
# O( n*log(x)*log(n))