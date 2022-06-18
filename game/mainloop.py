"""Mainloop
"""

import pygame as pg
from entities.abstract.entity import Entity # only used for type hints
from entities.characters.abstract.character import Character # only used for type hints

def mainloop(screen: pg.Surface, background: pg.Surface, allsprites: pg.sprite.Group, entities: list[Entity]):
    """Mainloop
    """
    clock = pg.time.Clock()

    end_turn = entities["end_turn"]
    soldier = entities["soldier"]
    swagavulin = entities["swagavulin"]
    deck = entities["deck"]
    you_win = entities["you_win"]

    going = True
    while going:
        clock.tick(60)

        # Handle Input Events and Logic (in the future this should be in a separate functions/classes)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

                deck.use_card(pos, swagavulin)
                deck.update_hand()

                if swagavulin.get_health() <= 0:
                    allsprites.add(you_win)

                if end_turn.rect.collidepoint(pos):
                    deck.new_turn()
                    deck.update_hand()

        # Update
        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        deck.draw_hand(screen)
        allsprites.draw(screen)
        pg.display.flip()
