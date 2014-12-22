'''What is the first term in the Fibonacci sequence to contain 1000 digits?'''


def largeFibonacci(n):
	'''computes first fibonacci numbers with 1000 digits'''
	prev = [1]
	current = [1]
	current_n = 2
	while len(current) != n:
		# pad previous with zeros if its too short
		different = len(current) - len(prev)
		for x in range(different):
			prev.insert(0, 0)
		carry = 0
		next = []
		for x in range(len(current)-1, -1, -1):
			_sum = current[x] + prev[x] + carry
			next.insert(0, _sum % 10)
			carry = _sum / 10
		if carry > 0:
			next.insert(0, carry)
		prev = current
		current = next
		current_n += 1
	return current_n

print largeFibonacci(1000)