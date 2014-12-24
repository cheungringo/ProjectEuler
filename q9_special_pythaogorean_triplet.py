'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# find the product of a pythagorean triple whose sum is 1000
# Use Euclid's Formula stating that for any two integers m, n where m > n
# there is a pythagoren triple a, b, c, where a = m**2 - n**2, b = 2mn, c = m**2 + n**2

pysum = int(raw_input())
ceiling = int(raw_input("Enter ceiling: (20 is usually good)"))
m = 2
n = 1
a = 3
b = 4
c = 5
incrementCounter = 1
while (pysum % (a + b + c) != 0):
	if (incrementCounter == -1):
		n += 1
		m = n + 1
		incrementCounter *= -1
	elif (m == ceiling):
		incrementCounter *= -1
	elif (m < ceiling):
		m += 1
	a = m**2 - n**2
	b = 2*m*n
	c = m**2 + n**2
print a, b, c
k = pysum / (a+b+c)
product = k*a*k*b*k*c
print product

