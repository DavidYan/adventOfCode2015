import math

def readInput():
	with open('day3.txt') as directions:
		inputStr = ""
		for i in directions.readlines():
			inputStr += i 
		return inputStr

# coordinates is a [x, y] array
def getNewLoc(direction, coordinates):
	if direction == '^':
		coordinates[1] += 1
	elif direction == 'v':
		coordinates[1] -= 1
	elif direction == '>':
		coordinates[0] += 1
	elif direction == '<':
		coordinates[0] -= 1

	return coordinates

def locString(coordinates):
	return str(coordinates[0])+','+str(coordinates[1])

def getNumHouses():
	directions = readInput()

	count = 0
	santaLoc = [0, 0]
	roboLoc = [0, 0]
	movers = [santaLoc, roboLoc]
	
	houses = {locString(santaLoc): 1}

	for direction in directions:
		mover = movers[count % 2]
		mover = getNewLoc(direction, mover)
		houses[locString(mover)] = 1
		count += 1

	return len(houses)

def main():
	print getNumHouses()

if __name__ == '__main__':
	main()