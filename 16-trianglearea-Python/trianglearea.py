# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

def trianglearea(s1, s2, s3):
	# your code goes here
	s1=float(s1)
	s2=float(s2)
	s3=float(s3)
	if float(s1)+float(s2)<=float(s3) or float(s2)+float(s3)<=float(s1) or float(s3)+float(s1)<=float(s2):
		return 0
	# pass
	s=(s1+s2+s3)/2
	a=( s*(s-s1)*(s-s2)*(s-s3) )**0.5
	return a