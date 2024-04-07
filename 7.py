import math

primeCount = 2
currentNum=3

while(primeCount < 10001):
	currentNum += 2
	prime = True
	for i in range(2,math.floor(math.sqrt(currentNum)+1.0)):
		if currentNum % i == 0:
			prime = False
	if prime:
		primeCount += 1
print(currentNum)