'''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

# only thing I can think of for this solution is brute forcing it
# question is just what number to stop at
# we can stop at 354294 since (9^5) * 6 is 6 digits, meaning we cannot get to 7 digits using a sum
# of 9^5 7 times which is actually the greatest possible sum in 7 digits meaning that anything less
# than 9,999,999 will not satisfy this criteria

def getSum(power):
	maximum = (9**power)*6
	result = 0
	for number in range(2, maximum):
		str_number = str(number)
		total = 0
		for digit in str_number:
			total += int(digit)**power
		if total == number:
			result += number

	return result

print getSum(5)

