from typing import Typing

class Base:
	def __init__(
		self,
		index,
		name,
		attack,
		defense,
		sp_attack,
		sp_defense,
		speed,
		health,
		type1,
		type2=Typing.Null
	):
		self.index = index
		self.name = name
		self.attack = attack
		self.defense = defense
		self.sp_attack = sp_attack
		self.sp_defense = sp_defense
		self.speed = speed
		self.health = health
		self.type1 = type1
		self.type2 = type2
	
	def status(self):
		type2_text = ""

		if self.type2 != Typing.Null:
			type2_text = self.type2.name
		
		print("[{}]".format())