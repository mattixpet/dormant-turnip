"""Med kit
"""

from entities.cards import Card
from entities.characters import Character # only for type hints

class MedKit(Card):
    """Med(ical) kit
    Heal damage taken last turn.
    """
    def __init__(self):
        Card.__init__(self, 'med_kit', damage=0, mana_cost=1, targeted=False, scale=0.15)

        self.text = """Heal damage taken
last turn.
Mana cost: {mana}""".format(mana=self.mana_cost) 

    def use(self, user: Character, target: Character):
        Card.use(self, user, target)

        user.heal(user.get_damage_last_turn())
        