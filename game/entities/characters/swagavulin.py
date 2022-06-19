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
        # Note: This should be in a table somewhere to be references,
        #       so that if we change the text it is reflected everywhere
        self.actions = [
            'debuff by 3',
            '6x2 damage',
            '20 damage',
            '10 damage',
            '6x2 damage',
            '20 damage',
            '10 damage'
        ]

        self.current_action = '???' # Start by doing nothing
        self.intent = self.current_action # This changes if cahracter is buffer for example

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
            color = (200,200,0) if self.current_action == '***' or self.current_action == '???' else color
            display_text = "{action} incoming".format(action=self.intent)
            if self.current_action == '***' or self.current_action == '???':
                display_text = self.current_action
            text = font.render(display_text , True, color)
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
                target.receive_damage(6)
                target.receive_damage(6)
            case '20 damage':
                target.receive_damage(20)
            case '10 damage':
                target.receive_damage(10)
            case '***':
                pass # We're stunned, do nothing
            case _:
                pass # ???

        self.current_action = random.choice(self.actions)
        self.intent = self.current_action

    def get_stunned(self):
        """Get stunned
        We're stunned! Lose our next action.

        Note: This should probably be part of an "Enemy class" which inherits from Character.
        """
        self.current_action = '***'
        self.intent = self.current_action

    def notify_buff(self, buff: str):
        """Notify buff
        Let us know our opponent has a buff, which may impact our intent
        """
        if buff == 'hunker_down':
            match self.current_action:
                case 'debuff by 3':
                    pass
                case '6x2 damage':
                    self.intent = '2x2 damage'
                case '20 damage':
                    self.intent = '5 damage'
                case '10 damage':
                    self.intent = '3 damage'