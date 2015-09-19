'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
My strategy: Basically just check for each of the possible hands from highest to lowest. If both 
have the same hand resolve the tie, if either of them have the hand and the other doesn't we have a winner.
'''

class hand:
	def __init__(self, cards):
		self.ranks = []
		self.suits = []
		self.singles = []
		for x in range(5):
			if cards[x][0] == "T":
				self.ranks.append(10)
			elif cards[x][0] == 'J':
				self.ranks.append(11)
			elif cards[x][0] == 'Q':
				self.ranks.append(12)
			elif cards[x][0] == 'K':
				self.ranks.append(13)
			elif cards[x][0] == 'A':
				self.ranks.append(1)
			else:
				self.ranks.append(int(cards[x][0]))
			self.suits.append(cards[x][1])
		self.ranks.sort()
		self.getSingles()
	def getSingles(self):
		singles = []
		for x in range(5):
			if self.ranks.count(self.ranks[x]) == 1:
				if self.ranks[x] == 1:
					singles.append(14)	
				else:
					singles.append(self.ranks[x])
		singles.sort()
		singles.reverse()
		self.singles = singles
	def checkFlush(self):
		for x in range(4):
			if self.suits[x] != self.suits[x+1]:
				return 0
		return 1
	def checkStraight(self):
		if self.ranks[0] == 1:
			if self.ranks[1] == 10:
				for x in range(1, 4):
					if ((self.ranks[x] + 1) != self.ranks[x+1]):
						return 0
				return 14
		for x in range(4):
			if self.ranks[x] + 1 != self.ranks[x+1]:
				return 0
		return self.ranks[4]
	def checkTriple(self):
		if self.ranks.count(self.ranks[0]) == 3:
			return self.ranks[0]
		elif self.ranks.count(self.ranks[1]) == 3:
			return self.ranks[1]
		elif self.ranks.count(self.ranks[2]) == 3:
			return self.ranks[2]
		return 0
	def checkDouble(self, start):
		if (self.ranks[start] == self.ranks[start+1]):
			return self.ranks[start]
		return 0
	def checkRoyalFlush(self):
		for x in range(10, 14):
			if x not in self.ranks:
				return 0
		if 1 in self.ranks:
			return self.checkFlush()
	def checkStraightFlush(self):
		if self.checkStraight():
			if self.checkFlush():
				return self.ranks[4]
		return 0
	def checkFoaK(self):		
		'''returns the card for which there is four of a kind or 0'''
		if self.ranks.count(self.ranks[0]) == 4:
			return self.ranks[0]
		elif self.ranks.count(self.ranks[1]) == 4:
			return self.ranks[1]
		return 0
	def checkFH(self):
		'''returns the card for which there is three of a kind or 0'''
		triple = self.checkTriple()
		if triple == 0:
			return 0
		if self.ranks.index(triple) == 0:
			double = self.checkDouble(3)
			if double > 0:
				return triple
		if self.ranks.index(triple) == 2:
			double = self.checkDouble(0)
			if double > 0:
				return triple
		return 0
	def checkPairs(self):
		pairs = []
		for x in range(4):
			if (self.checkDouble(x) > 0):
				if (self.ranks[x] == 1):
					pairs.append(14)
				else:
					pairs.append(self.ranks[x])
		if len(pairs) == 0:
			return []
		pairs.sort()
		pairs.reverse()
		return pairs
		
def readFile(filename):
	f = open(filename, 'r')
	p1wins = 0
	total = 0
	i = 0
	for line in f:
		winner = checkWinner(line)
		if winner == 1:
			total += 1
		i += 1
	return total
		
def checkWinner(line):
	hands = line.split(' ')
	hand1 = hand(hands[0:5])
	hand2 = hand(hands[5:10])
	RF = checkRF(hand1, hand2)
	if RF > 0:
		return RF
	SF = checkSF(hand1, hand2)
	if SF > 0:
		return SF
	FoaK = checkFoaK(hand1, hand2)
	if FoaK > 0:
		return FoaK
	FH = checkFH(hand1, hand2)
	if FH > 0:
		return FH
	Flush = checkFlush(hand1, hand2)
	if Flush > 0:
		return Flush
	Straight = checkStraight(hand1, hand2)
	if Straight > 0:
		return Straight
	Triple = checkTriple(hand1, hand2)
	if Triple > 0:
		return Triple
	final = checkPairsAndBelow(hand1, hand2)
	if final > 0:
		return final

# the convention here is to return 1 if player 1 wins, 2 if player 2 wins and 0 in case of tie
def checkRF(hand1, hand2):
	if hand1.checkRoyalFlush() > 0:
		return 1
	if hand2.checkRoyalFlush() > 0:
		return 2
	return 0

def checkSF(hand1, hand2):
	one = hand1.checkStraightFlush()
	two = hand2.checkStraightFlush()
	return decideReturn(one, two)

def checkFoaK(hand1, hand2):
	one = hand1.checkFoaK()
	two = hand2.checkFoaK()
	return decideReturn(one, two)

def checkFH(hand1, hand2):
	one = hand1.checkFH()
	two = hand2.checkFH()
	return decideReturn(one, two)

def checkFlush(hand1, hand2):
	one = hand1.checkFlush()
	two = hand2.checkFlush()
	if one > two:
		return 1
	if two > one:
		return 2
	if one > 0 and two > 0:
		return decideSingles(hand1, hand2)
	return 0

def checkStraight(hand1, hand2):
	one = hand1.checkStraight()
	two = hand2.checkStraight()
	return decideReturn(one, two)

def checkTriple(hand1, hand2):
	one = hand1.checkTriple()
	two = hand2.checkTriple()
	if one == 1:
		return 1
	if two == 1:
		return 2
	return decideReturn(one, two)

def checkPairsAndBelow(hand1, hand2):
	one = hand1.checkPairs()
	two = hand2.checkPairs()

	if len(one) > len(two):
		return 1
	elif len(two) > len(one):
		return 2
	else:
		for x in range(len(one)):
			if (one[x] > two[x]):
				return 1
			elif (two[x] > one[x]):
				return 2
		return decideSingles(hand1, hand2)

def decideSingles(hand1, hand2):
	for x in range(len(hand1.singles)):
		if hand1.singles[x] > hand2.singles[x]:
			return 1
		if hand2.singles[x] > hand1.singles[x]:
			return 2

def decideReturn(one, two):
	if one > two:
		return 1
	elif two > one:
		return 2
	return 0

print readFile('q54input.txt')


