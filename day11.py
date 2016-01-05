import math

# hard coded because why not.
incrementLetter = {'a':'b', 'b':'c', 'c':'d', 'd':'e','e':'f', 'f':'g', 'g':'h', 'h':'i', 'i': 'j', 'j':'k', 'k':'l', 'l': 'm', 'm':'n', 'n': 'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'aa'}
tripletSequence = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']

def increaseLetter(word):
	if len(word) == 1:
		return incrementLetter[word]

	# so the word has more than one letter
	lastLetter = word[len(word) - 1]

	# recursion to do carry ops.
	if lastLetter == 'z':
		return increaseLetter(word[:-1]) + 'a'
	else:
		return word[:-1] + incrementLetter[lastLetter]

def getNextPwd(password):
	currentPwd = increaseLetter(password)
	while True:
		if validPwd(currentPwd):
			return currentPwd
		else:
			currentPwd = increaseLetter(currentPwd)

def validPwd(password):
	# check if bad letters are in there
	if 'i' in password or 'o' in password or 'l' in password:
		return False

	# now stream the letters in password
	firstChar = ''
	secondChar = ''
	thirdChar = ''

	triplets = 0
	doubles = 0

	# greedy exits when possible
	for char in password:
		thirdChar = secondChar
		secondChar = firstChar
		firstChar = char

		# this counts non-overlapping doubles
		if firstChar == secondChar and firstChar != thirdChar: 
			doubles += 1

			if doubles > 1 and triplets > 1:
				return True

		if thirdChar + secondChar + firstChar in tripletSequence:
			if doubles > 1:
				return True
			else:
				triplets += 1

	return triplets > 0 and doubles > 1

def main():
	startPwd = 'vzbxkghb'
	secondPwd = 'vzbxxyzz'

	# insert startPwd for part A, secondPwd for part B
	print getNextPwd(secondPwd)

if __name__ == '__main__':
	main()