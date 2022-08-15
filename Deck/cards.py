
class Card:
    def __init__(self, name, suit, value):
        """
        Created a card object which contains name,suit,value
        :param name: string card name
        :param suit: 'Heart', 'Club', 'Spade', 'Diamond'
        :param value: card integer values according the game rules and card suit
        """
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        :return: returns a card, for example (7,Heart)
        """
        return f"{self.name} {self.suit}"
