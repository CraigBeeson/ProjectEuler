import math
lcm = 1
for i in range(2,20):
	lcm = int((lcm * i)/math.gcd(lcm,i))

print(lcm)