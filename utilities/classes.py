import time 
import random

class Player:
        
    def __init__(self,name):
        """"
        args :
            name (str)
            symbol (str) : "X" or "O"
            cells (list) : contains the cells filled by the player
        """
        self.name = name
        self.symbol = None
        self.cells = []
    
    def __equal__(self,player):
        if self.name == player.name :
            return True 
        return False
    
    def addCell(self,cell) :
        """
        args:
            cell (str) : the cell filled by the player
        """
        self.cells.append(cell)
    
    def test(self):
        """tests if the cells list contaains one of the winning combos 

        retruns :
            boolean :
        """
        winCombos = [["1","5","9"],
            ["2","5","8"],
            ["3","5","7"],
            ["4","5","6"],
            ["1","4","7"],
            ["3","6","9"]
            ]
        if (len(self.cells)>=3):
            for winCombo in winCombos :
                if all(item in self.cells for item in winCombo):
                    return True
        return False  



class DisplayManager :
    "takes care of all displays during the game"

    def welcomeMessage(self):
        print("""
welcome to our beloved tic tac toe game!!!
      we hope that you like it
        """)
    
    def settingPlayers(self):
        """
        returns: 
            p1 (Player)
            p2 (Player)
            whoPlaysFirst (Player)
        """
        name1 = input("player 1 please enter your name :  ")
        p1 = Player(name1)
        name2 = input("player 2 please enter your name :  ")
        p2 = Player(name2)
        print("ROCKS! PAPERS! SCISSORS! ...")
        whoPlaysFirst = random.choice([p1,p2])
        time.sleep(2)
        print(f"{whoPlaysFirst.name} will start")
        return p1,p2, whoPlaysFirst 

    def roundHandling(self,currentPlayer,otherPlayer,validInput):
        """
        args: 
            currentPlayer (Player)
            otherPlayer (Player): player waiting for his turn
            validInput (list) : list of the remaining cells
        
        Raises: 
            valueError if the value entered by the player doesn't exit in the validInput list 
        """
        Error = True 
        while (Error):
            move = input(f"{currentPlayer.name} please enter your move (1-9)  ")
            try :
                if move not in validInput :
                    raise ValueError
                else :
                    Error = False
                    validInput.remove(move)
                    currentPlayer.addCell(move)
                    for i in range(1,10):                                          
                        if str(i) in currentPlayer.cells :
                            print(f"| {currentPlayer.symbol} ",end="")
                        elif str(i) in otherPlayer.cells :
                            print(f"| {otherPlayer.symbol} ",end="")
                        else: 
                            print("| . ",end="")
                        if i %3 == 0:
                            print("\n-------------")
                    print("\n")
            except ValueError: 
                print("invalid input\n")


    
       