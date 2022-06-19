"""Flash grenade
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class FlashGrenade(Card):
    """Flash grenade
    """
    def __init__(self):
        Card.__init__(self, 'flash_grenade', damage=0, mana_cost=3, targeted=True, scale=0.2)

        self.title = "Flash grenade"
        self.text = """Stuns enemy for 1 
            turn.
Mana cost: {mana}""".format(mana=self.mana_cost) 

    def use(self, user: Character, target: Character):
        can_play = Card.use(self, user, target)
        if not can_play:
            return False
        target.get_stunned() # Stun our target!
        return True