'''Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

a and b can be negative

Considering quadratics of the form:

n**2 + an + b, where abs(a) < 1000 and abs(b) < 1000

where abs(n) is the modulus/absolute value of n
e.g. abs(11) = 11 and abs(4) = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces 
the maximum number of primes for consecutive values of n, starting with n = 0.'''

# this seems relatively straightforward and easy to do with a brute force function
# there are 2000*2000 possibilities which is a piece of cake for the computer. As soon 
# as a number is not prime, then it can return the consecutive primes
def check_Quadratic(a, b):
	'''returns the number of consecutive primes
	starting at n = 0 that the quadratic formula
	n**2 + a*n + b produces'''
	consecutive = 0
	n = 0
	# import q7
	while is_prime(n**2+a*n+b):
		n += 1
		consecutive += 1
	return consecutive

def is_prime(n):
	if n == 0:
		return False
	if n < 0:
		return False
	for i in range(3,int(n**.5)+1,2):
		if not n % i:
			return False
	return True

longest = 0
product = 0
for a in range(-1000, 1000):
	for b in range(-1000, 1000):
		current = check_Quadratic(a, b)
		if current > longest:
			print "Most consecutive primes: " + str(current) + " a: " + str(a) + " b: " + str(b)
			longest = current
			product = a*b

print product