# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def powerful(n):
	for i in range(1,n+1):
		if n%i==0 and prime(i)==True:
			if n%(i**2)!=0:
				return False
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	# pass
	num=1
	c=-1
	while(c<n):
		if powerful(num)==True:
			c+=1
		num+=1
	return num-1