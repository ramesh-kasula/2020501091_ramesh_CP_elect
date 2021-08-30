# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	# pass
	n=abs(n)
	c=1
	num=0
	maxc=0
	while n>0:
		a=n%10
		n=n//10
		b=n%10
		if a==b:
			c+=1
		else:
			if maxc==c:
				if num>=a:
					num=a
			elif(maxc<c):
				maxc=c
				num=a
			c=1
	return num

print(longestdigitrun(117773732))
print(longestdigitrun(677886))