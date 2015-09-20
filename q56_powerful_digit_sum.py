'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

def numToList(n):
	array = []
	while n > 0:
		array.insert(0, n % 10)
		n /= 10
	return array

def multLists(power, exponent):
	arrays = []
	for x in range(len(exponent)-1, -1, -1):
		array = []
		carry = 0
		for z in range(len(exponent) - 1- x):
			array.insert(0, 0)
		for y in range(len(power)-1, -1, -1):
			product = exponent[x] * power[y] + carry
			if product > 9:
				carry = product / 10
			else:
				carry = 0
			array.insert(0, product % 10)
		if carry > 0:
			array.insert(0, carry)
		arrays.append(array)
	return arrays

def padFront(a, b):
	while (len(a) < len(b)):
		a.insert(0, 0)
	while (len(b) < len(a)):
		b.insert(0, 0)

def addLists(a, b):
	result = []
	carry = 0
	for x in range(len(a)-1, -1, -1):
		temp = a[x] + b[x] + carry
		if temp > 9:
			carry = 1
		else:
			carry = 0
		result.insert(0, temp % 10)
	if carry > 0:
		result.insert(0, carry)
	return result

def multiply(longer, twoDigit):
	results = multLists(longer, twoDigit)
	padFront(results[0], results[1])
	result = addLists(results[0], results[1])
	return result

def sumList(a):
	total = 0
	for x in range(len(a)):
		total += a[x]
	return total

def findPowerfulDigitSum():
	digitSum = 0
	# starting at 11 since I'm pretty sure the base will be at least 11
	for base in range(11, 100):
		arrayBase = numToList(base)
		for exponent in range(2, 100):
			arrayExponent = numToList(base)
			arrayBase = multiply(arrayBase, arrayExponent)
			total = sumList(arrayBase)
			if (total > digitSum):
				digitSum = total
	return digitSum

print findPowerfulDigitSum()


