import random
import math
L1 = []
L2 = []
L3 = []
avg = 0
for i in range(0, 500):
	for x in range(0, 9):
		rnum = random.randint(1, 500)
		L1.append(rnum)
	L2.append(L1)
	L1.sort()
	minn = max(L1)
	maxx = minn + (minn * .2)
	L3.append(random.randint(minn, int(maxx)))
	L1 = []
	print(str(L2[i]) + ":" + str(L3[i]))
for y in L3:
	avg += y 
print(avg)
print(avg/500)
