import math

def check(num):
	for i in range(2,math.floor(math.sqrt(num))):
		if num % i == 0:
			return False
	return True

number = 600851475143
test = math.floor(math.sqrt(number))
largestNum = 0
largestI = 0
i = 3
while (i <= test):
	if number % i == 0:
		temp = number/i
		if temp > largestNum:
			if check(temp):
				largestNum = temp
		if largestNum == 0:
			if check(i):
				largestI = i
	i+=2

print(max(largestNum,largestI))