# Collapsewhitespaces [10 pts]
# Without using the s.replace() method, write the function 
# collapseWhitespace(s), that takes a string s and returns an 
# equivalent string except that each occurrence of whitespace 
# in the string is replaced by a single space. So, for example, 
# collapseWhitespace("a\t\t\tb\n\nc") replaces the three tabs 
# with a single space, and the two newlines with another single 
# space , returning "a b c ". Here are a few more test cases 
# for you:

# assert(cw("a\nb") == "a b")
# assert(cw("a\n   \t    b") == "a b")
# assert(cw("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
# Once again, do not use s.replace() in your solution. 
# You should not use a regular expression library.

def cw(s):
    # Your code goes here...
    res=""
    for i in range(len(s)):
        if s[i].isalpha():
            if i==len(s)-1:
                res+=s[i]
            else:
                res+=s[i]+" "
    if s[-1].isalpha==False:
        res+=" "
    return res



assert(cw("a\nb") == "a b")
assert(cw("a\n   \t    b") == "a b")
assert(cw("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
print ("All test cases passed...")