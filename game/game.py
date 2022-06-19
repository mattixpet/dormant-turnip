"""Game
"""

import pygame as pg
from tools.resources import load_image
from mainloop import mainloop, end_turn
from entities import Entity, Deck
from entities.characters import Soldier, Swagavulin
from entities.cards import FragGrenade, NoScope360, FlashGrenade, HunkerDown, MedKit, RiotShield, Ump45

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

def start_game():
    """Start game
    Sets everything up and then starts the mainloop.
    """

    # Initialize everything
    pg.init()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    pg.display.set_caption("Slay the Swagavulin")

    # Create the backgound
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put text on the background, centered
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Try and beat the Swagavulin", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display the background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare game objects
    end_turn_button = Entity('end_turn', 0.5, (800,400))
    you_win = Entity('you_win', 0.7, (370,50))
    character_dead = Entity('character_dead', 0.9, (300,30))
    soldier = Soldier()
    swagavulin = Swagavulin()
    deck = Deck(
        soldier,
        [
            FragGrenade(),
            FragGrenade(),
            FragGrenade(),
            FlashGrenade(),
            FlashGrenade(),
            HunkerDown(),
            MedKit(),
            RiotShield(),
            RiotShield(),
            RiotShield(),
            Ump45()
        ]
    )

    allsprites = pg.sprite.RenderPlain((soldier, swagavulin, deck, end_turn_button))

    # 360noscope can end turn, so it needs the end turn function and it's arguments
    # and manual adding here after deck is created
    deck.add_card(
        NoScope360(end_turn, [deck, swagavulin, soldier, character_dead, allsprites])
    )

    entities = {
        "end_turn_button": end_turn_button,
        "soldier": soldier,
        "swagavulin": swagavulin,
        "deck": deck,
        "you_win": you_win,
        "character_dead": character_dead
    }

    # Turn initialization logic
    deck.new_turn()
    deck.update_hand()

    # Start the game!
    mainloop(screen, background, allsprites, entities)

    pg.quit()


if __name__ == "__main__":
    start_game()