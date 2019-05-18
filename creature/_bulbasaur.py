from ._base import Base
from typing import Typing

class Bulbasaur(Base):
	def __init__(self):
		super().__init__(
			index=1,
			name="Bulbasaur",
			type1=Typing.Grass,
			type2=Typing.Poison,
			health=45,
			attack=49,
			defense=49,
			sp_attack=65,
			sp_defense=65,
			speed=45
		)