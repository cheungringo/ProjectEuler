'''Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
product of an integer with (1,2, ... , n) where n > 1?
'''

# we get some hints off the bat. we know that the first number has to be a 9 which eliminates a lot 
# of possibilities
# next we can use an integer and keep multiplying by 1 2 3 .. n and check if pandigital
# until the length of the number exceeds 9, then we go to the next one
# since we have to have n >= 2, the max digit size is 4. We do not need to check anything past
# 9999 since 5 digits twice will give 10 digits, exceeding the rules of the problems