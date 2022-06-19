"""Riot shield
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class RiotShield(Card):
    """Riot shield
    Block x damage
    """
    def __init__(self):
        Card.__init__(self, 'riot_shield', damage=0, mana_cost=1, targeted=False, scale=0.25)

        self.block = 7

        self.title = "Riot shield"
        self.text = """Block for {block}.
Mana cost: {mana}""".format(block=self.block, mana=self.mana_cost) 

    def use(self, user: Character, target: Character):
        can_play = Card.use(self, user, target)
        if not can_play:
            return False

        user.add_buff('block', self.block)

        return True
        