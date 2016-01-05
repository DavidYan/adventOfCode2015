import math

def loadInventory(weapons, armor, rings):
	getInfo('day21weaps.txt', weapons)
	getInfo('day21armor.txt', armor)
	getInfo('day21rings.txt', rings)

def getInfo(filename, category):
	with open(filename) as items:
		for item in items.read().splitlines():
			info = item.split()
			stats = {}
			stats["name"] = info[0]
			stats["cost"] = int(info[1])
			stats["damage"] = int(info[2])
			stats["armor"] = int(info[3])

			category.append(stats)

def fight(player, boss, equips, debug):
	currentPlayer = player.copy()
	cost = 0
	for item in equips:
		cost += equip(currentPlayer, item)

	playerHp = currentPlayer["hp"]
	bossHp = boss["hp"]
	count = 0

	while True:
		if count % 2 == 0: #player's turn
			bossHp -= (currentPlayer["atk"] - boss["def"])

			if bossHp <= 0:
				return cost
		else: #boss's turn
			playerHp -= (boss["atk"] - currentPlayer["def"])

			if playerHp <= 0:
				return -1*cost

		count += 1

def equip(player, item):
	player["atk"] += item["damage"]
	player["def"] += item["armor"]
	return item["cost"]

def solveA(player, boss, weapons, armors, rings):
	minCost = 100000 #arbitrary high number
	for i in range(len(weapons)):
		weapon = weapons[i]

		for j in range(len(armors)):
			armor = armors[j]

			for k in range(len(rings)):
				ring1 = rings[k]
				remaining = rings[:k] + rings[k+1:]

				for l in range(len(rings) - 1):
					ring2 = remaining[l]

					result = fight(player, boss, [weapon, armor, ring1, ring2], False)
					if result > 0 and result < minCost:
						minCost = result

	return minCost

def solveB(player, boss, weapons, armors, rings):
	maxCost = 0
	for i in range(len(weapons)):
		weapon = weapons[i]

		for j in range(len(armors)):
			armor = armors[j]

			for k in range(len(rings)):
				ring1 = rings[k]
				remaining = rings[:k] + rings[k+1:]

				for l in range(len(rings) - 1):
					ring2 = remaining[l]

					result = fight(player, boss, [weapon, armor, ring1, ring2], False)
					if result < 0 and -result > maxCost:
						maxCost = -result

	return maxCost

def main():
	weapons = []
	armor = []
	rings = []

	# add the empty options in case you choose to buy none.
	loadInventory(weapons, armor, rings)
	nothingItem = {"name": "none", "cost": 0, "damage": 0, "armor": 0}
	armor.append(nothingItem)
	rings.append(nothingItem)
	rings.append(nothingItem)

	boss = {"hp": 104, "atk": 8, "def": 1}
	player = {"hp": 100, "atk": 0, "def": 0}

	print solveA(player, boss, weapons, armor, rings)
	print solveB(player, boss, weapons, armor, rings)

if __name__ == '__main__':
	main()