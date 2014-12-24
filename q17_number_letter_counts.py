'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?
'''

# if numbers are written in words, how many letters would be used
num_map = {1: 'one', 2: 'two', 3: 'three', 4:'four' , 5: 'five', 6: 'six', 
7: 'seven', 8: 'eight', 9:'nine', 10:'ten', 11: 'eleven', 12: 'twelve',
13: 'thirteen', 14:'fourteen', 15: 'fifteen', 16:'sixteen', 17:'seventeen',
18: 'eighteen', 19: 'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
60: 'sixty', 70: 'seventy', 80: 'eighty', 90:'ninety', 100:'hundred'}

one_99 = 0
for x in range(1, 100):
 	if x <= 20:
 		one_99 += len(num_map[x])
 	elif (x % 10 != 0):
		ones = x%10
		one_99 += len(num_map[ones])+len(num_map[x-ones])
	else:
		one_99 += len(num_map[x])

one_99 *= 10

# now just need to add the hundreds: ex. one hundred and something
hundreds = 0
for x in range(1, 10):
	hundreds += 100*(len(num_map[x]) + len(num_map[100]) + len('and'))
	hundreds -= len('and') # take out the and for right on hundred

print one_99 + hundreds + len('onethousand')

