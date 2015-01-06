'''Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , n) where n > 1?
'''

# we get some hints off the bat. we know that the first number 
# has to be a 9 which eliminates a lot of possibilities
# next we can use an integer and keep multiplying by 1 2 3 .. n 
# and check if pandigital until the length of the number 
# exceeds 9, then we go to the next one since we have to 
# have n >= 2, the max digit size is 4. We do not need to check 
# anything past 9999 since 5 digits twice will give 10 digits, 
# exceeding the rules of the problems

def isPandigital(num):
	'''takes in number as array and checks if pandigital
	returns True or False'''
	if len(num) != 9:
		return False
	for digit in range(1, 10):
		if digit not in num:
			return False
	return True
def getPandigital():
	'''gets the largest pandigital that can be made by
	multiplying consecutive numbers'''
	greatest = 0
	for num in range(1, 10000):
		current = []
		for digit in str(num):
			current.append(int(digit))
		n = 2
		while len(current) < 9:
			for digit in str(n*num):
				current.append(int(digit))
			n += 1
		if isPandigital(current):
			for x in range(len(current)):
				current[x] = str(current[x])
			new = ''.join(current)
			if int(new) > greatest:
				greatest = int(new)
				print greatest
	return greatest
print getPandigital()
'''
# test isPandigital
yes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
no = [1, 2, 3, 4, 5, 6]
no2 = [3, 3, 3, 4]
print isPandigital(yes)
print isPandigital(no)
print isPandigital(no2)'''


