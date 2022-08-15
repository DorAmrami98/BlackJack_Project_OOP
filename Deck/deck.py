from Deck.cards import Card


class Deck:
    def __init__(self):
        """
        Created a card values dictionary according to the game rules
        in addition list of cards which the card values being inserted to
        """
        self.list_of_cards = []
        card_values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                            'K': 10, 'A': 11}
        suits = ['Heart', 'Club', 'Spade', 'Diamond']
        for suit in suits:
            for key in card_values_dict:
                card = Card(key, suit, card_values_dict[key])
                self.list_of_cards.append(card)

    def __str__(self):
        """
        :return: returns the deck of cards
        """
        return f"The Deck Of Cards:\n {self.list_of_cards}"
