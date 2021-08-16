# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	# pass
	for i in range(len(str(n))-1):
		if str(n)[i]==str(n)[i+1]:
			return True
	return False