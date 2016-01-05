import math

def readInputStrings():
	count = 0
	with open('day5.txt') as strings:
		for i in strings.readlines():
			if testNiceString2(i):
				count += 1
		return count

def TestNiceString1(inputString):
	print 'meow'

def testNiceString2(inputString):
	doubleRepeats = False
	overlap = False
	prevChar = ''

	# Now break input down into sequence of letters
	for i in range(len(inputString)):
		char = inputString[i]

		# check for overlaps
		if i >= 2 and inputString[i] == inputString[i-2]:
			overlap = True

			# Check if we can exit early
			if doubleRepeats:
				return True

		# check for repeats, string comprehensions are cool
		doubleString = prevChar + char
		if len(doubleString) > 1 and doubleString in inputString[i+1:]:
			doubleRepeats = True

			# Check if we can exit early
			if overlap:
				return True

		# update prevChar
		prevChar = char

	return doubleRepeats and overlap

def main():
	print readInputStrings()

if __name__ == '__main__':
	main()