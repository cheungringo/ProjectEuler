'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII 
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, 
and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a 
given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key 
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of 
random bytes. The user would keep the encrypted message and the encryption key in different locations, 
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the 
message. The balance for this method is using a sufficiently long password key for security, but short enough 
to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using cipher.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the 
plain text must contain common English words, decrypt the message and find the sum of 
the ASCII values in the original text.

need to use frequency analysis at intervals of 3
most frequent should be space (32), followed by letter e (101)
'''

def readFile(filename):
	f = open(filename, 'r')
	characters = f.read().split(',')
	for x in range(len(characters)):
		characters[x] = int(characters[x])
	return characters

def separateIntoPiles(keyLength, characters):
	piles = []
	start = 0
	for x in range(keyLength):
		pile = []
		for i in range(start, len(characters), keyLength):
			pile.append(characters[i])
		piles.append(pile)
		start += 1
	return piles

def findRange(array):
	minimum = 100
	maximum = 0
	for x in range(len(array)):
		if array[x] < minimum:
			minimum = array[x]
		if array[x] > maximum:
			maximum = array[x]
	return (minimum, maximum)

def findFrequencies(array):
	arrayRange = findRange(array)
	frequency = [0 for x in range(arrayRange[0], arrayRange[1]+1)]
	for x in range(len(array)):
		frequency[array[x]] += 1
	return frequency

def getMaxPos(array):
	pos = 0
	maximum = 0
	for x in range(len(array)):
		if array[x] > maximum:
			maximum = array[x]
			pos = x
	return pos

def getKey(maximum, character):
	# maximum XOR key should equal the character
	for x in range(127):
		if maximum ^ x == character:
			return x

def crackCipher(filename):
	piles = separateIntoPiles(3, readFile(filename))
	total = 0
	for x in range(len(piles)):
		key = getKey(getMaxPos(findFrequencies(piles[x])), 32)
		decrypted = decrypt(key, piles[x])
		for i in range(len(decrypted)):
			total += decrypted[i]
	return total

def decrypt(key, encrypted):
	decrypted = []
	for x in range(len(encrypted)):
		decrypted.append(encrypted[x] ^ key)
	return decrypted


print crackCipher('q59input.txt')



