# find sum of all primes below 2 million


def is_prime(n):
	for i in range(3,int(n**.5)+1,2):
		if not n % i:
			return False
	return True

def sum_primes(n):
	primes = [2, 3, 5, 7, 11, 13]
	pysum = 2 + 3 + 5 + 7 + 11 + 13
	i = 15
	while 1:
		if is_prime(i):
			if i >= n:
				break
			pysum += i
		i += 2
	return pysum

n = int(raw_input("Find sum of primes below n: "))
print sum_primes(n)