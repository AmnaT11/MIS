def gcd(a,b):
	t = b
	b = a % b
	
	if b == 0:
		return t
	else:
		return gcd(t,b)
		
print(gcd(16,24)) 