import math
amiNums = set()
for i in range(1,10000):
	divisors1 = []
	divisors2 = []
	for j in range(2,int(math.sqrt(i))+1):
		if i % j == 0:
			divisors1.append(j)
			divisors1.append(i/j)
	sum1=1
	for j in divisors1:
		sum1 += j
	for j in range(2,int(math.sqrt(sum1))+1):
		if sum1 % j == 0:
			divisors2.append(j)
			divisors2.append(sum1/j)
	sum2=1
	for j in divisors2:
		sum2+=j
	if i == sum2 and i != sum1:
		amiNums.add(sum1)
		amiNums.add(sum2)

amiSum = 0
for i in amiNums:
	amiSum += i
print(amiSum)