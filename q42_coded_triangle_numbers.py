'''
Stated problem:
The nth term of the sequence of triangle numbers is given by, tn = (n(n+1))/2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly 
two-thousand common English words, how many are triangle words?

Subproblem:
Parse the file and check the value of each word, preferably using ASCII (ord function)
Make a list of triangular numbers and see if the sum is in the list, the list should be up to t^25 to be safe
Solution:
Go through words in file, sum them by using ASCII and check if sum is in triangular numbers list
'''

def ReadFile(filename):
	''' 
	Returns a list of lowercase strings containing the 2000 words in the file
	which were comma separated and surrounded with quotation marks
	'''
	f = open(filename, 'r')
	contents = f.read()
	contents = contents.split(",")
	for i in range(len(contents)):
		contents[i] = contents[i].strip('"').lower()
	return contents

def GetTriangular(n):
	'''
	Returns a list of the first n triangular numbers
	'''
	triangulars = []
	for x in range(1, n+1):
		triangulars.append((x*(x+1))/2)
	return triangulars

def GetValue(word):
	'''
	Returns the integer value of the word as a sum of its letters
	'''
	total = 0
	for x in range(len(word)):
		value = ord(word[x])-96
		total += value
	return total

def CodedTriangularNumbers(filename):
	words = ReadFile(filename)
	triangulars = GetTriangular(30)
	total = 0
	for word in words:
		value = GetValue(word)
		if value in triangulars:
			total += 1
	return total


print CodedTriangularNumbers('q42input.txt')



