# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    # pass
    if len(lst)!=len(lst[0]):
        return False
    for i in lst:
        if len(i)!=len(set(i)):
            return False
    r=[]
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            r.append(lst[i][j])
        if len(r)!=len(set(r)):
            return False
        r=[]
    return True


lst=[['1','2','3'],['2','3','1'],['3','1','2']]
lst2=[['1','2','3'],['2','3','1'],['3','1','1']]
lst3=[['1','2','3'],['2','2','1'],['3','2','2']]
lst4=[['1','2','3','4'],['2','2','1'],['3','2','2']]

assert(isLatinSquare(lst)==True)
assert(isLatinSquare(lst2)==False)
assert(isLatinSquare(lst3)==False)
assert(isLatinSquare(lst4)==False)
print("Test Cases Passed..!!!")