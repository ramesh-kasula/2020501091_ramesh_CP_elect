# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	# pass
	s1=float( ( (x2-x1)**2+(y2-y1)**2 )**0.5 )
	s2=float(( (x3-x2)**2+(y3-y2)**2 )**0.5)
	s3=float(( (x1-x3)**2+(y1-y3)**2 )**0.5)
	if float(s1)+float(s2)<=float(s3) or float(s2)+float(s3)<=float(s1) or float(s3)+float(s1)<=float(s2):
		return 0
	# pass
	s=(s1+s2+s3)/2
	a=( s*(s-s1)*(s-s2)*(s-s3) )**0.5
	return a