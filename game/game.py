import pygame as pg
from tools.resources import load_image
from mainloop import mainloop

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

def start_game():
    """Start game
    Sets everything up and then starts the game.
    """

    # Initialize Everything
    pg.init()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Slay the Swagavulin")

    # Create The Backgound
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Try and beat the Swagavulin", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    #chimp = Chimp()
    #fist = Fist()
    #allsprites = pg.sprite.RenderPlain((fist, chimp))
    allsprites = ''

    #image, rect = load_image("soldier", -1, 1)

    # Start the game!
    mainloop(screen, background, allsprites)

    pg.quit()


if __name__ == "__main__":
    start_game()