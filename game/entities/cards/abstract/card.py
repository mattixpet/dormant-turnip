"""Card class
Inherits from Entity.
Contains things Cards have in common but Entities do not.
"""

from entities.abstract.entity import Entity
from entities.characters.abstract.character import Character

class Card(Entity):
    """Card
    """
    
    def __init__(self, name: str, damage: int = 0, mana_cost: int = 0):
        Entity.__init__(self, name)

        self.targeted = True
        self.damage = damage
        self.mana_cost = mana_cost

    def use(target: Character):
        """
        Do everything the card does once on `target` enemy (or self). 
        Leave it to the user of the card to make sure to remove the card from the hand afterwards.
        """
        target.damage(self.damage)


