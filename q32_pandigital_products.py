'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'''

# first off, only need to check up to 2 x 3 numbers since the minimum 3x3 sum
# 100 x 100 would be at minimum 10,000 and 3 + 3 + 5 > 9 
# similarly, also 2 x 2 will be at most 99 x 99 = 9801 meaning 2x2 digits meaning < 9
# therefore only need to check 2x3 numbers
# idea will be to go through all 2x3 products will be 90 * 900 = 81, 000 possibilities
# can optimize by excluding a lot. 
# we can either have 1x4 or 2x3, just try for both

def pandigital():
	pandigitals = []
	for x in getPans(10, 100, 100, 1000):
		if x not in pandigitals:
			pandigitals.append(x)
	for x in getPans(2, 10, 1000, 10000):
		if x not in pandigitals:
			pandigitals.append(x)
	return pandigitals

def getPans(a, b, c, d):
	pandigitals = []
	for multiplier in range(a, b):
		for multiplicand in range(c, d):
			product = multiplier*multiplicand
			total_str = str(multiplier) + str(multiplicand) + str(product)
			digits = []
			for digit in total_str:
				digits.append(int(digit))
			if 0 in digits or len(set(digits)) != 9:
				continue
			if product not in pandigitals:
				if product > 1000 and product < 9999:
					pandigitals.append(product)
	return pandigitals

pandigitals = pandigital()
print pandigitals
total = 0
for x in pandigitals:
	total += x

print total

