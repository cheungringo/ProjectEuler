file_object = open("q11input.txt", 'r')
grid = []
for line in file_object:
	row = line.rstrip().split(' ')
	for x in range(len(row)):
		row[x] = int(row[x])
	grid.append(row)

product = 0
count = 0
#check horizontally adjacent
for row in range(len(grid)):
	for col in range(len(grid)-3):
		temp = grid[row][col]*grid[row][col+1]*grid[row][col+2]*grid[row][col+3]
		if temp > product:
			product = temp

#check vertically adjacent
for row in range(len(grid)-3):
	for col in range(len(grid)):
		temp = grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col]
		if temp > product:
			product = temp

#check diagonal, down/right
for row in range(len(grid)-3):
	for col in range(len(grid)-3):
		temp = grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3]
		if temp > product:
			product = temp
# check diagonal, up/right
for row in range(3, len(grid)):
	for col in range(len(grid)-3):
		temp = grid[row][col]*grid[row-1][col+1]*grid[row-2][col+2]*grid[row-3][col+3]
		if temp > product:
			product = temp

print product

