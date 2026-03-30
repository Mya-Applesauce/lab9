"""
player
Ari Papke
player class
03/29/26
"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

    #def win_coin(self):

    #def lose_coin(self):

    #def get_wallet(self):

    #def get_name(self):

coin_toss = Player("n")

for ii in range(10):
    coin_toss.toss_coin()
    print(f"after toss, side up is {coin_toss.get_coin_side()}")