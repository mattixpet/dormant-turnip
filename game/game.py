"""Game
"""

import pygame as pg
from tools.resources import load_image
from mainloop import mainloop
from entities.abstract.entity import Entity
from entities.cards.abstract.card import Card
from entities.characters.soldier import Soldier
from entities.characters.swagavulin import Swagavulin
from entities.deck import Deck

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
    end_turn = Entity('end_turn', 0.6, (740,390))
    you_win = Entity('you_win', 0.7, (370,50))
    soldier = Soldier()
    swagavulin = Swagavulin()
    card = Card('frag_grenade', soldier, 150, True, 1)
    card1 = Card('frag_grenade', soldier, 5, True, 1)
    card2 = Card('frag_grenade', soldier, 5, True, 1)
    deck = Deck([card, card1, card2])
    allsprites = pg.sprite.RenderPlain((soldier, swagavulin, deck, end_turn))

    entities = {
        "end_turn": end_turn,
        "soldier": soldier,
        "swagavulin": swagavulin,
        "deck": deck,
        "you_win": you_win
    }

    # Turn initialization logic
    deck.new_turn()
    deck.update_hand()

    # Start the game!
    mainloop(screen, background, allsprites, entities)

    pg.quit()


if __name__ == "__main__":
    start_game()