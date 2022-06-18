"""Deck class
Contains discard pile, players hand and draw pile and exhausted (if we have that mechanic)
"""

import random
import pygame as pg
from entities import Entity
from entities.characters import Character
from entities.cards import Card # only for type hinting

class Deck(Entity):
    """Deck
    """
    def __init__(self, cards: list[Card]):
        Entity.__init__(self, 'deck', 0.17, (30,330))

        self.cards = cards.copy() # maintain a copy of our entire deck

        self.deck = cards
        self.hand = []
        self.discard = []

        self.handsize = 3

        self.card_positions = [
            (360,250),
            (530,250),
            (700,250)
        ]

        self.hand_sprites = None # Used for displaying our hand on screen

    def update_hand(self):
        """Update
        Update our sprite list with sprites in hand and positions applicable
        """
        for i in range(len(self.hand)):
            self.hand[i].set_pos(self.card_positions[i])
            self.hand[i].update()

        self.hand_sprites = pg.sprite.RenderPlain(self.hand)

    def draw_hand(self, screen: pg.Surface):
        """Draw hand
        Draws our current hand on the screen.
        """
        self.hand_sprites.draw(screen)
        for card in self.hand:
            card.draw_text(screen)

    def new_turn(self):
        """New turn
        Discard our hand and draw up to `self.handsize`
        """
        while self.hand != []:
            self.discard.append(self.hand.pop())

        for i in range(self.handsize):
            self._draw_card()

    def use_card(self, pos: tuple[int,int], target: Character):
        """Use card
        Attempt to use a card on `target` when user clicks `pos`. If no card is there, do nothing.
        """
        for card in self.hand:
            if card.rect.collidepoint(pos):
                card.use(target)
                self._discard_card(card)

    def _draw_card(self):
        """Draw card
        """
        if self.deck == []:
            # Our deck is empty, shuffle discard pile into draw pile
            self._shuffle()

        self.hand.append(self.deck.pop())

    def _discard_card(self, card: Card):
        """Discard card
        """
        self.hand.remove(card)
        self.discard.append(card)

    def _shuffle(self):
        """Shuffle
        Shuffles our discard pile into our deck
        """
        # Move all cards from discard to our deck
        while self.discard != []:
            self.deck.append(self.discard.pop())

        # Then shuffle the deck
        random.shuffle(self.deck)