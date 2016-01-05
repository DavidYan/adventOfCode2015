import math

class Reindeer:
	def __init__(self, speed, speedTime, rest, name):
		self.distance = 0
		self.speed = speed
		self.speedTime = speedTime
		self.rest = rest
		self.resting = False
		self.timer = speedTime
		self.name = name
		self.points = 0

	def getDistance(self):
		return self.distance

	def getName(self):
		return self.name

	def tickOne(self):
		if self.resting:
			# resting
			self.timer -= 1
			if self.timer == 0:
				self.resting = False
				self.timer = self.speedTime
		else:
			# speeding
			self.distance += self.speed
			self.timer -= 1
			if self.timer == 0:
				self.resting = True
				self.timer = self.rest

	def addPoint(self):
		self.points += 1

	def getPoints(self):
		return self.points


def readInput():
	reindeers = []
	with open('day14.txt') as stats:
		for line in stats.readlines():
			strings = line.split(" ")

			name = strings[0]
			speed = int(strings[3])
			speedTime = int(strings[6])
			rest = int(strings[len(strings) - 2])

			reindeer = Reindeer(speed, speedTime, rest, name)
			reindeers.append(reindeer)

	return reindeers

def awardPoint(reindeers):
	theReindeer = ''
	maxDistance = 0

	for i in range(len(reindeers)):
		distance = reindeers[i].getDistance()
		if maxDistance < distance:
			maxDistance = distance
			theReindeer = reindeers[i]

	theReindeer.addPoint()

def main():
	length = 2503

	reindeers = readInput()

	for time in range(length):
		for reindeer in reindeers:
			reindeer.tickOne()
		awardPoint(reindeers)

	distances = [reindeer.getDistance() for reindeer in reindeers]
	points = [reindeer.getPoints() for reindeer in reindeers]

	print max(points)

if __name__ == '__main__':
	main()