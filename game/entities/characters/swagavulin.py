"""Swagavulin class
"""

import random
from entities.characters.abstract.character import Character

class Swagavulin(Character):
    """Swagavulin
    """

    def __init__(self):
        Character.__init__(self, 'swagavulin', 0.6, (860,10), 150)

        # List of things Swagavulin can do to the character
        self.actions = [
            'debuff by 3',
            '6x2 damage',
            '20 damage',
            '10 damage'
        ]

        self.current_action = random.choice(self.actions)

    def perform_action(self, target: Character) -> None:
        """Use action
        Swagavulin goes stabby stabby (or debuffy debuffy) on `target`

        Then updates to next action.
        """
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

    def get_intent(self) -> str:
        """Get intent
        Get info on what Swagavulin intends to do next
        """
        return self.current_action