# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    # pass
    s1=s1.lower()
    s2=s2.lower()
    if len(set(s1))!=len(set(s2)):
        return False
    for i in s1:
        if s1.count(i)!=s2.count(i):
            return False
    return True

# write your test cases here...
assert(areAnagrams("aba","aab")==True)
assert(areAnagrams("abaa","aaab")==True)
assert(areAnagrams("abba","aaab")==False)
assert(areAnagrams("abac","abab")==False)
assert(areAnagrams("abbca","abcab")==True)
assert(areAnagrams("abbca","abcab")==True)
assert(areAnagrams("abbbca","abbbab")==False)
assert(areAnagrams("abbccaa","acbacab")==True)
assert(areAnagrams("abbceda","abcabed")==True)
print("Test Cases passed")