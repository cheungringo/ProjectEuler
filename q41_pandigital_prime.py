'''
Stated Problem:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
Subproblems:
Determine whether or not a number is prime
Generate pandigital primes in descending order starting with 987654321
Possible shortcuts: can't end in even number, so eliminate if the last digit is even
Solution:
Generate pandigital primes lexicographically in descending order
Check if prime
'''

import itertools

'''
An implementation of itertools.permutations, basically a recursive subarray generation algorithm:
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
'''

def IsPrime(number):
	'''
	Returns True if the number is prime and False if it is composite
	'''
	if number < 3:
		return False
	if number % 2 == 0:
		return False
	for factor in range(3, int((number**(.5)+1)//1), 2):
		if number % factor == 0:
			return False
	return True

def GeneratePandigitals(n):
	'''
	Returns an array of all the uneven pandigitals of size n
	'''
	pandigitals = []
	base = [x for x in range(1, n+1)]
	for pandigital in list(itertools.permutations(base, n)):
		if pandigital[n-1] % 2 == 0:
			continue
		else:
			number = 0
			for digit in range(len(pandigital)):
				number += pandigital[digit]*10**(n-digit-1)
			pandigitals.append(number)
	return pandigitals

def PandigitalPrime():
	'''
	Returns the greatest n digit pandigital prime
	'''
	for n in range(9, 0, -1):
		for pandigital in list(reversed(GeneratePandigitals(n))):
			if IsPrime(pandigital):
				return pandigital

print PandigitalPrime()
	
		


