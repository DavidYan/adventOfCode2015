import math
import pprint

def readInput():
	# create a dictionary with wirenames and their associated values
	wireTrace = {}
	with open('day7.txt') as instructions:
		for instruction in instructions.readlines():
			# clean terms of trailing and leading newlines or spaces
			cleanedExps = [i.rstrip().lstrip() for i in instruction.rstrip('\n').split("->")]
			wireTrace[cleanedExps[1]] = cleanedExps[0]

	# COMMENT THIS OUT TO RUN PART ONE OF THIS DAY
	wireTrace['b'] = 46065

	return evaluate(wireTrace, 'a')

# The crux of this problem is to recognize that there is only one expression which evaluates to a wire.
# So in the instructions manual, given wire A there is only one such input expression X such that X -> A
# Evalute returns either a number or an expression to be evaluted
def evaluate(inputs, wireToTrace): 
	# check if our input is already a number or a stringified number
	if isinstance(wireToTrace, (int, long)):
		return wireToTrace
	elif wireToTrace.isdigit():
		return int(wireToTrace)

	# if we get a direct number from our dictionary, then we're good.
	currentExp = inputs[wireToTrace]

	if isinstance(currentExp, (int, long)):
		return currentExp
	elif currentExp.isdigit():
		inputs[wireToTrace] = int(currentExp)
		return int(currentExp)

	# Else we need to evaluate
	# Luckily, all operators are on the left side expression, which is great.
	exps = currentExp.split(" ")
	output = 0

	# Search for instructions
	if 'NOT' in exps:
		word = exps[1]
		output = ~ evaluate(inputs, word)
	elif 'AND' in exps:
		word1 = exps[0]
		word2 = exps[2]
		output = evaluate(inputs, word1) & evaluate(inputs, word2)
	elif 'OR' in exps:
		word1 = exps[0]
		word2 = exps[2]
		output = evaluate(inputs, word1) | evaluate(inputs, word2)
	elif 'LSHIFT' in exps: # shifts 2nd arg is number
		word1 = exps[0]
		word2 = exps[2]
		output = evaluate(inputs, word1) << evaluate(inputs, word2)
	elif 'RSHIFT' in exps: # shifts 2nd arg is number
		word1 = exps[0]
		word2 = exps[2]
		output = evaluate(inputs, word1) >> evaluate(inputs, word2)
	else: # only option left is variable reassignment
		output = evaluate(inputs, exps[0])


	# Don't forget to clean the output at each step with 16-bit mask
	cleanOutput = output & 65535
	inputs[wireToTrace] = cleanOutput

	return cleanOutput

def main():

	print readInput()

if __name__ == '__main__':
	main()