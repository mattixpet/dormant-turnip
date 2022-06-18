"""Frag grenade class
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class FragGrenade(Card):
    """Frag grenade
    """
    def __init__(self, character: Character):
        Card.__init__(self, 'frag_grenade', character, damage=5, mana_cost=1, targeted=True, scale=0.2)

        self.text = """Damage to all: {dmg}
        Mana cost: {mana}""".format(dmg=self.damage, mana=self.mana_cost) 

