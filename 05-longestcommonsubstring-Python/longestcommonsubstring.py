# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    # pass
    x=len(s1)
    y=len(s2)
    maxlen=0
    end=x
    look=[[0]*(y+1)]*(x+1)
    for i in range(x):
        for j in range(y):
            if s1[i]==s2[j]:
                look[i+1][j+1]=look[i][j]+1
                if look[i+1][j+1]>=maxlen:
                    maxlen=look[i+1][j+1]
                    # endind=i
                    end=i+1
    return s1[end-maxlen:end]