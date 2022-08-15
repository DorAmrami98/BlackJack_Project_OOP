from Participents.Hand import Hand
from strategies import strategy1


class Player:
    def __init__(self, name="PLAYER", chip=10, strategy=strategy1):
        """
        A player class which contains his name ,chip quantity and the strategy he uses
        :param name: player name
        :param chip: player budget, default 10 chips
        :param strategy: default strategy 1
        """
        self.name = name
        self.chip = chip
        self.player_hand = Hand()
        self.strategy = strategy

    def __str__(self):
        """
        :return: return the player name
        """
        return f"PLAYER: {self.name}"
