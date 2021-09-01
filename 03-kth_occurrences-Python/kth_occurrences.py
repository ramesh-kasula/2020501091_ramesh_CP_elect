# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

def fun_kth_occurrences(s, n):
	d=dict()
	for i in s:
		if not i.isalpha():
			pass
		elif(i in d):
			d[i]+=1
		else:
			d[i]=1
	c=1
	while c<n:
		maxn=max(d.values())
		for k,v in d.items():
			if maxn==v:
				d[k]=0
				c+=1
				print(d)
	for k,v in d.items():
		if v==max(d.values()):
			return k
	return ""



print(fun_kth_occurrences("helllo woorld",2))