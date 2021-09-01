# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def happy(n):
	if n==1:
		return 1
	res=0
	while n>0:
		a=n%10
		n=n//10
		res+=a**2
	return res
def ishappynumber(n):
	# your code goes here
	# pass
	if n==1 or n==7:
		return True
	res=0
	for i in range((n//2)+1):
		res=happy(n)
		if res==1:
			return True
		n=res
	return False
def nth_happy_number(n):
	if n==1:
		return 1
	num=0
	c=1
	while(c<=n):
		num+=1
		if ishappynumber(num):
			c+=1
	return num
