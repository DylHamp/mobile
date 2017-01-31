import random
import math

L1 = []
L2 = []
L3 = []
for i in range(0, 500):
	for x in range(0, 9):
		rnum = random.randint(1, 500)
		L1.append(rnum)
	L1.sort()
	L2.append(L1)
	L3.append(L1[4]*2)
	L1 = []
	print(str(L2[i]) + ":" + str(L3[i]))


