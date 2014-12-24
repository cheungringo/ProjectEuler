'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and 
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the 
value of the denominator.'''

# we can check by comparing 12 to the twenties, so basically mod by 10 and then multiply by 10
# and do comparisons by 10

def findFrac():
	fractions = []
	for numerator in range(12, 90):
		ones = numerator % 10
		new_tens = ones * 10
		for denominator in range(new_tens + 1, new_tens + 10):
			if (float(numerator)/denominator == float(numerator/10)/(denominator%10)) and numerator != denominator:
				fractions.append(str(numerator) + '/' + str(denominator))
	return fractions

print findFrac()

