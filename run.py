import numpy as np

class ConnectFour:
    """
    Main class.
    """
    def __init__(self):
        self.board = np.zeros(shape= (6,7), dtype=str)
        self.winner = None
        self.to_play = None
    
    def printBoard(self):
        print("+---+---+---+---+---+---+---+")
        for r in range(6):
            for column in range(7):
                print(self.board[0,column] + "|   ", end="")
            print("|")
        print("+---+---+---+---+---+---+---+")
        print("  1   2   3   4   5   6   7  ")

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