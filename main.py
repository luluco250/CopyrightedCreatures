from trainer import Trainer
import creature
import moves

red = Trainer("Ash", 20, [
	creature.Pikachu(),
	creature.Charmander(),
	creature.Squirtle(),
])

gold = Trainer("Ethan", 10, [
	creature.Geodude(),
	creature.Bulbasaur(),
	creature.Pidgey(),
])

pikachu = lucas.creatures[0]
charmander = lucas.creatures[1]
squirtle = lucas.creatures[2]
bulbasaur = lucas.creatures[3]

bulbasaur.do_move(squirtle, moves.absorb)
bulbasaur.status()
squirtle.status()