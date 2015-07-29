'''
Stated Problem:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Main problem: 2^1000 is too large to fit into one number. 
Solution: Use an array with each element being one digit, then just sum the array at the end.
Runtime: 1000 multiplication operations along with an n-digit sum.
'''

def MultiplyArray(array, factor):
	''' 
	Multiplies the array by the factor and returns the product array.
	The array is assumed to be read from left to right as if a normal number.
	'''
	length = len(array)
	carry = 0
	for i in range(len(array)-1, -1, -1):
		product = array[i]*2
		if product + carry < 10:
			array[i] = product + carry 
			carry = 0
		else:
			array[i] = product + carry - 10
			carry = (product + carry) // 10
	if carry > 0:
		array.insert(0, carry)
	return array

def ArraySum(array):
	'''
	Adds the elements in the array and returns the sum.
	'''
	arraySum = 0
	for i in range(len(array)):
		arraySum += array[i]
	return arraySum

def powerDigitSum(base, exponent):
	'''
	Returns the sum of digits in the power calculated by raising the base to an exponent
	'''
	array = [1]
	for i in range(exponent):
		array = MultiplyArray(array, base)
	return ArraySum(array)

print(powerDigitSum(2, 1000))




