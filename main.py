import time 
import random
from utilities.classes import *

d = DisplayManager()
d.welcomeMessage()

p1,p2, whoPlaysFirst = d.settingPlayers()
if p1 == whoPlaysFirst :
    p1.symbol = "x"
    p2.symbol = "O"
else :
    p1.symbol = "O"
    p2.symbol = "X"
 
running = True 
validInput = ["1","2","3","4","5","6","7","8","9"]
currentPlayer = whoPlaysFirst
playAgain = "-1"

while running:
    #setting the other player
    if currentPlayer == p1:
        otherPlayer = p2
    else :
        otherPlayer = p1
    
    d.roundHandling(currentPlayer,otherPlayer,validInput)

    if currentPlayer.test():
        print(f"{currentPlayer.name} has won\n")
        playAgain=input("""game over
enter 1 to play again or enter 0 to exit
/****************************************/
""")

    elif len(validInput) == 0: 
        print("no one wins\n")
        playAgain=input("""game over
enter 1 to play again or enter 0 to exit
/****************************************/
""")

    if playAgain == "1":
        print("welcome again !!!")
        p1,p2, whoPlaysFirst = d.settingPlayers()
        if p1 == whoPlaysFirst :
            p1.symbol = "x"
            p2.symbol = "O"
        else :
            p1.symbol = "O"
            p2.symbol = "X"
        running = True 
        validInput = ["1","2","3","4","5","6","7","8","9"]
        currentPlayer = whoPlaysFirst
        playAgain = "-1"
    elif playAgain == "0" :
        running = False
    else :
        #setting the currentplayer
        if currentPlayer == p1:
            currentPlayer = p2
        else :
            currentPlayer = p1
    





