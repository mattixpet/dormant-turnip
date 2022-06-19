"""360 no scope
"""

import random
from entities.cards import Card
from entities.characters import Character # only for type hints

class NoScope360(Card):
    """360 no scope memes
    """
    def __init__(self, end_turn_callback: callable, end_turn_callback_args: list):
        Card.__init__(self, '360noscope', damage=5, mana_cost=2, targeted=True, scale=0.5)

        self.title = "360 Memes"

        self.end_turn_callback = end_turn_callback
        self.end_turn_callback_args = end_turn_callback_args

        self.whiff_damage = 5
        self.pow_damage = 150

        self.text = """10% {pow} damage
90% {whiff} damage and 
            end turn
Mana cost: {mana}""".format(pow=self.pow_damage, whiff=self.whiff_damage, mana=self.mana_cost) 


    def use(self, user: Character, target: Character):
        # determine if we whiff or MAX DAMAGE
        if random.random() < 0.1:
            self.damage = self.pow_damage
        else:
            self.damage = self.whiff_damage

        Card.use(self, user, target)

        if self.damage == self.whiff_damage:
            # We whiffed, end our turn
            self.end_turn_callback(*self.end_turn_callback_args)
            return 'dont discard'