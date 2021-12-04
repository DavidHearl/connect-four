import numpy as np

class ConnectFour:
    """
    Main class.
    """
    def __init__(self):
        self.board = np.zeros(shape= (6,7), dtype=int)
        self.winner = None
        self.to_play = None
    
    def printBoard(self):
        markers = [" ", "X", "O"]
        print("+---+---+---+---+---+---+---+")
        for row in range(6):
            for column in range(7):
                print("| " + markers[self.board[row,column]] + " ", end="")
            print("|")
        print("+---+---+---+---+---+---+---+")
        print("  0   1   2   3   4   5   6  ")


game = ConnectFour()
game.board[0,1] = 1
game.board[1,0] = 1
print(game.board)
game.printBoard()