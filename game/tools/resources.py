"""
Functions to help with resources/loading/files/management I guess.. might be a better name out there
"""
import pygame as pg
import os
import json

def resource_to_path(key):
    """
    Looks up data/json/resources.json with key and uses the value from there to create a full path to return.

    Note: This could be unneccessarily performance heavy since it opens the file each time it is called,
    if the resources aren't too many we can read them all in and keep a table of the values in memory.
    """
    with open("data/json/resources.json") as resource_file:
        data = json.load(resource_file)
        path = data[key]

    return os.path.abspath(path)

def load_image(name, colorkey=None, scale=1):
    fullname = resource_to_path(name)
    image = pg.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = resource_to_path(name)
    sound = pg.mixer.Sound(fullname)

    return sound