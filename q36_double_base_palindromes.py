'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

# just need to check if decimal palindromic AND binary palindromic. 
# need a decimal to binary converter
def dectoBin(n):
	''' returns an array representation of the binary'''
	base = 2
	binary = []
	while n > 0:
		remainder = n % 2
		if remainder == 0:
			binary.append(0)
		else:
			binary.append(1)
		n /= 2
	return binary

def getPals(high):
	pals = []
	for num in range(1, high):
		flag = 1
		decimal = []
		for digit in str(num):
			decimal.append(digit)
		for index in range(len(decimal)/2):
			if decimal[index] != decimal[len(decimal)-1-index]:
				flag = 0
		if flag == 0:
			continue
		binary = dectoBin(num)
		for index in range(len(binary)/2):
			if binary[index] != binary[len(binary)-1-index]:
				flag = 0
		if flag == 1:
			print binary
			pals.append(num)
	return pals

pals = getPals(1000000)

result = 0
for number in pals:
	result += number

print result

