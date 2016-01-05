import random

spellList = {
	"magic missile": {"cost": 53, "turns": 0},
	"drain": {"cost": 73, "turns": 0},
	"shield": {"cost": 113, "turns": 6},
	"poison": {"cost": 173, "turns": 6},
	"recharge": {"cost": 229, "turns": 5}
}

def fight(player, boss, mode, monteCarlo):
	currentPlayer = player.copy()
	currentBoss = boss.copy()
	manaSpent = 0
	activeSpells = []
	count = 0 

	# game loop
	while True:
		# apply effects at start of turn.
		applySpells(currentPlayer, currentBoss, activeSpells)

		if count % 2 == 0: # player turn
			if mode == "hard":
				currentPlayer["hp"] -= 1
				if currentPlayer["hp"] <= 0:
					return -1

			spells = getValidSpells(currentPlayer, activeSpells)
			if len(spells) == 0: # you got no magic, you ded. loss
				return -1

			if monteCarlo == True:
				spellToCast = random.choice(spells)
			else: # modify logic here to solve deterministically
				spellToCast = spells[0]

			manaSpent += castSpell(currentPlayer, currentBoss, activeSpells, spellToCast)
			if currentBoss["hp"] <= 0 : # win
				return manaSpent
		else: # boss turn
			if currentBoss["hp"] <= 0: # win
				return manaSpent

			damage = currentBoss["atk"] - currentPlayer["def"]
			if damage <= 0:
				damage = 1

			currentPlayer["hp"] -= damage
			if currentPlayer["hp"] <= 0: # loss
				return -1

		count += 1

def getValidSpells(player, activeSpells):
	# you can't stack effects, so active effects limit spell choices
	activeEffects = []
	if len(activeSpells) > 0:
		for spell in activeSpells:
			spellName = spell[0]
			activeEffects.append(spellName)

	mp = player["mp"]
	spells = []
	for spell in spellList.keys():
		if spellList[spell]["cost"] <= mp and spell not in activeEffects:
			spells.append(spell)

	return spells

def applySpells(player, boss, activeSpells):
	if len(activeSpells) > 0:
		refreshActives = []
		for i in range(len(activeSpells)):
			spell = activeSpells[i]
			spellName = spell[0]
			spell[1] -= 1

 			turns = spell[1]
			if spellName == "shield":
				if turns == 5:
					player["def"] += 7
				elif turns == 0:
					player["def"] -= 7
			elif spellName == "poison":
				boss["hp"] -= 3
			elif spellName == "recharge":
				player["mp"] += 101

			if turns != 0:
				refreshActives.append(spell)

		# Python hack to update spells due to pass by assignment
		del activeSpells[:]
		for spell in refreshActives:
			activeSpells.append(spell)

def castSpell(player, boss, activeSpells, newSpell):
	player["mp"] -= spellList[newSpell]["cost"]
	if newSpell == "magic missile":
		boss["hp"] -= 4
	elif newSpell == "drain":
		boss["hp"] -= 2
		player["hp"] += 2
	else:
		activeSpells.append([newSpell, spellList[newSpell]["turns"]])

	return spellList[newSpell]["cost"]

def solveARandomly(player, boss, reps):
	minManaSpent = 10000
	solveRandomly = True

	for i in range(reps):
		result = fight(player, boss, "normal", solveRandomly)
		if result >= 0 and result < minManaSpent:
			print "new min! " + str(result)
			minManaSpent = result

	return minManaSpent

def solveBRandomly(player, boss, reps):
	minManaSpent = 10000
	solveRandomly = True

	for i in range(reps):
		result = fight(player, boss, "hard", solveRandomly)
		if result >= 0 and result < minManaSpent:
			print "new min! " + str(result)
			minManaSpent = result

	return minManaSpent

def main():
	boss = {"hp": 51, "atk": 9}
	player = {"hp": 50, "mp": 500, "def": 0}
	numReps = 10000000

	#print solveARandomly(player, boss, numReps)
	print solveBRandomly(player, boss, numReps)

if __name__ == '__main__':
	main()