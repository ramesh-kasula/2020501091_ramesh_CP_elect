# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# Your code goes here
	rSL=[]
	sr=0
	for i in range(len(L)):
		sr+=sum(L[i])
		rSL.append(sr)
		sr=0
	for i in range(len(rSL)):
		if rSL.count(rSL[i])==1:
			row=i
	# print(row)
	cr=0
	cSL=[]
	for i in range(len(L)):
		for j in range(len(L)):
			cr+=L[j][i]
		cSL.append(cr)
		cr=0
	# print(cSL)
	for i in range(len(cSL)):
		if cSL.count(cSL[i])==1:
			col=i
	# print(row,col)
	if row!=len(L)-1:
		d=sum(L[row])-sum(L[row+1])
	else:
		d=sum(L[row])-sum(L[row-1])
	L[row][col]-=d
	return L
print(fixmostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 18], [9, 6, 7, 12],[4, 15, 14, 1]]))