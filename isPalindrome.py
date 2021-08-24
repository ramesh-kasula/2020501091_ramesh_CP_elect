# Note: isPalindromicPrime branch is not there as part of the Github branch. We request you to create a branch and then write your solution. Here is the problem description.
# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")

def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def isPalindromicPrime(n):
    rn=str(n)[::-1]
    rn=int(rn)
    if rn==n and prime(n):
        return True
    return False

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")