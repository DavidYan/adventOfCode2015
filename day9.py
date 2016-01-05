# I LOVE YOU PYTHON LIBRARIES
import math
from itertools import permutations
#itertools.permutations(iterable[, r])

def readInput():
	travelDict = {}
	with open('day9.txt') as locations:
		for location in locations.readlines():
			strings = location.split(" ")
			start = strings[0]
			end = strings[2]
			distance = int(strings[4].rstrip('\n'))

			# build bidirectional dict.
			if start not in travelDict.keys():
				travelDict[start] = {end: distance}
			elif end not in travelDict[start].keys():
				travelDict[start][end] = distance

			if end not in travelDict.keys():
				travelDict[end] = {start: distance}
			elif start not in travelDict[end].keys():
				travelDict[end][start] = distance

	return travelDict

def getShortestPath(travelDict):
	shortestDistance = 999999 # should be safe since longest distance < 1000 for each city

	# 8! number of paths, brute force time.
	for possiblePath in permutations(travelDict.keys()):
		prevCity = ''
		pathLength = 0
		for city in possiblePath:
			if prevCity != '':
				pathLength += travelDict[prevCity][city]

			prevCity = city

		if pathLength < shortestDistance:
			shortestDistance = pathLength

	return shortestDistance

def getLongestPath(travelDict):
	longestDistance = 0 

	# 8! number of paths, brute force time.
	for possiblePath in permutations(travelDict.keys()):
		prevCity = ''
		pathLength = 0
		for city in possiblePath:
			if prevCity != '':
				pathLength += travelDict[prevCity][city]

			prevCity = city

		if pathLength > longestDistance:
			longestDistance = pathLength

	return longestDistance


def main():
	travelDict = readInput()
	# print getShortestPath(travelDict)
	print getLongestPath(travelDict)

if __name__ == '__main__':
	main()