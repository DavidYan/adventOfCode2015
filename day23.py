import math

def readInput():
	commandList = []
	with open('day23.txt') as instructions:
		for instruction in instructions.read().splitlines():
			commandList.append(instruction.split(" "))

	return commandList

def interpret(instructions, registers, counter):
	instruction = instructions[counter]
	command = instruction[0]

	# main command switch
	# branch between jumps and non-jumps
	if command[0] == 'j': # jumps
		if command == 'jmp': # jump only takes 2 args
			displacement = instruction[1]
			modifier = displacement[0]
			number = displacement[1:]

			if modifier == '+':
				counter += int(number)
			elif modifier == '-':
				counter -= int(number)
		else: # other jumps take 3 args
			target = instruction[1][0] #strip comma
			displacement = instruction[2]
			modifier = displacement[0]
			number = displacement[1:]
			result = counter
			counter += 1

			if modifier == '+':
				result += int(number)
			elif modifier == '-':
				result -= int(number)

			if command == 'jie' and registers[target] % 2 == 0:
				counter = result
			elif command == 'jio' and registers[target] == 1:
				counter = result
	else: # non-jumps
		target = instruction[1]
		counter += 1
		if command == 'inc':
			registers[target] += 1
		elif command == 'hlf':
			registers[target] = registers[target] / 2
		elif command == 'tpl':
			registers[target] = registers[target] * 3

	# run sanitation checks
	if registers['a'] < 0:
		registers['a'] = 0

	if registers['b'] < 0:
		registers['b'] = 0

	if counter >= len(instructions):
		counter = -1

	return counter


def run(instructions, regs):
	counter = 0 #-1 will be our exit number.
	registers = regs.copy()

	while counter != -1:
		counter = interpret(instructions, registers, counter)

	return registers

def main():
	instructions = readInput()
	registersA = {'a': 0, 'b': 0}
	registersB = {'a': 1, 'b': 0}

	resultsA = run(instructions, registersA)
	resultsB = run(instructions, registersB)
	print resultsA['b']
	print resultsB['b']

if __name__ == "__main__":
	main()