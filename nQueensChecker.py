# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN chessboard such that no two queens are attacking each other. For most values of N, there are many ways to solve this problem. Here, you will write the function nQueensChecker(board) that takes a 2d list of booleans where True indicates a queen is present and False indicates a blank cell, and returns True if this NxN board contains N queens all of which do not attack any others, and False otherwise.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	# pass
	if qR==oR or qC==oC or abs(qR-oR)==abs(qC-oC):
		return True
	return False

def nQueensChecker(a):
    # Your code goes here...
    # pass
    l=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]==True:
                l.append((i,j))
    # print(l[0][0])
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if canqueenattack(l[i][0],l[i][1],l[j][0],l[j][1])==True:
                return False
    return True

assert(nQueensChecker([[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]])==True)
assert(nQueensChecker([[False,True,True,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]]
)==False)
print("Test Cases Passed")
