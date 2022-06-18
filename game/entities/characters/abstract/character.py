"""Character class
"""

from entities.abstract.entity import Entity

class Character(Entity):
    """Character
    """
    def __init__(self, name: str, scale: float = 1, pos: tuple[int,int] = (0,0), health: int = 100):
        Entity.__init__(self, name, scale, pos)

        self.health = health

        self.strength = 0

    def receive_damage(self, amount: int):
        self.health -= amount

    def get_strength(self, ) -> int:
        return self.strength

    def add_strength(self, amount: int) -> None:
        """Add strength
        Increase character strength by `amount` (positive or negative).
        """
        self.strength += amount