from random import shuffle


class DeckError(Exception):
    pass


class CardError(Exception):
    pass

ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')


class Card:

    def __init__(self, value, suit):
        if value not in ranks:
            raise ValueError("Value must be from 1 to 13")
        if str(suit).capitalize() not in suits:
            raise ValueError("Must use a valid suit of card not: {0}".format(suit))

        self.value = value
        self.suit = suit

    def str(self):
        return '{0} of {1}'.format(ranks[self.value], self.suit.capitalize())


class Deck:

    def __init__(self, deckname, decksize=1, isdeck=True):
        self.deck = []
        if isdeck is True:
            for x in range(decksize):
                self.deck = [Card(y, x) for x in suits for y in ranks]

        self.deckname = str(deckname)

    def __invert__(self):
        shuffle(self.deck)

    def __call__(self):
        return [str(x) for x in self.deck]

    def __repr__(self):
        return repr(str(self.deck))

    def __add__(self, o):

        if isinstance(o, Card):
            self.addCard(o)
        elif isinstance(o, Deck):
            for card in o.deck:
                self.addCard(card)
        else:
            raise TypeError('You cannot add "{0}" to deck, only Deck or Card'.format(type(o)))

    def draw(self):
        if len(self.deck) < 1:
            raise DeckError('{0}\'s deck is empty!'.format(self.deckname))
        return self.deck.pop(0)

    def addCard(self, card):
        if not isinstance(card, Card):
            raise CardError("Must be of type Card, not: {0}".format(type(card)))
        self.deck.append(card)
