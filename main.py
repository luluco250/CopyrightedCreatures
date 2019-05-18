from trainer import Trainer
import creature

lucas = Trainer("Lucas", 20, [
	creature.Pikachu(),
	creature.Charmander(),
	creature.Squirtle(),
	creature.Bulbasaur()
])
lucas.list_creatures()