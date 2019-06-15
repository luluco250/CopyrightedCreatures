from ._base import Base
from typing import Typing

class Pidgey(Base):
	def __init__(self):
		super().__init__(
			index=16,
			name="Pidgey",
			type1=Typing.Normal,
            type2=Typing.Flying,
			health=40,
			attack=45,
            defense=40,
            sp_attack=35,
			sp_defense=35,
			speed=56
		)