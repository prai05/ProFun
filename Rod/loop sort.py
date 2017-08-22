import time
start = time.time()

list = []
for i in range(10000):
  list.append(10000-i)
sort = []


def sort(list): # selection sort
  for i in range (len(list)):
    min = list[i]
    ind = i
    for j in range (i+1,  len(list)):
      if (list[j] < min):
        min = list[j]
        ind = j
    t = list[i]
    list[i] = list[ind]
    list[ind] = t
  for i in list: # print
    print(i)

def sort2(list): # bubble sort
  for i in range(len(list), 0, -1):
    for j in range(1, i):
      if (list[j] < list[j-1]):
        t = list[j]
        list[j] = list[j-1]
        list[j-1] = t
  for i in list: # print
    print(i)

sort2(list)
print(" {0:.20f} seconds" .format(time.time()-start))

