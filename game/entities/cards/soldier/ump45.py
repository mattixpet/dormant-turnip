"""UMP45
The OP of the OP.
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class Ump45(Card):
    """UMP45
    The OP of the OP.
    """
    def __init__(self):
        Card.__init__(self, 'ump45', damage=20, mana_cost=1, targeted=True, scale=0.2)

        self.text = """Damage: {dmg}
Mana cost: {mana}""".format(dmg=self.damage, mana=self.mana_cost) 

