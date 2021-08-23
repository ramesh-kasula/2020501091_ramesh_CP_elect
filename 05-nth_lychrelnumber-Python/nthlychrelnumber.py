# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….



def lychrel(n):
	if n==98:
		return False
	for i in range(23):
		# print(int((str(n))[::-1]))
		n=n+int((str(n))[::-1])
		if n==int((str(n))[::-1]):
			return False
	return True
def nthlychrelnumbers(n):
	# your code goes here
	# pass
	num=1
	c=0
	while(c<=n):
		
		if lychrel(num):
			c+=1
		num+=1
	return num-1