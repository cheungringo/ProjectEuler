'''In England the currency is made up of pound, E, and pence, p, and there are eight coins in 
general circulation:

1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can E2 be made using any number of coins?'''

# this can be solved recursively by lowering the denomination each time

def makeChange(remainder, coin):
	currentcoin = coin # we need to figure out how many times 
	#current coin fits into current total
	# lower the denomination by 1 each time
	if coin == 200:
		coin = 100
	elif coin == 100:
		coin = 50
	elif coin == 50:
		coin = 20
	elif coin == 20:
		coin = 10
	elif coin == 10:
		coin = 5
	elif coin == 5:
		coin = 2
	elif coin == 2:
		coin = 1
	elif coin == 1:
		return 1
	else:
		coin = 200
	num_ways = 0
	num_coins = remainder / currentcoin 
	for x in range(num_coins+1):
		# call makeChange with the new remainder and the next denomination
		num_ways += makeChange(remainder - x*currentcoin, coin)
	return num_ways

print makeChange(200, 200)