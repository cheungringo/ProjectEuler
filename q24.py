'''
A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
# write a function to find all the permutations of 
# the algorithm is to compute the factorials that fit into 1000000 to get each digit 

def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n-1)

def lexicographic(nth_perm):
	permutation = []
	possible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	first = 9
	while nth_perm > 0:
		if first == 1:
			break
		if factorial(first) >= nth_perm:
			permutation.append(possible.pop(0))
			first -= 1
			continue
		remainder = nth_perm % factorial(first)
		if remainder == 0: 
		# if remainder is 0, then it's the last permutation of the PREVIOUS digit
			current_digit = possible.pop(nth_perm / factorial(first)-1)
		else:
			current_digit = possible.pop(nth_perm / factorial(first))
		permutation.append(current_digit)
		nth_perm = remainder
		first -= 1
	for x in range(len(possible)-1, -1, -1):
		permutation.append(possible[x])
	return permutation

for x in range(1000, 2000):
	print lexicographic(x)
