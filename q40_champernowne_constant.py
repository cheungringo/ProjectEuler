'''An irrational decimal fraction is created by concatenating the 
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find 
the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000'''

# strategy is to just iterate through the numbers multiplying by 
# ten each time we find and multiply the previous power of ten
def getProduct():
	product = 1 
	current = 1 # stores the current number, incremented by 1
	next = 10 # stores the next power of ten that we want
	which_digit = 1 # tells us which digit we are at right now
	# when we get to next we get the digit with formula
	# which_digit - next + 1 from the end
	num_digits = 1 # is updated at end of loop if all digits in
	# number are 9
	while which_digit <= 1000000:
		current += 1
		which_digit += num_digits
		if which_digit >= next:
			product *= int(str(current)[-(which_digit-next+1)])
			next *= 10
		flag = True # now check if we need to increment num_ digits
		for digit in str(current):
			if int(digit) != 9:
				flag = False
		if flag == True:
			num_digits += 1
	return product

print getProduct()





