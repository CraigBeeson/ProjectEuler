palindrome = 0
i = 999
j = 999
while(not palindrome):
	step = i*j
	if str(step) == str(step)[::-1]:
		palindrome = step
	j -= 1
	if j == 900:
		i -= 1
		j = i

print(palindrome)