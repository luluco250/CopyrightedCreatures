from trainer import Trainer
import creature
import moves

lucas = Trainer("Lucas", 20, [
	creature.Pikachu(),
	creature.Charmander(),
	creature.Squirtle(),
	creature.Bulbasaur()
])
lucas.list_creatures()

pikachu = lucas.creatures[0]
charmander = lucas.creatures[1]
squirtle = lucas.creatures[2]
bulbasaur = lucas.creatures[3]

bulbasaur.do_move(squirtle, moves.absorb)
bulbasaur.status()
squirtle.status()