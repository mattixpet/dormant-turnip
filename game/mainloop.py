"""Mainloop
"""

import pygame as pg
from entities import Entity, Deck # only used for type hints
from entities.characters import Character # only used for type hints

def end_turn(deck: Deck, enemy: Character, playing_character: Character):
    """End turn
    Function to do logic at end of turn. To be used as callback from cards which end turn (360 noscope)
    """
    enemy.perform_action(playing_character) # enemy gets to hurt us now
    deck.new_turn()
    deck.update_hand()
    playing_character.new_turn()

def mainloop(screen: pg.Surface, background: pg.Surface, allsprites: pg.sprite.Group, entities: list[Entity]):
    """Mainloop
    """
    clock = pg.time.Clock()

    end_turn_button = entities["end_turn_button"]
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
                # Game logic
                pos = pg.mouse.get_pos()

                deck.use_card(pos, swagavulin)
                deck.update_hand()

                if swagavulin.get_health() <= 0:
                    allsprites.add(you_win)

                if end_turn_button.rect.collidepoint(pos):
                    end_turn(deck, enemy=swagavulin, playing_character=soldier)

        # Update
        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        deck.draw_hand(screen)
        allsprites.draw(screen)
        # Hack to draw text/health/stats of swagavulin and soldier
        # Normally would be just one draw function for these
        swagavulin.draw_extras(screen)
        soldier.draw_extras(screen)
        pg.display.flip()
