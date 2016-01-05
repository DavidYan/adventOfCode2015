import math

def readInput():
	count = 0
	memCount = 0
	with open('day8.txt') as inputs:
		for line in inputs.readlines():
			if line:
				# discount the newline char
				count += (len(line) - 1)

				cleanedLine = line[:-1]
				memCount += encodeCount(cleanedLine)


	return abs(count - memCount)

# function used for part 1
def decodeCount(inputLine):
	strippedLine = inputLine[1:-1]
	count = 0
	escapeFlag = False
	for i in range(len(strippedLine)):
		char = strippedLine[i]
		offset = 1

		# Check if \ sign is an escape flag or not.
		if char == '\\' and not escapeFlag:
			escapeFlag = True
			offset = 0
		elif escapeFlag:
			if char == 'x':
				offset = -1

			escapeFlag = False

		count += offset

	#print 'This is sequence: ' + strippedLine
	#print 'Norm Count: ' + str(len(strippedLine))
	#print 'Mem Count: ' + str(count)

	return count

def encodeCount(inputLine):
	count = 2 # Include leading and trailing quotation marks

	for i in range(len(inputLine)):
		char = inputLine[i]
		offset = 1

		if char == '\\' or char == '\"':
			offset = 2

		count += offset

	print 'This is sequence: ' + inputLine
	print 'Norm Count: ' + str(len(inputLine))
	print 'Mem Count: ' + str(count)

	return count

def main():
	print readInput()

if __name__ == '__main__':
	main()