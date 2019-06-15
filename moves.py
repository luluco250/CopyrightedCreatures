def tackle(a, b):
	dmg = round(40 * (a.attack / 300))
	dmg -= round(b.defense / 300)
	b.curr_health -= max(dmg, 1)

def absorb(a, b):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	b.curr_health -= max(dmg, 1)
	a.curr_health += max(dmg // 2, 1)

def thundershock(a, b):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	b.curr_health -= dmg

def ember(a, b):
	dmg = round(40 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	b.curr_health -= dmg

def wing_attack(a, b):
	dmg = round(60 * (a.sp_attack / 300))
	dmg -= round(b.sp_defense / 300)
	b.curr_health -= dmg