from ._base import Base
from typing import Typing

class Geodude(Base):
	def __init__(self):
		super().__init__(
			index=74,
			name="Geodude",
			type1=Typing.Rock,
            type2=Typing.Ground,
			health=40,
			attack=80,
            defense=100,
            sp_attack=30,
			sp_defense=30,
			speed=20
		)