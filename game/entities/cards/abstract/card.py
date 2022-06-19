"""Card class
Inherits from Entity.
Contains things Cards have in common but Entities do not.
"""

import pygame as pg
from tools.util import round_number
from entities import Entity
from entities.characters import Character

class Card(Entity):
    """Card
    """
    def __init__(self, name: str, damage: int = 0, mana_cost: int = 0, targeted: bool = True, scale: float = 0.2):
        Entity.__init__(self, name, scale)

        self.targeted = targeted
        self.damage = damage
        self.mana_cost = mana_cost

        self.text = "Damage: {dmg}\nMana cost: {mana}".format(dmg=self.damage, mana=self.mana_cost)
        self.text_pos = (self.rect.bottomleft[0], self.rect.bottomleft[1]+10)

    def update(self):
        Entity.update(self)
        self.text_pos = (self.rect.bottomleft[0], self.rect.bottomleft[1]+10)

    def draw_text(self, screen: pg.Surface):
        lines = self.text.split('\n')
        font = pg.font.Font(None, 24)
        i = 0
        for line in lines:
            text = font.render(line, True, (10, 10, 10))
            screen.blit(text, (self.text_pos[0], self.text_pos[1] + i*15))
            i += 1

    def use(self, user: Character, target: Character):
        """Use
        Do everything the card does as `user` once on `target` enemy (or self). 
        Leave it to whoever uses the class to make sure to remove the card from the hand afterwards.
        """
        user_buffs = user.get_buffs()
        damage = self.damage + user.get_strength()
        if 'hunker_down' in user_buffs:
            damage = round_number(damage * 0.25) # you happy Tumi? Round ekki floor
        target.receive_damage(max(damage, 0)) # can't deal negative damage, so we max(dmg,0)
