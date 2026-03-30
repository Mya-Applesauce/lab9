"""coin
Ari Papke
coin class
03/29/26
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads!"

    def toss(self):
        side = random.randrange(2)
        if side == 0:
            self.__sideup = "Heads!"
        elif side == 1:
            self.__sideup = "Tails!" 
        else:
            print("I don't understand ranges")

    def get_sideup(self):
        return self.__sideup

coin_toss = Coin()

print("the value of the coin before we toss it is", 
      coin_toss.get_sideup())
for ii in range(10):
    coin_toss.toss()
    print(f"after toss, side up is {coin_toss.get_sideup()}")
