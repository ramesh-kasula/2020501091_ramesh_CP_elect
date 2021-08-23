# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def happy(n):
	if n==1:
		return 1
	res=0
	while n>0:
		a=n%10
		n=n//10
		res+=a**2
	return res
def happyPrime(n):
	res=0
	for i in range(n//2):
		res=happy(n)
		if res==1:
			return True
		n=res
	return False
def fun_nth_happy_prime(n):
	if n==0:
		return 7
	a=-1
	c=0
	while c<n:
		a+=1
		if(happyPrime(a) and prime(a)):
			c+=1
	return a