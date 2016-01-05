import math

def readDims():
	with open('day2.txt') as presents:
		data = [[int(dimension) for dimension in i.split('x')] for i in presents.readlines()]

	return data

def getPaperAmt(dimArray):
	h = dimArray[0]
	l = dimArray[1]
	w = dimArray[2]

	# first find the smallest two dimensions
	# naively assume it's ordered
	firstSmallest = h
	secondSmallest = l
	thirdSmallest = w
	
	if (firstSmallest <= secondSmallest and thirdSmallest < secondSmallest):
		secondSmallest = thirdSmallest
	elif (secondSmallest < firstSmallest and thirdSmallest < firstSmallest):
		firstSmallest = thirdSmallest

	# now to calculate the amount of paper
	return (firstSmallest*secondSmallest) + 2*(h*l + l*w + h*w)

def getTotalPaper():
	data = readDims()
	total = 0

	for package in data:
		total += getPaperAmt(package)

	print total	

def getRibbonAmt(dimArray):
	h = dimArray[0]
	l = dimArray[1]
	w = dimArray[2]

	# first find the smallest two dimensions
	# naively assume it's ordered
	firstSmallest = h
	secondSmallest = l
	thirdSmallest = w
	
	if (firstSmallest <= secondSmallest and thirdSmallest < secondSmallest):
		secondSmallest = thirdSmallest
	elif (secondSmallest < firstSmallest and thirdSmallest < firstSmallest):
		firstSmallest = thirdSmallest

	return 2*(firstSmallest+secondSmallest) + (l*w*h)

def getTotalRibbon():
	data = readDims()
	total = 0

	for package in data:
		total += getRibbonAmt(package)

	print total

def main():
	getTotalRibbon()

#print floor

if __name__ == '__main__':
	main()