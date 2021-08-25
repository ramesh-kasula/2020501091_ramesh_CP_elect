# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def isKaprekar(n):
    if n==1:
        return True
    sqn=n**2
    for i in range(len(str(sqn))-1):
        if 10**(i+1)==n:
            continue
        s=(sqn//10**(i+1))+(sqn%10**(i+1))
        if s==n:    
            return True
        return False
def fun_nth_kaprekarnumber(n):
    num=0
    c=0
    while c<=n:
        num+=1
        if(isKaprekar(num)==True):
            c+=1
    return num