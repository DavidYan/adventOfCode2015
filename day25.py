import math

def triangleSum(number):
	return (number*(number+1))/2

# figured the formula for diagonal traversal
def getActualOrder(row, column):
	return triangleSum(row + column - 2) + column

def machineAlgo(number):
	magicMultiplier = 252533
	magicDivisor = 33554393

	product = number * magicMultiplier
	return product % magicDivisor

def solve(row, column, start):
	order = getActualOrder(row, column)
	currentVal = start
	for i in range(order - 1): #offset from starting value
		currentVal = machineAlgo(currentVal)

	return currentVal

def main():
	start = 20151125 # input from the problem
	problemRow = 3010
	problemCol = 3019
	# To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019.
	print solve(problemRow, problemCol, start)

if __name__ == '__main__':
	main()