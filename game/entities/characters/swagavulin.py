"""Swagavulin class
"""

import random
import pygame as pg # just for type hints
from entities.characters import Character

class Swagavulin(Character):
    """Swagavulin
    """

    def __init__(self):
        Character.__init__(self, 'swagavulin', 0.6, (860,10), 150)

        self.health_pos = (1040,380)
        self.intent_pos = (840,100)

        # List of things Swagavulin can do to the character
        self.actions = [
            'debuff by 3',
            '6x2 damage',
            '20 damage',
            '10 damage'
        ]

        self.current_action = random.choice(self.actions)

    def draw_extras(self, screen: pg.Surface):
        """Draw extras
        Draw health and next intent
        """
        if pg.font:
            # Draw health
            font = pg.font.Font(None, 32)
            text = font.render("Health: {health}".format(health=self.health), True, (10, 10, 10))
            screen.blit(text, self.health_pos)

            # Draw intent
            font = pg.font.Font(None, 48)
            color = (10,150,10) if self.current_action == 'debuff by 3' else (255,10,10)
            text = font.render("{action} incoming".format(action=self.current_action), True, color)
            screen.blit(text, self.intent_pos)

    def perform_action(self, target: Character) -> None:
        """Use action
        Swagavulin goes stabby stabby (or debuffy debuffy) on `target`

        Then updates to next action.
        """
        if self.health <= 0:
            # Can't do much if we're dead right?
            return

        match self.current_action:
            case 'debuff by 3':
                target.add_strength(-3)
            case '6x2 damage':
                target.receive_damage(12)
            case '20 damage':
                target.receive_damage(20)
            case '10 damage':
                target.receive_damage(10)

        self.current_action = random.choice(self.actions)
