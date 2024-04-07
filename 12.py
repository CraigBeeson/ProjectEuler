import math

currentNum = 0
solved = False
i = 1

while(not solved):
	currentNum += i
	divisorCount = 0
	if math.sqrt(currentNum) <= 251:
		pass
	else:
		for j in range(2,int(math.sqrt(currentNum))):
			if currentNum % j == 0:
				divisorCount += 2
		if divisorCount >= 500:
			solved = True
	i += 1

print(currentNum)