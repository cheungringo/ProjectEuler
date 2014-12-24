'''The number, 197, is called a circular prime because all rotations 
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

# could easily brute force this and just check if numbers are prime
# however, it's faster to do a prime number sieve to get all the primes below one million
# and then check rotations
import math

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

def findCircular(low, high):
	count = 0
	primes = sieveEratosthenes(low, high)
	for prime in primes:
		prime_as_list = []
		for digit in str(prime):
			prime_as_list.append(digit)
		for x in range(len(prime_as_list)-1):
			# print ''.join(prime_as_list)
			rotate_right(prime_as_list)
			# print ''.join(prime_as_list)
			if is_prime(int(''.join(prime_as_list))) < 0:
				count -= 1
				break
		count += 1
	return count

def rotate_right(l):
	# rotates list l once to the right
	last = l[len(l)-1]
	for index in range(len(l)-1, 0, -1):
		l[index] = l[index-1]
	l[0] = last

def is_prime(n):
	for x in range(2, int(math.sqrt(n)+1)):
		if n % x == 0:
			return -1
	return 1

print str(13 + findCircular(100, 1000000))