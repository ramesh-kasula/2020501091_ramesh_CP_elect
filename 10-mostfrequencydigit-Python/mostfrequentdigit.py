# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	# pass
	if len(str(n))==len(set(str(n))):
		return int(min(str(n)))
	res=dict()
	for i in range(len(str(n))):
		res[str(n)[i]]=str(n).count((str(n))[i])
	print(res)
	ress=[]
	for key,i in res.items():
		if int(i) == int(max(res.values())):
			ress.append(int(key))
	if len(ress)<2:
		return ress[0]
	else:
		return min(ress)