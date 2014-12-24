'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''

# can stop at 9!*7 since it has seven digits
# this implementation is kinda slow

def get_factorial(n):
	if n == 0 or n == 1:
		return 1
	return n*get_factorial(n-1)

factorials = {}
for x in range(0, 10):
	factorials[x] = get_factorial(x)

def findDigitFact():
	Sum = 0
	for num in range(3, factorials[9]*7):
		total = 0
		for digit in str(num):
			total += factorials[int(digit)]
		if total == num:
			Sum += total
	return Sum

print findDigitFact()