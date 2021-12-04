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

    def move(self, column):
        # Write Checks for winner, check if they have pick 0-6, check is column is full.
        selectedColumn = self.board[:,column]
        filled = True
        height = 5
        while filled:
            if self.board[height, column] == 0:
                filled = False
                break
            height -= 1

        self.board[height, column] = self.to_play

        if self.to_play == 1:
            self.to_play = 2
        else:
            self.to_play = 1

    def playGame(self):
        print("Welcome to connect 4")
        print("You are X")
        self.to_play = 1
        for _ in range(8):
            if self.to_play == 1:
                self.move(int(input("Enter Column: ")))
            else:
                self.move(np.random.randint(7))

            print(self.checkFour(self.board[:,0]))
            print(self.board[:,0])
            self.printBoard()

    def checkFour(self, values):
        current = values[0]
        count = 0
        for i in range(len(values)):
            if values[i] == 0:
                current = values[i]
                count = 1
                pass

            if values[i] == current:
                count += 1
            else:
                current = values[i]
                count = 1
            
            if count == 4:
                return current
            

game = ConnectFour()
game.printBoard()
game.playGame()
print(game.checkFour([0,1,1,1,1,0]))

"""
Currently have function to check for 4 in a row in an array

Must write functions to:
    - Check columns for wins
    - Checks rows for wins
    - Check diagonals for wins
    - Function to wrap above functions

    - Include winCheck in move function
    - Adapt play function to create win message
    - error checkers

    - Maybe make computer less stupid

"""