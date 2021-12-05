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
        """
        Assigns values to markers and creates board
        """
        markers = [" ", "X", "O"]
        print("+---+---+---+---+---+---+---+")
        for row in range(6):
            for column in range(7):
                print("| " + markers[self.board[row,column]] + " ", end="")
            print("|")
        print("+---+---+---+---+---+---+---+")
        print("  0   1   2   3   4   5   6  ")

    def move(self, column):
        """

        """
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
        """
        Sets player as 1 then gets PC to select a random point between 0 and 6
        """
        self.to_play = 1
        for _ in range(16):
            if self.to_play == 1:
                self.move(int(input("Enter Column: ")))
            else:
                self.move(0)
                self.move(1)
                self.move(2)
                #self.move(np.random.randint(7))
                
            print(self.board[:,0])
            print(self.checkWinner())
            print(self.board.diagonal(), print(self.board.diagonal(1))),
            self.printBoard()

    def checkFour(self, values):
        """
        Checks to see if there are 4 values in a row, 
        ignoring 0 as it is an empty space.
        """
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

    def checkWinner(self):
        """
        Checks for columns and rows for a win
        """
        for column in range(6):
            values = self.board[:,column]
            result = self.checkFour(values)
        
            if result:
                return result

        for row in range(6):
            values = self.board[row,:]
            result = self.checkFour(values)
        
            if result:
                return result

        # There is no point checking the diagonals that are less the 4
        for diag in range(-3, 4):
            values = self.board.diagonal(diag)
            result = self.checkFour(values)

            if result:
                return result

        for diagReverse in range(-3, 4):
            values = np.fliplr(self.board).diagonal(diagReverse)
            result = self.checkFour(values)

            if result:
                return result        

#def main():
    #game = ConnectFour()
    #game.printBoard()
    #game.playGame()

print("Welcome to connect four, to play please enter the column you would like to play in")
#main()

game = ConnectFour()
np.fill_diagonal(game.board,val=2)
game.printBoard()
print(game.checkWinner())
game.board = np.fliplr(game.board)
print(game.board)
print(game.checkWinner())

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
    - Change play game to while loop based on game finish/win

    - Maybe make computer less stupid

"""