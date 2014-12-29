'''A palindromic number reads the same both ways. The largest 
palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit 
numbers.'''

# Answer 906609

# need a function isPalindrome, then just run through all 
# 900 * 900 possibilities only 180,000 

def isPalindrome(num):
	length = len(str(num))
	for i in range(length/2):
		if int(str(num)[i]) != int(str(num)[length-1-i]):
			return -1
	return 1

def largest():
	greatest = 1
	for a in range(100, 1000):
		for b in range(100, 1000):
			product = a*b
			if isPalindrome(product) > 0 and product > greatest:
				greatest = product
	return greatest


print largest()