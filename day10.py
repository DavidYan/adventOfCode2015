personalInput = "3113322113"

def lookSay(nums):
	currentNum = ''
	count = 0
	output = ""

	for char in nums:
		if char == currentNum:
			count += 1
		else:
			if (len(currentNum) != 0): #ignore empty char case
				output += (str(count) + currentNum)
			
			count = 1
			currentNum = char

	# need to append last group to the output string
	output += (str(count) + currentNum)
	
	return output

def main():
	currentValue = personalInput
	part1iterations = 40
	part2iterations = 50

	for i in range(part2iterations):
		currentValue = lookSay(currentValue)

	print len(currentValue)

if __name__ == '__main__':
	main()