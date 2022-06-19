"""Character class
"""

from tools.util import round_number
from entities.abstract.entity import Entity

class Character(Entity):
    """Character
    """
    def __init__(self, name: str, scale: float = 1, pos: tuple[int,int] = (0,0), health: int = 100):
        Entity.__init__(self, name, scale, pos)

        self.health = health
        self.strength = 0
        self.temporary_buffs = [] # Buffs only valid for a turn

        self.health_lost_this_turn = 0
        self.health_lost_last_turn = 0

    def receive_damage(self, amount: int):
        if 'hunker_down' in self.temporary_buffs:
            amount = round_number(amount * 0.25) # you happy Tumi? Round ekki floor
        self.health -= amount
        self.health_lost_this_turn += amount

    def new_turn(self):
        """New turn
        Called when turn ends. Reset our temporary buffs for example.
        """
        self.temporary_buffs = []
        self.health_lost_last_turn = self.health_lost_this_turn
        self.health_lost_this_turn = 0

    def add_buff(self, buff: str):
        self.temporary_buffs.append(buff)

    def heal(self, amount: int):
        self.health += amount

    def get_damage_last_turn(self):
        return self.health_lost_last_turn

    def get_buffs(self):
        return self.temporary_buffs

    def get_health(self) -> int:
        return self.health

    def get_strength(self) -> int:
        return self.strength

    def add_strength(self, amount: int) -> None:
        """Add strength
        Increase character strength by `amount` (positive or negative).
        """
        self.strength += amount