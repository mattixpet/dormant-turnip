"""Hunker down
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class HunkerDown(Card):
    """Hunker down
    Block incoming damage 75%
    Deal 25% less damage
    """
    def __init__(self):
        Card.__init__(self, 'hunker_down', damage=0, mana_cost=2, targeted=False, scale=1)

        self.text = """Block incoming
damage by 75%.
Reduce damage
this turn to 25%.
Mana cost: {mana}""".format(mana=self.mana_cost) 

    def use(self, user: Character, target: Character):
        Card.use(self, user, target)

        user.add_buff('hunker_down')
        target.notify_buff('hunker_down')
        