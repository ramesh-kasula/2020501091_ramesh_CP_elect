# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math


def isKaprekar(n):
    if(n==1):
        return True
    dc=len(str(n*n))
    sq=n*n
    for i in range(dc-1):
        p=10**(i+1)
        if(p==n):
            continue
        s=(sq//p)+(sq%p)
        if(s==n):
            return True
    return False

def fun_nearestkaprekarnumber(n):
    a=n
    b=n
    cl=0
    cr=0
    
    while( isKaprekar(a)==False):
        # print(a)
        cl+=1
        a-=1
    while(isKaprekar(b) == False):
        cr+=1
        b+=1
    if cl<=cr:
        return a
    return b
