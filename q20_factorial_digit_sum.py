'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
# just write out long multiplication method

def sum_factorial_digits(num):
	product = [3, 6, 2, 8, 8]
	for x in range(11, num+1):
		carry = 0
		ones = x % 10
		tens = x / 10
		temp_ones = []
		temp_tens = [0] 
		# this loop does the multiplication for the ones digit against current product
		length = len(product)
		for y in range(length):
			temp_product = (ones*product[length-1-y] + carry) % 10
			carry = (ones*product[length-1-y]+carry) /10
			temp_ones.insert(0, temp_product)
		if carry > 0:
			temp_ones.insert(0, carry)
		# temp_ones will have an array of the product of ones in order
		carry = 0 # reset carry for the temp_tens array
		# this loop does multi for the tens digit against current product
		for y in range(length):
			temp_product = (tens*product[length-1-y] + carry) % 10
			carry = (tens*product[length-1-y]+carry) /10
			temp_tens.insert(0, temp_product)
		if carry > 0:
			temp_tens.insert(0, carry)
		# temp_tens will have array of the product of tens in order
		# even out length of tens and ones
		while True:	
			if len(temp_tens) > len(temp_ones):
				temp_ones.insert(0, 0)
			elif len(temp_tens) < len(temp_ones):
				temp_tens.insert(0, 0)
			else:
				break
		carry = 0
		length = len(temp_tens)
		product = []
		zeros = True
		# now just add temp_tens and temp_ones and put result into product
		for x in range(length):
			#if (temp_ones[-1-x] + temp_tens[-1-x] + carry)%10 == 0:
			#	if zeros:
			#		continue
			#zeros = False
			product.insert(0, (temp_ones[-1-x] + temp_tens[-1-x] + carry)%10)
			carry = (temp_ones[-1-x] + temp_tens[-1-x] + carry) /10
		if carry > 0:
			product.insert(0, carry)
	final = 0
	for x in range(len(product)):
		final += product[x]
	print product
	print final
	
sum_factorial_digits(100)
