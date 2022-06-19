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
        # Current buffs possible:
        #     'hunker_down'
        #     'block'
        self.temporary_buffs = [] # Buffs only valid for a turn

        self.health_lost_this_turn = 0
        self.health_lost_last_turn = 0

        self.block = 0

        self.max_mana = 3
        self.mana = self.max_mana

    def receive_damage(self, amount: int):
        if 'hunker_down' in self.temporary_buffs:
            amount = round_number(amount * 0.25) # you happy Tumi? Round ekki floor
        if 'block' in self.temporary_buffs:
            block = self.block # store our block value temporarily
            self.block -= amount # update our block to be reduced
            amount = max(0, amount - block) # can't heal from block, so we max(0,..)
        self.health -= amount
        self.health_lost_this_turn += amount

    def new_turn(self):
        """New turn
        Called when turn ends. Reset our temporary buffs for example.
        """
        self.temporary_buffs = []
        self.health_lost_last_turn = self.health_lost_this_turn
        self.health_lost_this_turn = 0
        self.block = 0 # Reset block every turn
        self.mana = self.max_mana

    def add_buff(self, buff: str, value: int = 0):
        """Add buff
        `buff` is a name of buff. See possible buffs in __init__.
        Optional `value` to come with the buff. E.g. block value.
        """
        if buff in self.temporary_buffs:
            match buff:
                case 'hunker_down':
                    pass
                case 'block':
                    self.block += value
        else:
            if buff == 'block':
                self.block += value
            self.temporary_buffs.append(buff)

    def heal(self, amount: int):
        self.health += amount

    def use_mana(self, amount: int) -> bool:
        """Use mana
        Cards call this to let us know we used them so we can reduce our mana.

        Returns True if we have enough mana to play the card otherwise False
        """
        if self.mana < amount:
            return False
        self.mana -= amount
        return True

    def is_dead(self) -> bool:
        return self.health <= 0

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