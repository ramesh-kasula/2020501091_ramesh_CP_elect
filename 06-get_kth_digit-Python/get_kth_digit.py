# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	if len(str(digit))<k:
		return 0
	digit=abs(digit)
	r=0
	for i in range(k+1):
		r=digit%10
		digit=digit//10
	return r