from ._base import Base
from typing import Typing

class Squirtle(Base):
	def __init__(self):
		super().__init__(
			index=7,
			name="Squirtle",
			type1=Typing.Water,
			health=44,
			attack=48,
			defense=65,
			sp_attack=50,
			sp_defense=64,
			speed=43
		)