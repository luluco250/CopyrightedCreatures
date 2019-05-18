from ._base import Base
from typing import Typing

class Pikachu(Base):
	def __init__(self):
		super().__init__(
			index=25,
			name="Pikachu",
			type1=Typing.Electric,
			health=35,
			attack=55,
			sp_defense=50,
			sp_attack=50,
			defense=40,
			speed=90
		)