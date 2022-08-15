
class Hand:
    def __init__(self):
        """
        resets the hand value
        an empty list of cards which will get the cards from the dealer
        resets the hand condition
        """
        self.cards = []
        self.hand_val = 0
        self.soft = False

    def get_card(self, card):
        """
        Adding a card to the cards list
        calculating the hand value using the 'calculate' function
        using the 'soft_or_hard' function to determine the hand condition
        """
        # adding card
        self.cards.append(card)
        # calculate hand value
        self.calculate(card)
        # check if soft
        self.soft_or_hard()

    def value(self):
        """
        :return: returns the hand value
        """
        return self.hand_val

    def soft_or_hard(self):
        """
        checks if soft or hard according to the game rules
        if hand has 'Ace' and his value is 11 -> soft
        if soft -> true
        """
        for card in self.cards:
            if card.name == "A" and card.value == 11:
                self.soft = True
                return
        self.soft = False

    def calculate(self, card):
        """
        calculating the card value
        """
        self.hand_val += card.value

        if self.hand_val > 21:
            for card in self.cards:
                if card.name == "A" and card.value == 11 and self.hand_val > 21:
                    card.value = 1
                    self.hand_val -= 10
