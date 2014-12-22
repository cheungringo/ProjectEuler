'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is 
formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?'''

# this is quite an easy problem, can immediately see a pattern:
# sum is just 1 + (1+2) + (1+2+2) + (1+2+2+2) + (1+2+2+2+2) then switch to + 4.
# pattern terminates for 5 by 5 when done adding 4 and 7 by 7 when done adding 6 so (n/2)*2

def get_spiral_sum(n):
	if n % 2 == 0:
		print "That's an even number, won't work"
		return
	else:
		spiral_sum = 1
		current = 1
		add = 2
		end = (n/2)*2+2
		while add != end:
			for x in range(4):
				current += add
				spiral_sum += current
			add += 2
	return spiral_sum

print get_spiral_sum(1001)