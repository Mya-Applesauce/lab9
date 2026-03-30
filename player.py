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

    def win_coin(self, gain):
        self.__wallet += gain

    def lose_coin(self, loss):
        self.__wallet -= loss

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name

#coin_toss = Player("n")

#for ii in range(10):
    #coin_toss.toss_coin()
    #print(f"after toss, side up is {coin_toss.get_coin_side()}")
    #if coin_toss.get_coin_side() == 0:
        #coin_toss.win_coin(1)
    #elif coin_toss.get_coin_side() == 1:
        #coin_toss.lose_coin(1)

#print(f"{coin_toss.get_name()}'s wallet has {coin_toss.get_wallet()} coins")