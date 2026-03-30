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

    