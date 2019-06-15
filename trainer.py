class Trainer:
	def __init__(self, name, money, creatures):
		self.name = name
		self.money = money
		self.creatures = creatures
	
	def list_creatures(self):
		print("{}'s creatures: ".format(self.name))
		for c in self.creatures:
			print(c.name)
	
	def defeated(self):
		result = True

		for creature in self.creatures:
			result = result and creature.fainted()
		
		return result