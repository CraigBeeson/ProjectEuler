singles = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
}
tens = {
	2: "twenty",
	3: "thirty",
	4: "forty",
	5: "fifty",
	6: "sixty",
	7: "seventy",
	8: "eighty",
	9: "ninety",
}
betweeners = {
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
}
lCount = 0
for i in range(1,1001):
	if i == 1000:
		lCount += len("onethousand")
	else:
		tempS = ""
		if i >= 100:
			temp = i//100
			tempS += singles[temp] + "hundred"
			if i%100 >= 20:
				temp = (i%100)//10
				tempS += "and" + tens[temp]
				if i%10 > 0:
					tempS += singles[i%10]
			elif (i%100 <= 20) and (i%100 >= 10):
				temp = i%100
				tempS += "and" + betweeners[temp]
			elif i%100 > 0:
				temp = i%100
				tempS += "and" + singles[i%100]
		elif i >= 20:
			temp = i//10
			tempS += tens[temp]
			if i%10 > 0:
				tempS += singles[i%10]
		elif (i <= 20) and (i >= 10):
			tempS += betweeners[i]
		else:
			tempS += singles[i]
		lCount += len(tempS)

print(lCount)