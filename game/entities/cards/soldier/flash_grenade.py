"""Flash grenade
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class FlashGrenade(Card):
    """Flash grenade
    """
    def __init__(self):
        Card.__init__(self, 'flash_grenade', damage=0, mana_cost=2, targeted=True, scale=0.2)

        self.text = """Stuns enemy for 1 
            turn.
Mana cost: {mana}""".format(mana=self.mana_cost) 

    def use(self, user: Character, target: Character):
        Card.use(self, user, target)
        target.get_stunned() # Stun our target!