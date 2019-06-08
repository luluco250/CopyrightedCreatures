def tackle(a, b):
	dmg = round(40 * (a.attack / 255))
	dmg -= round(b.defense / 255)
	b.curr_health -= max(dmg, 1)

def absorb(a, b):
	dmg = round(40 * (a.sp_attack / 255))
	dmg -= round(b.sp_defense / 255)
	b.curr_health -= max(dmg, 1)
	a.curr_health += max(dmg // 2, 1)

def thundershock(a, b):
	dmg = round(40 * (a.sp_attack / 255))
	dmg -= round(b.sp_defense / 255)
	b.curr_health -= dmg

def ember(a, b):
	dmg = round(40 * (a.sp_attack / 255))