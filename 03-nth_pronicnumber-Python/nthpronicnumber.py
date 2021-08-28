# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronic(n):
	for i in range(int(n/2)+1):
		if i*(i+1)==n:
			return True
	return False

def nthpronicnumber(n):
	# Your code goes here
	# pass
	num=0
	c=1
	while(c<=n):
		num+=1
		if pronic(num):
			c+=1
	return num

print(nthpronicnumber(6))