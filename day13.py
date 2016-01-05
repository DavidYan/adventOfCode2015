# I LOVE YOU PYTHON LIBRARIES
import math
from itertools import permutations
#itertools.permutations(iterable[, r])

def readInput():
	interactDict = {}
	with open('day13.txt') as interactions:
		for interaction in interactions.readlines():
			strings = interaction.split(" ")
			personA = strings[0]
			personB = strings[len(strings) - 1].rstrip('.\n')

			modifier = strings[2]
			amount = 0
			if modifier == 'lose':
				amount -= int(strings[3])
			elif modifier == 'gain':
				amount += int(strings[3]) 

			# build directional dict.
			if personA not in interactDict.keys():
				interactDict[personA] = {personB: amount}
			elif personB not in interactDict[personA].keys():
				interactDict[personA][personB] = amount


	return interactDict

def getMaxHappy(interactions):
	maximum = 0 # should be safe since longest distance < 1000 for each city
	numPeople = len(interactions.keys())

	# 8! number of paths, brute force time.
	for possibleSeating in permutations(interactions.keys()):
		currentHappiness = 0

		for i in range(len(possibleSeating)):
			currentPerson = possibleSeating[i]

			# circular looping
			neighborA = possibleSeating[(i + 1) % numPeople]
			neighborB = possibleSeating[(i - 1) % numPeople]
			
			currentHappiness += interactions[currentPerson][neighborA]
			currentHappiness += interactions[currentPerson][neighborB]

		if maximum < currentHappiness:
			maximum = currentHappiness

	return maximum

# for part B
def addMe(interactions):
	meDict = {}

	for person in interactions.keys():
		interactions[person]['me'] = 0
		meDict[person] = 0

	interactions['me'] = meDict

	return interactions


def main():
	# interactions = readInput()
	interactions = addMe(readInput())
	print getMaxHappy(interactions)

if __name__ == '__main__':
	main()