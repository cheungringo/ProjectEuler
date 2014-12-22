# starting from the top of a triangle, find the maximum total from 
# to to the bottom
# just go from second last row and add the greater of the two adjacent
# numbers in the row below it, then do the same
# once you reach the beginning, will have the max

inp = file('q18input.txt', 'r')
array = []
for line in inp:
	row = line.rstrip().split(' ')
	for x in range(len(row)):
		row[x] = int(row[x])
	array.append(row)

i = len(array)-1
for x in range(len(array)-2, -1, -1):
	for y in range(i):
		print array[x][y], array[x+1][y+1]
		if array[x+1][y] > array[x+1][y+1]:
			array[x][y] += array[x+1][y]
		else:
			array[x][y] += array[x+1][y+1]
	i -= 1

print array

