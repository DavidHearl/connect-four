import numpy as np

class ConnectFour:
    """
    Main class.
    """
    def __init__(self):
        self.board = np.zeros(shape= (7,6), dtype=str)
        self.winner = None
        self.to_play = None
    
    def printBoard(self):
        print("|",end="")
        for i in range(7):
            print("| "

game = ConnectFour()
game.printBoard()

















#print(   1   2   3   4   5   6   7)
#print("+---+---+---+---+---+---+---+")
#print("|   |   |   |   |   |   |   |")
#print("|   |   |   |   |   |   |   |")
#print("|   |   |   |   |   |   |   |")
#print("|   |   |   |   |   |   |   |")
#print("|   |   |   |   |   |   |   |")
#print("| X | O |   |   |   |   |   |")
#print("+---+---+---+---+---+---+---+")