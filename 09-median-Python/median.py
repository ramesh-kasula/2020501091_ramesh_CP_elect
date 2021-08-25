# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	# pass
	a=sorted(a)
	if len(a)<1:
		return None
	if len(a)%2==0:
		x=a[(len(a)//2)-1]
		y=a[len(a)//2]
		return (x+y)/2
	return a[len(a)//2]