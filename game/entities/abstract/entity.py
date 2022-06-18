"""Entity class
"""

import pygame as pg
from tools.resources import load_image, resource_to_path

class Entity(pg.sprite.Sprite):
    """Entity
    """
    def __init__(self, name: str, scale: float = 1, starting_pos: tuple[int,int] = (0,0)):
        self.name = name # Id of this entity, used for example for sprites

        pg.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image, self.rect = load_image(self.name, -1, scale)
        self.rect.topleft = starting_pos # Make sure sprite is drawn here even without update of pos

        self.pos = starting_pos # Set our position, default value top left


    def get_name(self):
        return self.name

    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos: tuple[int,int]):
        self.pos = new_pos

    def update(self):
        # Move to new position
        self.rect.topleft = self.pos
