import math

targetNumber = 33100000

def partA(target):
	number = 1
	while True:
		value = target
		for i in range(1, int(number**0.5)+1):
			if number % i == 0:
				otherDivisor = number / i
				value -= i*10
				value -= otherDivisor*10

			if value <= 0:
				return number

		number += 1

def partB(target):
	# since we only have to march the elves 50 times, this method is now faster
	upperBound = 1986000 # generated upper bound from a bad solution, 'too high'
	val = [0 for i in range(upperBound)] 

	count = 0

	# offsets are a bitch
	for i in range(1, upperBound+1):
		for j in range(1,51):
			position = i*j - 1
			if position < upperBound:
				val[position] += i * 11

	for k in range(upperBound):
		if val[k] >= target:
			return k + 1 #undo offset

def main():
	#print partA(targetNumber)
	print partB(targetNumber)

if __name__ == '__main__':
	main()