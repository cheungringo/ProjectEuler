'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
score of 938 x 53 = 49714

What is the total of all the name scores in the file?
'''

file_object = open("p022_names.txt", "r")
names = []
for line in file_object:
	temp = line.split(',')
	for name in temp:
		names.append(name.strip('"'))
names.sort() # sort the names
# create the map for letter values
import string
values = {}
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

total = 0
rank = 1
for name in names:
	name_score = 0
	for char in name:
		name_score += values[char]
	name_score *= rank
	total += name_score
	rank += 1

print total

