from Participents.Dealer import Dealer
from strategies import strategy1, strategy3
from Participents.Player import Player
from Game.Blackjack import Game


# a few simple test functions
# test 1 game example
def test():
    dealer = Dealer('Eli', 10000)
    a = Player('Alice', 100, strategy1)
    b = Player('Bob', 200, strategy3)
    c = Player('Clod', 100, strategy1)
    d = Player('Dian', 250, strategy3)
    print("Dealer:", dealer.name)
    print("Players:", a.name, b.name, c.name, d.name)
    players = [a, b, c, d]
    g = Game(dealer, players)
    g.run()
    print(g.log)


# test simulation of 300 games
def test_sim():
    dealer = Dealer('Eli', 10000)
    a = Player('Alice', 500, strategy3)
    b = Player('Bob', 500, strategy1)
    c = Player('Clod', 500, strategy1)
    for i in range(300):
        g = Game(dealer, [a, b, c])
        g.run()
        print(a.name, a.chip)  # which budget is higher?
        print(b.name, b.chip)
        print(c.name, c.chip)


test()
print("")
# print("-CHIP COUNT-")
# test_sim()
