from Deck.deck import Deck
from Participents.Hand import Hand


class Game:
    def __init__(self, dealer, players):
        """
        :param dealer: inserting dealer
        :param players: inserting players
        """
        self.dealer = dealer
        self.players = players
        self.log = Log()

    def win_or_lose(self, player):
        """
        A function that checks all the game scenarios and determine who wins according the conditions.
        in addition, changes the chip amount according the results
        if a player wins, he gets 1 chip and if he loses, he loses 1 chip
        same for the dealer
        """
        if player.player_hand.value() > 21:
            player.chip -= 1
            self.log.add_event(f"{player} BUSTED!")
            if self.dealer.dealer_hand.value() <= 21:
                self.log.add_event(f"{self.dealer} WINS!")
                # if dealer wins he gets 1 chip, player loses his bet
                self.dealer.chip += 1
            else:
                # if the dealer value is > 21, loses his bet and busted
                self.log.add_event(f"{self.dealer} BUSTED!")
                self.dealer.chip -= 1
        # if the player has 21, he's got blackjack and wins automatically
        elif player.player_hand.value() == 21:
            player.chip += 1
            self.dealer.chip -= 1
            self.log.add_event(f"{player} GOT BLACKJACK!, IT'S A WIN")
        else:
        # the player has under 21
            if self.dealer.dealer_hand.value() > 21:
                # the player < 21 and dealer > 21
                self.log.add_event(f"{player} WINS!")
                player.chip += 1
                self.dealer.chip -= 1
            else:
                # both player and dealer are under 21, doing comparison between player and dealer
                if player.player_hand.value() > self.dealer.dealer_hand.value():
                    # if player > dealer
                    self.log.add_event(f"{player} WINS!")
                    player.chip += 1
                    self.dealer.chip -= 1
                elif player.player_hand.value() == self.dealer.dealer_hand.value():
                    self.log.add_event(f"PUSH!")  # draw
                else:
                    # if dealer > player
                    self.log.add_event(f"{self.dealer} WINS!")
                    self.dealer.chip += 1
                    player.chip -= 1

    def reset(self):
        """
        A function that resets the game in each round :
        empties the player hand
        empties the dealer hand
        resets the deck
        resets the game log
        """
        for player in self.players:
            player.player_hand = Hand()
        self.dealer.dealer_hand = Hand()
        self.dealer.deck = Deck()
        self.log = Log()

    def run(self):
        """
        A function that begins the progress of the game
        first, using the 'reset' function and resets the game.
        shuffles the deck of cards once the game begins
        dealer deals 2 cards for each of the players'
        dealer deals 2 cards for himself.
        then,the function uses the given strategies and determines if hit or stand
        if hit, gets a card
        if stand , continue to the next player
        if the player is busted, continue to next player
        at the end, checks who won
        """
        # reset:
        self.reset()
        # shuffles the deck of cards once the game begins
        self.dealer.shuffle()
        # the dealer deals 2 cards for each player
        for player in self.players:
            self.log.add_event(f"{player}")
            for i in range(2):
                card = self.dealer.deal()
                player.player_hand.get_card(card)
                self.log.add_event(f"   gets {card}")
        # the dealer deals 2 card to himself
        self.log.add_event(f"{self.dealer}")
        for i in range(2):
            card = self.dealer.deal()
            self.dealer.dealer_hand.get_card(card)
            self.log.add_event(f"   gets {card}")
        # for each player:
        for player in self.players:
            self.log.add_event(f"{player}'s turn")
            # check if hit or stand
            while player.player_hand.value() <= 21:
                if player.strategy(player.player_hand, self.dealer.dealer_hand) == "hit":
                    self.log.add_event(f"{player}: Hit me!")
                    # if hit, gets a card
                    card = self.dealer.deal()
                    player.player_hand.get_card(card)
                    self.log.add_event(f"{player} gets {card}")
                    # if player busted, continue to next player
                    if player.player_hand.value() > 21:
                        self.log.add_event(f"{player} BUSTED!")
                # if player says 'stand', continue to next player
                else:  # stand
                    self.log.add_event(f"{player}: Stand!")
                    break

        # dealer's turn
        self.log.add_event(f"{self.dealer}'s turn")
        while self.dealer.dealer_hand.value() <= 21:
            if self.dealer.strategy(self.dealer.dealer_hand) == "hit":
                self.log.add_event(f"{self.dealer}: Hit me!")
                # if hit, gets a card
                card = self.dealer.deal()
                self.dealer.dealer_hand.get_card(card)
                self.log.add_event(f"{self.dealer} gets {card}")
                # if dealer busted, the player wins
                if self.dealer.dealer_hand.value() > 21:
                    self.log.add_event(f"{self.dealer} BUSTED!")
            # if dealer says 'stand', check who win
            else:  # stand
                self.log.add_event(f"{self.dealer}: Stand!")
                break

        # check who win
        for player in self.players:
            self.win_or_lose(player)


class Log:
    def __init__(self):
        """
        An empty list which gets the game events
        """
        self.events = []

    def add_event(self, str):
        """
        A function that adds the game events to the events list
        :param str: An event print, for example (the player won!)
        """
        self.events.append(str)

    def __str__(self):
        """
        :return: prints the game events one by one
        """
        return "\n".join(self.events)
