import math
sum = 2
i = 3
while(i < 2000000):
	tempA = int(math.sqrt(i))
	isPrime = True
	for j in range(2,tempA+1):
		if (i%j == 0):
			isPrime = False
	if isPrime:
		sum += i
	i+=2

print(sum)