'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
1393/985, is the first example where the number of digits in the numerator exceeds 
the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''
# will store fractions in an array with numerator as element 0 and denominator as element one
def getNextElement(fraction):
	# first add one
	denom = fraction[0] + fraction[1]
	# then flip the fraction
	fraction[0] = fraction[1]
	fraction[1] = denom
	fraction[0] += fraction[1]
	return fraction

def getNumDigits(n):
	numDigits = 0
	while n > 0:
		n /= 10
		numDigits += 1
	return numDigits

def checkExpansions(n):
	fraction = [3, 2]
	count = 0
	for x in range(1, n):
		fraction = getNextElement(fraction)
		if (getNumDigits(fraction[0]) > getNumDigits(fraction[1])):
			count += 1
	return count


print checkExpansions(1000)

