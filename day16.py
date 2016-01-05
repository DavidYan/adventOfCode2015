import math

def readInput():
	with open('day16.txt') as aunts:
		for aunt in aunts.readlines():
			strings = aunt.split(' ')
			data = {'children': -1, 'cats': -1, 'samoyeds': -1, 'pomeranians': -1, 'akitas': -1, 'vizslas': -1, 'goldfish': -1, 'trees': -1, 'cars': -1, 'perfumes': -1}
			
			auntNum = strings[1].rstrip(':')
			stat1 = strings[2].rstrip(':')
			stat1val = strings[3].rstrip(',')
			stat2 = strings[4].rstrip(':')
			stat2val = strings[5].rstrip(',')
			stat3 = strings[6].rstrip(':')
			stat3val = strings[7].rstrip('\n')

			data[stat1] = int(stat1val)
			data[stat2] = int(stat2val)
			data[stat3] = int(stat3val)

			if testPartB(data):
				print auntNum
				return

def testPartA(data):
	if data['children'] >= 0 and data['children'] != 3:
		return False
	elif data['cats'] >= 0 and data['cats'] != 7:
		return False
	elif data['samoyeds'] >= 0 and data['samoyeds'] != 2:
		return False
	elif data['pomeranians'] >= 0 and data['pomeranians'] != 3:
		return False
	elif data['akitas'] >= 0 or data['vizslas'] > 0:
		return False
	elif data['goldfish'] >= 0 and data['goldfish'] != 5:
		return False
	elif data['trees'] >= 0 and data['trees'] != 3:
		return False
	elif data['cars'] >= 0 and data['cars'] != 2:
		return False
	elif data['perfumes'] >= 0 and data['perfumes'] != 1:
		return False

	return True

def testPartB(data):
	if data['children'] >= 0 and data['children'] != 3:
		return False
	elif data['cats'] >= 0 and data['cats'] <= 7:
		return False
	elif data['samoyeds'] >= 0 and data['samoyeds'] != 2:
		return False
	elif data['pomeranians'] >= 0 and data['pomeranians'] >= 3:
		return False
	elif data['akitas'] >= 0 or data['vizslas'] > 0:
		return False
	elif data['goldfish'] >= 0 and data['goldfish'] >= 5:
		return False
	elif data['trees'] >= 0 and data['trees'] <= 3:
		return False
	elif data['cars'] >= 0 and data['cars'] != 2:
		return False
	elif data['perfumes'] >= 0 and data['perfumes'] != 1:
		return False

	return True

def main():
	readInput()

if __name__ == '__main__':
	main()