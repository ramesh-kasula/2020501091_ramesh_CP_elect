# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	# Your code goes here
	# pass
	c1=1
	c2=0
	for i in range(1,len(L)):
		if L[i]==L[i-1]:
			c1+=1
		if c1>=k:
			j=i
			while(c1!=c2 and L[j]==L[j-1]):
				j+=1
				c2+=1
			L[i],L[j]=L[j],L[i]
			c1=1
	s=len(L)-c2
	return L[0:s]