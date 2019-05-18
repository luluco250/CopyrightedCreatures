from ._base import Base
from typing import Typing

class Charmander(Base):
	def __init__(self):
		super().__init__(
			index=4,
			name="Charmander",
			type1=Typing.Fire,
			health=39,
			attack=52,
			defense=43,
			sp_attack=60,
			sp_defense=50,
			speed=65
		)