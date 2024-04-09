namesTxt = ""
names = []
with open("names.txt",'r') as f:
	namesTxt = f.read().replace("\"", "")
	f.close()
names = namesTxt.split(",")
names.sort()
nameValSum = 0
for i in range(0,len(names)):
	temp = 0
	for j in [ord(val)-64 for val in names[i]]:
		temp += j
	nameValSum += temp * (i+1)

print(nameValSum)