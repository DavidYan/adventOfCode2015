import math
from itertools import combinations
#itertools.combinations(iterable, arrayLength)

def readInput():
	cups = []
	with open('day17.txt') as containers:
		for cup in containers.read().splitlines():
			cups.append(int(cup))

	return cups

def numRecA(cups, target):
	combos = 0
	# Base case, test all of the leftover combos
	if len(cups) == 2:
		combos = 0
		if cups[0] == target:
			combos += 1
		elif cups[1] == target:
			combos += 1
		elif cups[0] + cups[1] == target:
			combos += 1

		return combos


	# recursive case
	# number of solutions total is number having this cup as part of solution and number of solutions not having this cup
	for i in range(len(cups)):
		potentialCup = cups[i]
		newCups = cups[:i] + cups[i+1:]
		combos += numRecA(newCups, target) + numRecA(newCups, target - potentialCup)

	return combos


def numCombosA(cups, target):
	# brute force baby
	numCups = len(cups)
	validComboCount = 0

	# hack because our input has no numbers greater than 50.
	# So we know each possible solution has 4 or more cups in it.
	for i in range(4, numCups+1):
		for combo in combinations(cups, i):
			if sum(combo) == target:
				validComboCount += 1

	return validComboCount

def numCombosB(cups, target):
	# brute force baby
	numCups = len(cups)
	validComboCount = 0
	minCups = 0
	# hack because our input has no numbers greater than 50.
	# So we know each possible solution has 4 or more cups in it.
	# Break as soon as we determine the minimum number of cups and combos
	for i in range(4, numCups+1):
		for combo in combinations(cups, i):
			if minCups > 0 and i > minCups:
				break
			elif sum(combo) == target:
				validComboCount += 1

				if minCups == 0:
					minCups = i

	return validComboCount

def main():
	cups = readInput()
	target = 150

	print numRecA(cups, target)
	print numCombosA(cups, target)
	#print numCombosB(cups, target)

if __name__ == '__main__':
	main()