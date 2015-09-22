'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them 
in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

def checkCombos(array, n):
	if not isPrime(n):
		return False
	for x in range(len(array)):
		if not isPrime(int(str(array[x]) + str(n))):
			return False
		if not isPrime(int(str(n) + str(array[x]))):
			return False
	return True

def isPrime(n):
	for x in range(2, int(n**(.5))+1):
		if n % x == 0:
			return False
	return True

def recursivelyAppend(array, length, cap):
	if len(array) >= length:
		return array
	for x in range(3, cap, 2):
		curLength = len(array)
		if checkCombos(array, x):
			array.append(x)
			result = recursivelyAppend(array, length, cap)
			if result != None:
				return result
			while len(array) > curLength:
				del array[-1]
	return None

def solveProblem(length, cap, start_cap):
	start_val = 7
	while start_val < start_cap:
		if not isPrime(start_val):
			start_val += 2
			continue
		print start_val
		result = 10000000
		new = recursivelyAppend([start_val], length, cap)
		if new == None:
			start_val += 2
			continue
		total = 0
		for x in range(5):
			total += new[x]
		if total < result:
			result = total
		start_val += 2
	return result

print solveProblem(5, 10000, 15)