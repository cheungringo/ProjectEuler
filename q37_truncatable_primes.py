'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.'''

def sieveEratosthenes(lower, upper):
	# 0 will mark prime, 1 will mark composite
	array = [0 for x in range(0,upper+1)]
	for x in range(2, upper):
		if array[x] == 1:
			continue
		else:
			for y in range(x**2, upper+1, x):
				array[y] = 1
	primes = []
	for num in range(lower, upper+1):
		if array[num] == 0:
			primes.append(num)
	return primes

import math 

def getPrimes():
	count = 0
	result = []
	primes = sieveEratosthenes(20, 1000000)
	for prime in primes:
		if checkLR(prime) > 0:
			result.append(prime)
			count += 1
		if count == 11:
			break
	return result

def checkLR(prime):
	arr = []
	for digit in str(prime):
		arr.append(str(digit))
	# check removing from right
	for x in range(len(arr)-1):
		# print int(''.join(arr[:len(arr)-1-x]))
		# print int(''.join(arr[x+1:len(arr)]))
		if is_prime(int(''.join(arr[:len(arr)-1-x]))) < 0:
			return -1
		elif is_prime(int(''.join(arr[x+1:len(arr)]))) < 0:
			return -1
	return 1

def is_prime(n):
	if n <= 1:
		return -1
	for x in range(2, int(math.sqrt(n)+1)):
		if n % x == 0:
			return -1
	return 1

primes = getPrimes()

result = 0
for num in primes:
	result += num

print result