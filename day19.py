import math
import string
import pprint

inputMolecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

def readInput():
	replacements = {}
	with open('day19.txt') as startConfig:
		for line in startConfig.read().splitlines():
			strings = line.split(" ")
			key = strings[0]
			replacement = strings[2]

			if key not in replacements.keys():
				replacements[key] = [replacement]
			else:
				replacements[key].append(replacement)

	return replacements

def readInputReverse():
	replacements = {}
	with open('day19.txt') as startConfig:
		for line in startConfig.read().splitlines():
			strings = line.split(" ")
			key = strings[2]
			replacement = strings[0]

			if key not in replacements.keys():
				replacements[key] = replacement

	return replacements

# for Part A
def scanMolecule(molecule, replacements):
	# identify atoms
	combos = []

	if len(molecule) == 1 and molecule in replacements.keys():
		return replacements[molecule]

	for i in range(len(molecule)):
		token = ''
		char = molecule[i]
		if char.islower(): # atoms are at most 2 chars long.
			token = molecule[i-1] + char
			addCombos(molecule, i-1, token, replacements, combos)
		else: #char is upper.
			if i == len(molecule) - 1:
				token = char
			elif molecule[i+1].isupper():
				token = char

			addCombos(molecule, i, token, replacements, combos)

	# typecasting forces uniqueness
	return list(set(combos))

def addCombos(molecule, index, token, grammar, comboList):
	if len(token) == 0 or token not in grammar.keys():
		return

	for possible in grammar[token]:
		#print "replacing " + token + " at index " + str(index) + " with " + possible
		newMolecule = molecule[:index] + string.replace(molecule[index:], token, possible, 1)
		comboList.append(newMolecule)

# Part B
def getSteps(molecule, replacements, lookup):
	target = molecule
	steps = 0

	# greedy algorithm leads to the solution, though that is by luck.
	while target != 'e':
		for compound in replacements:
			if compound in target:
				target = str.replace(target, compound, lookup[compound], 1)
				break
		steps += 1

	return steps


def main():
	# Part A
	grammar = readInput()
	print len(scanMolecule(inputMolecule, grammar))

	# Part B
	grammar = readInputReverse()
	reverseSortKey = grammar.keys()
	reverseSortKey.sort(lambda x,y: cmp(len(y),len(x)))

	print getSteps(inputMolecule, reverseSortKey, grammar)


if __name__ == '__main__':
	main()