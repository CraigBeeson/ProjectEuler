import math

a = 0
b = 0
c = 0

for i in range(200,400):
	if a != 0:
		break
	for j in range(200,400-(i-200)):
		tempA = i
		tempB = j
		tempC = math.sqrt(i**2 + j**2)
		if (tempA+tempB+tempC == 1000.0):
			a = tempA
			b = tempB
			c = tempC

print(a*b*c)