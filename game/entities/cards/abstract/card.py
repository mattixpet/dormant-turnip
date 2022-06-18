"""Card class
Inherits from Entity.
Contains things Cards have in common but Entities do not.
"""

from entities.abstract.entity import Entity
from entities.characters.abstract.character import Character

class Card(Entity):
    """Card
    """
    
    def __init__(self, name: str, character: Character, damage: int = 0, mana_cost: int = 0, scale: float = 0.2):
        Entity.__init__(self, name, scale)

        self.character = character # The character using this card
        self.targeted = True
        self.damage = damage
        self.mana_cost = mana_cost

    def use(target: Character):
        """
        Do everything the card does once on `target` enemy (or self). 
        Leave it to the user of the card to make sure to remove the card from the hand afterwards.
        """
        target.receive_damage(self.damage + self.character.get_strength())


