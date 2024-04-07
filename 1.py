sumResult = 0
numbers = []
i = 1
while(i):
	result = i*5
	if result >= 1000:
		break
	else:
		numbers.append(result)
	i+=1
i=1
while(i):
	result = i*3
	if result >= 1000:
		break
	else:
		if result in numbers:
			pass
		else:
			numbers.append(result)
	i+=1
total = 0
for i in numbers:
	total += i
print("total: " + str(total))