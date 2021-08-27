# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidy(n):
    while(n>0):
        a=n%10
        n=n//10
        b=n%10
        if a<b:
            return False
    return True
    # for i in range(len(str(n))):


def fun_nth_tidynumber(n):
    num=0
    c=0
    while(c<=n):
        num+=1
        if tidy(num):
            c+=1
    return num

# print(fun_nth_tidynumber(100))
print(tidy(46))