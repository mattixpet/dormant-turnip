"""Soldier class
"""

from entities.characters.abstract.character import Character

class Soldier(Character):
    """Soldier
    """

    def __init__(self):
        Character.__init__(self, 'soldier', 0.1, (200,270), 100)

    