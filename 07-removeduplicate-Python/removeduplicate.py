# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	text=text[::-1]
	res=""
	for i in range(len(text)):
		if text[i] not in text[i+1::]:
			text.replace(text[i],"")
			res+=text[i]
	return res[::-1]