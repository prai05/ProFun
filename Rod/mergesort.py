import time
start = time.time()

list = []
temp = []

for i in range(10000):
  list.append(100000-i)

def sort(st, en):
	if (st >= en):
		return
	elif (st == en-1):
		if (list[st] > list[en]):
			t = list[st]; list[st] = list[en]; list[en] = t # swap
	else:
		mid = int((st+en)/2)
		sort(st, mid)
		sort(mid+1, en)
		lp = st; rp = mid+1; ptr = st;
		while (lp <= mid and rp <= en):
			if (list[lp] <= list[rp]):
				temp[ptr] = list[lp]; lp += 1; ptr += 1
			else:
				temp[ptr] = list[rp]; rp += 1; ptr += 1
		while (lp <= mid):
			temp[ptr] = list[lp]; lp += 1; ptr += 1
		while (rp <= en):
			temp[ptr] = list[rp]; rp += 1; ptr += 1
		for i in range(st, en+1):
			list[i] = temp[i]

for i in range(len(list)):
  temp.append(0)
sort(0, len(list)-1)
print(list)

print(" {0:.20f} seconds" .format(time.time()-start))
