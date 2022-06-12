import pygame as pg
from tools.resources import load_image

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

def start_game():
    '''
    Sets everything up and then starts the game.
    '''

    # Initialize Everything
    pg.init()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Slay the Swagavulin")

    # Create The Backgound
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    

    #image, rect = load_image('soldier', -1, 1)


if __name__ == "__main__":
    start_game()