from trainer import Trainer
import creature

lucas = Trainer("Lucas", 20, [
	creature.Pikachu(),
	creature.Charmander(),
	creature.Squirtle(),
	creature.Bulbasaur()
])
lucas.list_creatures()

def tackle(a, b):
	b.curr_health -= round(40 * (a.attack / 255))

pikachu = lucas.creatures[0]
charmander = lucas.creatures[1]
pikachu.do_move(charmander, tackle)

pikachu.status()
charmander.status()