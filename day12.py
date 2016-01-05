#open("mytextfile.in").read().splitlines()
import json

def readInput():
	with open('day12.txt') as package:
		return package.read()

# Since addition is commutative, we don't care what order we add things
# Can abuse this for recursion
def evalJson(jsonDict):
	sumSoFar = 0

	# Remove == 'red' check to get part A
	# keys can't be lists or dicts
	for key in jsonDict.keys():
		if key == 'red':
			return 0
		elif isinstance(key, (int)):
			sumSoFar += key

	for value in jsonDict.values():
		if value == 'red':
			return 0 
		elif isinstance(value, int):
			sumSoFar += value
		elif isinstance(value, list):
			sumSoFar += evalList(value)
		elif isinstance(value, dict):
			sumSoFar += evalJson(value)

	#print "current json: " + str(sumSoFar)
	return sumSoFar

def evalList(jsonList):
	sumSoFar = 0

	for item in jsonList:
		if isinstance(item, int):
			sumSoFar += item
		elif isinstance(item, list):
			sumSoFar += evalList(item)
		elif isinstance(item, dict):
			sumSoFar += evalJson(item)

	#print "current list: " + str(sumSoFar)
	return sumSoFar

def main():
	jsonDict = json.loads(readInput())
	print evalJson(jsonDict)

if __name__ == '__main__':
	main()