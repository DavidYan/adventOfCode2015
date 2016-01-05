import math

def readInput():
	with open('day18.txt') as startConfig:
		data = [[i for i in line] for line in startConfig.read().splitlines()]

	return data

def animate(grid, steps):
	newGrid = grid
	for i in range(steps):
		newGrid = processLights(newGrid)

	return newGrid

def processLights(grid):
	# deepcopy without using deepcopy, also is faster
	# BECAUSE PYTHON IS PASS BY REFERENCE WOOOPSSS
	newGrid = [x[:] for x in grid]

	for i in range(len(grid)):
		line = grid[i]
		for j in range(len(line)):
			# part b: early exit for corner cases
			if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(line) - 1):
				newGrid[i][j] = '#'
				continue			

			neighbors = getNeighbors(grid, i, j)

			lightsOn = 0
			for lights in neighbors:
				if lights == '#':
					lightsOn += 1

			light = grid[i][j]
			if light == '.' and lightsOn == 3: # turn on
				newGrid[i][j] = '#'
			elif light == '#' and not (lightsOn == 2 or lightsOn == 3): # turn off
				newGrid[i][j] = '.'
			else:
				newGrid[i][j] = light

	return newGrid

def getNeighbors(grid, i, j):
	neighbors = []
	modifiers = [[x, y] for x in [-1, 0, 1] for y in [-1, 0, 1] if not (x == y == 0)]

	for modifier in modifiers:
		newX = i+modifier[0]
		newY = j+modifier[1]

		if 0 <= newX <= len(grid) - 1 and 0 <= newY <= len(grid[0]) - 1:
			newValue = grid[newX][newY]
			neighbors.append(newValue)

	return neighbors

def printGrid(grid):
	printGrid = ''
	for line in grid:
		for char in line:
			printGrid += char

		printGrid += '\n'

	print printGrid

def main():
	lightGrid = readInput()
	
	# turn on all corner lights for part B
	lightGrid[0][0] = '#'
	lightGrid[len(lightGrid)-1][0] = '#'
	lightGrid[0][len(lightGrid[0])-1] = '#'
	lightGrid[len(lightGrid)-1][len(lightGrid[0])-1] = '#'

	finalGrid = animate(lightGrid, 100)

	count = 0
	for line in finalGrid:
		for light in line:
			if light == '#':
				count += 1

	print count

if __name__ == "__main__":
	main()