# problem is to find the first ten digits of the sum of the following
# hundred 50 digit numbers. Going to need 50 digit arrays and just do 
# carry adding on them.
input_file = open('q13input.txt', 'r')
numbers = []
for line in input_file:
	number = []
	line = line.rstrip()
	for x in range(len(line)):
		number.append(int(line[x]))
	numbers.append(number)

sum_array = []
carry = 0
for i in range(50):
	currentsum = 0
	for j in range(100):
		currentsum += numbers[j][50-1-i]
	currentsum += carry
	if currentsum > 9:
		ones = currentsum % 10
		carry = currentsum / 10
	else:
		ones = currentsum
		carry = 0
	sum_array.append(ones)

sum_array.append(carry)
first_ten = []
for x in range(9):
	first_ten.append(sum_array[len(sum_array)-1-x])

print first_ten



