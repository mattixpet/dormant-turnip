"""mainloop.py
"""

import pygame as pg

def mainloop(screen, background, allsprites):
    """Mainloop
    """
    clock = pg.time.Clock()

    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pg.MOUSEBUTTONUP:
                fist.unpunch()

        #allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        #allsprites.draw(screen)
        pg.display.flip()
