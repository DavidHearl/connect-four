import numpy as np

class ConnectFour:
    """
    Main class.
    """
    def __init__(self):
        self.board = np.zeros(shape= (6,7), dtype=int)
        self.winner = None
        self.to_play = None
        self.markers = [" ", "X", "O"]
    
    def printBoard(self):
        """
        Assigns values to markers and creates board
        """
        print("+---+---+---+---+---+---+---+")
        for row in range(6):
            for column in range(7):
                print("| " + self.markers[self.board[row,column]] + " ", end="")
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
        win = None
        while not win:
            if self.to_play == 1:
                incorrectFormat = True
                while incorrectFormat:
                    userInput = input("Enter Column: ")
                    try:
                        int(userInput)
                    except:
                        print("You have not entered an integer")
                        pass
                    else:
                        userInput = int(userInput)
                    #if type(userInput) != int:
                    #    print("You have not selected a column")
                    #    pass
                    if userInput not in range(7):
                        print("Number is not between 0 and 6")
                        pass
                    else:
                        incorrectFormat = False
                self.move(userInput)
            else:
                self.move(np.random.randint(7))

            self.printBoard()
            win = self.checkWinner()
        print(f"Player {self.markers[win]} has won the game")
        playAgain = input("Would you like to play again Y/N: ")
        playAgain = playAgain.lower()
        if playAgain == "y":
            # Run file again if user types "Y"
            exec(open('run.py').read())

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

def main():
    """
    Runs all program functions
    """
    game = ConnectFour()
    game.printBoard()
    game.playGame()

print("Welcome to connect four, to play please enter the column you would like to play in")
main()

"""
Must write functions to:
    - Check columns arn't full (for user and computer)
    - Maybe make computer less stupid
"""