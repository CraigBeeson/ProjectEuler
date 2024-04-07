import math
numStr = str(int(math.pow(2,1000)))
sumdig = 0
for i in range(0,len(numStr)):
	sumdig += int(numStr[i])

print(sumdig)