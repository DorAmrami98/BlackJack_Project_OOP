import random
from Deck.deck import Deck
from strategies import strategy_dealer
from Participents.Hand import Hand

class Dealer:
    def __init__(self, name="Dealer", chip: int = 1000):
        """
        :param name: Dealer name
        :param chip: budget
        """
        self.name = name
        self.chip = chip
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.strategy = strategy_dealer

    def __str__(self):
        """
        :return: return the dealer name
        """
        return f"DEALER: {self.name}"

    def shuffle(self):
        """
        The dealer takes the deck of cards and shuffles it only once (if the deck is full)
        """
        if len(self.deck.list_of_cards) < 52:
            raise Exception("can only be shuffled if The Deck Is full")
        random.shuffle(self.deck.list_of_cards)

    def deal(self):
        """
        The dealer using the "deal" function in order to take a card from the shuffled deck
        :return: returns the deck without the removed card
        """
        if len(self.deck.list_of_cards) == 0:
            raise Exception("the deck is empty")
        return self.deck.list_of_cards.pop()
