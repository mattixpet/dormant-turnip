"""Soldier class
"""

import pygame as pg
from entities.characters import Character

class Soldier(Character):
    """Soldier
    """
    def __init__(self):
        Character.__init__(self, 'soldier', scale=0.1, pos=(200,270), health=100)

        self.health_pos = (210,170)
        self.strength_pos = (self.health_pos[0], self.health_pos[1]+25)
        self.block_pos = (self.health_pos[0], self.health_pos[1]+50)
        self.mana_pos = (self.health_pos[0], self.health_pos[1]+75)

    def draw_extras(self, screen: pg.Surface):
        """Draw extras
        Draw health, strength and more
        """
        if pg.font:
            # Draw health
            font = pg.font.Font(None, 32)
            text = font.render("Health: {health}".format(health=self.health), True, (10, 10, 10))
            screen.blit(text, self.health_pos)

            # Draw strength
            font = pg.font.Font(None, 32)
            text = font.render("Strength: {strength}".format(strength=self.strength), True, (10, 10, 10))
            screen.blit(text, self.strength_pos)

            # Draw block
            font = pg.font.Font(None, 32)
            text = font.render("Block: {block}".format(block=self.block), True, (10, 10, 10))
            screen.blit(text, self.block_pos)

            # Draw mana
            font = pg.font.Font(None, 32)
            text = font.render("Mana: {mana}".format(mana=self.mana), True, (10, 10, 10))
            screen.blit(text, self.mana_pos)