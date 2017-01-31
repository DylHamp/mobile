import random
import math
import statistics as st
L1 = []
L2 = []
L3 = []
for i in range(0, 500):
	for x in range(0, 9):
		rnum = random.randint(1, 500)
		L1.append(rnum)
	L1.sort()
	L2.append(L1)
	L3.append(st.mean(L1))
	L1 = []
	print(str(L2[i]) + ":" + str(L3[i]))
print(st.mean(L3))
print(st.stdev(L3))
