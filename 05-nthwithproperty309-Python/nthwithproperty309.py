# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withProperty309(n):
	if n<309:
		return False
	num=n**5
	li=[1,2,3,4,5,6,7,8,9,0]
	for i in li:
		if str(i) not in str(num):
			return False
	return True

def nthwithproperty309(n):
	# Your code goes here
	# pass
	num=308
	c=0
	while c<=n:
		num+=1
		if withProperty309(num):
			c+=1
	return num

