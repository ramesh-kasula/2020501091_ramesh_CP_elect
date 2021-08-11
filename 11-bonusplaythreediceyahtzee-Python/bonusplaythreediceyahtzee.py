# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))


def handtodice(hand):
	# your code goes here
	res=[]
	for i in range(len(str(hand))):
		d=hand%10
		hand=hand//10
		res.append(d)
	return tuple(res[::-1])

def dicetoorderedhand(a, b, c):
	# your code goes here
	l=sorted([a,b,c])
	s=str(l[0])+str(l[1])+str(l[2])
	# print(int(s))
	return int(s[::-1])

def han(l):
	res=[]
	if l[0] == l[1] and l[1]==l[2]:
			res.append(l[0])
			res.append(l[1])	
			res.append(l[2])
			return res	
	for i in range(len(l)-1):
		if l[i] == l[i+1]:
			res.append(l[i])
			res.append(l[i+1])
	
	return res
	
def playstep2(hand, dice):
	# your code goes here
	l1=[]
	l2=[]
	for i in range(len(str(hand))):
		d=hand%10
		hand=hand//10
		l1.append(d)
	print(l1)
	if len(l1)==len(set(l1)):
		res1=max(l1)
	else:
		res1=han(l1)
	for i in range(len(str(dice))):
		d=dice%10
		dice=dice//10
		l2.append(d)
	l2=l2[::-1]
	print(l2)
	if type(res1)==list:
		if len(res1)==2:
			res1.append(l2[len(l2)-1])		
		r1=sorted(res1)[::-1]
		r2=l2[0:len(l2)-1]
		n1=0
		n2=0
		for i in range(len(r1)):
			n1+=r1[i]*10**((len(r1)-1)-i)
		for i in range(len(r2)):
			n2+=r2[i]*10**((len(r2)-1)-i)
		return (n1,n2)
	else:
		res2=[]
		res2.append(res1)
		res2.append(l2[len(l2)-1])
		res2.append(l2[len(l2)-2])
		r1=sorted(res2)[::-1]
		r2=l2[0:len(l2)-2]
		n1=0
		n2=0
		for i in range(len(r1)):
			n1+=r1[i]*10**((len(r1)-1)-i)
		for i in range(len(r2)):
			n2+=r2[i]*10**((len(r2)-1)-i)
		return (n1,n2)
def score(h):
	a=h%10
	x=h//10
	b=x%10
	x=x//10
	c=x%10
	if a!=b and b!=c and c!=a:
		return max(a,b,c)
	elif ((a==b and b!=c) or (b==c and c!=a)):
		return 10+b+b
	elif a==b and b==c:
		return 20+c+c+c
	

def bonusplaythreediceyahtzee(dice):
	# Your code goes here
	hand1=dice%1000
	dice1=dice//1000
	m,n=playstep2(hand1,dice1)
	o,p=playstep2(m,n)
	s=score(o)
	return(o,s)