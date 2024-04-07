currentNum = 999999
maxSteps = 1
maxStepsNum = 0
while currentNum > 800000:
	temp = currentNum
	steps = 1
	while temp > 1:
		if temp % 2 == 0:
			temp = temp//2
		else:
			temp = (temp * 3) + 1
		steps += 1
	if maxSteps < steps:
		maxSteps = steps
		maxStepsNum = currentNum
	currentNum -= 2

print(maxStepsNum)
	