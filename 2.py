sumResult = 0
term = 2
prevTerm = 1

def getNextTerm(arg1,arg2):
	global term 
	term = arg1+arg2
	global prevTerm
	prevTerm = arg2

while(term <= 4000000):
	if term%2==0:
		sumResult += term
	getNextTerm(prevTerm,term)

print(sumResult)