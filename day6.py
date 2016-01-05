import math

def readInput(grid):
	with open('day6.txt') as instructions:
		for instruction in instructions.readlines():
			parseInstruction2(instruction.rstrip('\n').split(" "), grid)

		# Then get number of lights on
		return numberOfLights2(grid)

### PART ONE OF DAY 6 ###
def parseInstruction1(words, grid):
	# Check what action to take, since this changes where coords are located
	if words[0] == 'toggle':
		coords1 = [int(i) for i in words[1].split(',')]
		coords2 = [int(i) for i in words[3].split(',')]
		toggle1(coords1, coords2, grid)
	elif words[1] == 'on':
		coords1 = [int(i) for i in words[2].split(',')]
		coords2 = [int(i) for i in words[4].split(',')]
		turnOn1(coords1, coords2, grid)
	elif words[1] == 'off':
		coords1 = [int(i) for i in words[2].split(',')]
		coords2 = [int(i) for i in words[4].split(',')]
		turnOff1(coords1, coords2, grid)

def numberOfLights1(grid):
	count = 0
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			if grid[i][j]:
				count += 1

	return count

def turnOn1(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			grid[i][j] = True

def turnOff1(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			grid[i][j] = False

def toggle1(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			grid[i][j] = not grid[i][j]

### PART TWO OF DAY 6 ###
def parseInstruction2(words, grid):
	# Check what action to take, since this changes where coords are located
	if words[0] == 'toggle':
		coords1 = [int(i) for i in words[1].split(',')]
		coords2 = [int(i) for i in words[3].split(',')]
		toggle2(coords1, coords2, grid)
	elif words[1] == 'on':
		coords1 = [int(i) for i in words[2].split(',')]
		coords2 = [int(i) for i in words[4].split(',')]
		turnOn2(coords1, coords2, grid)
	elif words[1] == 'off':
		coords1 = [int(i) for i in words[2].split(',')]
		coords2 = [int(i) for i in words[4].split(',')]
		turnOff2(coords1, coords2, grid)

def numberOfLights2(grid):
	count = 0
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			count += grid[i][j]

	return count

def turnOn2(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			grid[i][j] += 1 

def turnOff2(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			if (grid[i][j] > 0):
				grid[i][j] -= 1

def toggle2(coords1, coords2, grid):
	for i in range(coords1[0], coords2[0] + 1):
		for j in range(coords1[1], coords2[1] + 1):
			grid[i][j] += 2


def main():
	# create grid, fuck yeah list comprehensions!
	grid1 = [[False for i in range(1000)] for j in range(1000)]
	grid2 = [[0 for i in range(1000)] for j in range(1000)]

	print readInput(grid2)

if __name__ == '__main__':
	main()