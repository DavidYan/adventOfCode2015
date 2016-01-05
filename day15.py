# pip install pulp
from pulp import *
import math
import numpy

def readInput():
	valueMatrix = [[],[],[],[], []]

	with open('day15.txt') as ingredients:
		for line in ingredients.readlines():

			strings = line.split(" ")

			valueMatrix[0].append(int(strings[2].rstrip(',')))
			valueMatrix[1].append(int(strings[4].rstrip(',')))
			valueMatrix[2].append(int(strings[6].rstrip(',')))
			valueMatrix[3].append(int(strings[8].rstrip(',')))
			valueMatrix[4].append(int(strings[10].rstrip('\n')))

	return valueMatrix

# Brute force beyotchezzz
def getMaxScore(valueMatrix, maxIngredients):
	highestScore = 0
	span = maxIngredients + 1
	solution = [0, 0, 0, 0]

	count = 0
	for i in range(span):
		solution[0] = i
		for j in range(span - i):
			solution[1] = j
			for k in range(span - (i+j)):
				solution[2] = k
				for l in range(span - (i+j+k)):
					solution[3] = l

					# calorie check conditional for part B
					if numpy.dot(valueMatrix[4], solution) != 500:
						continue

					val1 = numpy.dot(valueMatrix[0], solution)
					val2 = numpy.dot(valueMatrix[1], solution)
					val3 = numpy.dot(valueMatrix[2], solution)
					val4 = numpy.dot(valueMatrix[3], solution)

					# don't bother multiplying if we get neg values
					if val1 > 0 and val2 > 0 and val3 > 0 and val4 > 0:
						total = val1 * val2 * val3 * val4
						if total > highestScore:
							highestScore = total

	return highestScore

# TODO Figure out if this is solvable via linear programming
def solve():
	prob = LpProblem("test1", LpMaximize)

	x = LpVariable("sprinkles", 5, -1, 0, 0)
	y = LpVariable("pb", -1, 3, 0, 0)
	z = LpVariable("frosting", 0, -1, 4, 0)
	v = LpVariable("sugar", -1, 0, 0, 2)

	prob += x*y*z*v

	prob += x+y+z+v <= 100

	GLPK().solve(prob)

	for v in prob.variables():
		print v.name, "=", v.varValue

	print "objective=", value(prob.objective)

def main():
	utilityMatrix = readInput()
	print getMaxScore(utilityMatrix, 100)

if __name__ == '__main__':
	main()