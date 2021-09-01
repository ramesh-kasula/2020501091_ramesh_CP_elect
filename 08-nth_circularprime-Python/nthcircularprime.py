# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def circular(n):
	if "0" in str(n):
		return False
	d=len(str(n))
	for i in range(d):
		s=str(n)
		s=s[-1]+s[:len(s)-1]
		n=int(s)
		if prime(n)==False:
			return False
	return True
		

def nthcircularprime(n):
	# Your code goes here
	# pass
	if n==1:
		return 2
	if n==2:
		return 3
	if n==3:
		return 5
	if n==4:
		return 7
	num=0
	c=0
	while(c<=n):
		num+=1
		if circular(num):
			c+=1
	return num