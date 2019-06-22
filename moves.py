from typing import Typing

class Move:
	def __init__(self, name, type, function):
		self.name = name
		self.type = type
		self.function = function
	
	def execute(self, poke_a, poke_b):
		mult = 1.0

		# Bonus de mesmo tipo do ataque.
		if self.type in {poke_a.type1, poke_a.type2}:
			mult += 0.5
		
		self.function(poke_a, poke_b, mult)
	
	def __str__(self):
		return self.name

def tackle(a, b, mult):
	dmg = round(40 * (a.attack / 300))
	dmg -= round(b.defense / 300)
	dmg *= mult
	b.curr_health -= max(dmg, 1)

def absorb(a, b, mult):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	dmg *= mult
	b.curr_health -= max(dmg, 1)
	a.curr_health += max(dmg // 2, 1)

def thundershock(a, b, mult):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	dmg *= mult
	b.curr_health -= dmg

def ember(a, b, mult):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	dmg *= mult
	b.curr_health -= dmg

def wing_attack(a, b, mult):
	dmg = round(60 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	dmg *= mult
	b.curr_health -= dmg

move_list = [
	Move("Tackle", Typing.Normal, tackle),
	Move("Absorb", Typing.Grass, absorb),
	Move("Thundershock", Typing.Electric, thundershock),
	Move("Ember", Typing.Fire, ember),
	Move("Wing Attack", Typing.Flying, wing_attack),
]