import math
import itertools

STUPIDLY_LARGE_NUMBER = 999999999999999

def readInput():
	packages = []
	with open('day24.txt') as presents:
		for present in presents.read().splitlines():
			packages.append(int(present))

	return packages

def getMinQE(configs):
	smallestConfig = []
	smallest = STUPIDLY_LARGE_NUMBER
	for config in configs:
		product = 1
		for num in config:
			product *= num

		if product < smallest or smallest < 0:
			smallest = product
			smallestConfig = config

	return smallest

def hasSubsetSum(array, index, targetSum):
	# Base cases
	if targetSum == 0:
		return True

	if index == 0 and targetSum > 0:
		return False

	# Check if last element is greater than sum, then ignore as candidate
	lastEle = array[index-1]
	if lastEle > targetSum:
		return hasSubsetSum(array, index-1, targetSum)
	else: # Check if we can get sum with or without last element
		newSum = targetSum - lastEle
		return hasSubsetSum(array, index-1, targetSum) or hasSubsetSum(array, index-1, newSum)

def twoPartitionable(array, index):
	total = sum(array)
	if total % 2 == 1: #sum is odd, shouldn't happen though
		return False
	
	return hasSubsetSum(array, index, total/2)

def checkSolution(combo, array):
	# create array of elements not in combo
	leftovers = [x for x in array if x not in combo]
	return twoPartitionable(leftovers, len(leftovers))

def technicallySmallestSize(array, target):
	current = target
	count = 0
	for i in range(len(array)):
		#python neg traversal?
		index = len(array) - (i+1)
		current -= array[index]
		count += 1

		if current <= 0:
			return count

# DISGUSTING BRUTE FORCE NP SOLUTION
def getSolutionsA(array, startSize, target):
	# 3-Partition Problem is annoying to solve so...
	# 3-Partition problem = Subset Sum problem + 2 Partition Problem.
	solutions = []
	size = startSize

	# First find a smallest subset that hits target.
	while True:
		combos = itertools.combinations(array, size)

		# check all combinations of smallest size
		for combo in combos:
			# Then check if combo solves the 2-partition problem.
			if sum(combo) == target:
				if checkSolution(combo, array):
					solutions.append(combo)

		if len(solutions) > 0:
			return solutions

		# Else check combos of one size larger
		size += 1

def getSolutionsB(array, startSize, target):
	# 4-Partition Problem = Subset Sum + 3 Partition Problem

	solutions = []
	size = startSize
	# First find a smallest subset that hits target
	while True:
		combos = itertools.combinations(array, size)

		# check all combos of smallest size:
		for combo in combos:
			if sum(combo) == target:
				leftovers = [x for x in array if x not in combo]
				if solveA(leftovers) < STUPIDLY_LARGE_NUMBER:
					solutions.append(combo)

		if len(solutions) > 0:
			return solutions

		size += 1


def solveA(presents):
	target = sum(presents)/3 # if the weights must be balanced well...
	# no two gifts ever weigh the same, this is useful
	#  for array comparisons.
	smallestSize = technicallySmallestSize(presents, target)
	solutions = getSolutionsA(presents, smallestSize, target)

	return getMinQE(solutions)

def solveB(presents):
	target = sum(presents)/4

	smallestSize = technicallySmallestSize(presents, target)
	solutions = getSolutionsB(presents, smallestSize, target)

	return getMinQE(solutions)

def main():
	presents = readInput()

	print solveA(presents)
	print solveB(presents)

if __name__ == '__main__':
	main()