'''
Stated problem:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 
in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Subproblems: 
Generate all the 10 digit pandigital numbers, 0 first does not count.
Check for each of the conditions above, add to sum if it passes.
'''

import itertools

def GeneratePandigitals(lower, upper):
	'''
	Returns the sum of all the pandigitals of size 10 that satisfy the properties above.
	'''
	sumPandigitals = 0
	base = [x for x in range(lower, upper+1)]
	for pandigital in list(itertools.permutations(base, upper+1)):
		if pandigital[0] == 0:
			continue
		else:
			if CheckPandigital(pandigital):
				number = 0
				for digit in range(len(pandigital)):
					number += pandigital[digit]*10**(upper-digit)
				sumPandigitals += number
	return sumPandigitals

def CheckPandigital(pandigital):
	'''
	Returns whether the pandigital as an integer array passes the conditions given above
	'''
	primes = [2, 3, 5, 7,  11, 13, 17]
	for digit in range(1, 8):
		number = 0
		for x in range(0, 3):
			number += pandigital[digit+x]*10**(2-x)
		if number % primes[digit-1] != 0:
			return False
	return True


print GeneratePandigitals(0, 9)
