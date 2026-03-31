"""
Lab 9
Ari Papke
coin matching game
03/29/26
"""

from player import Player

def main():
    player1 = Player("Sonic")
    player2 = Player("Tails")

    print(f"+++ Coin Match Madness! +++")

    active = True

    while active:
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")
    
        keep_playing = input("Do you want to play? (y/n): ")
        if keep_playing == "y" or keep_playing == "Y" or keep_playing == "yes" or keep_playing == "Yes":
            active = True
        elif keep_playing == "n" or keep_playing == "N" or keep_playing == "no" or keep_playing == "No":
            active = False
        else:
            print("That isn't an answer!")

        player1.toss_coin()
        player2.toss_coin() 

main()  