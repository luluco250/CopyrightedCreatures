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
		self.type1 = type1
		self.type2 = type2

		# Base stats.
		self.attack = attack
		self.defense = defense
		self.sp_attack = sp_attack
		self.sp_defense = sp_defense
		self.speed = speed
		self.health = health
		
		# Combat variables.
		self.curr_health = health

		# Buffs reset after battle.
		self.attack_buff = 0
		self.defense_buff = 0
		self.sp_attack_buff = 0
		self.sp_defense_buff = 0
		self.speed_buff = 0
	
	def status(self):
		type2_text = ""

		if self.type2 != Typing.Null:
			type2_text = self.type2.name
		
		print(
"""[{}]
HP: {}/{}
ATK: {}
DEF: {}
SP_ATK: {}
SP_DEF: {}
SPD: {}""".format(
		self.name,
		self.curr_health,
		self.health,
		self.attack,
		self.defense,
		self.sp_attack,
		self.sp_defense,
		self.speed
	))
	
	def do_move(self, other, move):
		move(self, other)