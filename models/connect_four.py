"""
Contains connect four class that sets up the board,
checks input errors and checks for a win.
"""


# Import numpy for use in the board creation
# and for checking a diagonal array
import numpy as np
from utilities import configure_board


class ConnectFour:
    """
    Main class - contains the functions that: prints
    the board, places counters, checks for user errors
    and checks for a player win.
    """
    def __init__(self):
        """Defines the board and creates markers"""
        # Got zeros from numpy to create an array of arrays
        # https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
        self.board = np.zeros(shape=(6, 7), dtype=int)
        # Sets winner and counter to be played as none
        self.winner = None
        self.to_play = None
        # Defines markers to index to later
        self.markers = [" ", "X", "O"]

    def print_board(self):
        """Prints a blank board"""
        print("+---+---+---+---+---+---+---+")
        # Creates an array of 0s that are used for the markers above
        configure_board(self.markers, self.board)
        print("+---+---+---+---+---+---+---+")
        print("  0   1   2   3   4   5   6  ")

    def move(self, column):
        """
        Contains movement behavior and the correct counter to use each turn
        """
        # Checks if a column is filled
        filled = True
        height = 5
        # Steps through height till it reaches the lowest position for a marker
        while filled:
            if self.board[height, column] == 0:
                filled = False
                break
            height -= 1

        self.board[height, column] = self.to_play

        # after playing move, change the to_play
        # variable to the other player
        if self.to_play == 1:
            self.to_play = 2
        else:
            self.to_play = 1

    def play_game(self):
        """
        Checks if the user has entered the correcy input,
        generates the computers move and displays a message if
        a user has won
        """
        # Sets the first marker to use as "X"
        self.to_play = 1
        # Sets win status and previous input to
        # none as it is the start of the game
        win = None
        prev_input = None
        # checks if the user has entered the wrong input
        # or if the column is already full, will loop
        # until the user gives the correct input
        while win is None:
            if self.to_play == 1:
                incorrect_format = True
                while incorrect_format:
                    user_input = input("Enter Column: ")
                    try:
                        user_input = int(user_input)
                    except ValueError:
                        print("You have not entered an integer")
                    if user_input not in range(7):
                        print("Number is not between 0 and 6")
                    elif user_input not in self.possible_moves():
                        print("This column is already full")
                    else:
                        incorrect_format = False
                self.move(user_input)
                prev_input = user_input
            else:
                # sets the moves the computer would like to play
                # in this case (user input -1, +0, +1)
                desirable_moves = [prev_input - 1, prev_input, prev_input + 1]
                possible_moves = []
                # checks to see if there are any possible moves
                # that are the same as desirable moves
                for col in desirable_moves:
                    if col in self.possible_moves():
                        possible_moves.append(col)

                # if there is a possible and desirable move choose one randomly
                if len(possible_moves) == 0:
                    self.move(np.random.choice(self.possible_moves()))
                # if there are no possible and desirable moves
                # choose a possible move
                else:
                    self.move(np.random.choice(possible_moves))

            # update the marker position on the board
            self.print_board()
            # check to see if a player has won
            win = self.check_winner()

        # if a player has won display a win message
        print(f"Player {self.markers[win]} has won the game")
        # ask the user if they would like to play again
        play_again = input("Would you like to play again Y/N: ")
        # convert the users input into a lower case
        play_again = play_again.lower()

        # if the presses "y" the game starts again
        if play_again == "y":
            self.board = np.zeros(shape=(6, 7), dtype=int)
            self.print_board()
            return self.play_game()

    def check_four(self, values):
        """Checks to see if there are four in a row"""
        # creates a count for how many markers are in a row
        # current is the marker that we are currently looking at
        current = values[0]
        count = 0
        # don't count 0s (empty spaces) and stop count going above 1
        for i in range(len(values)):
            if values[i] == 0:
                current = values[i]
                count = 1
            
            # if next value is the same as current add one to count
            if values[i] == current:
                count += 1
            # if next value is not same as curretn, change current to
            # value of next marker and reset count
            else:
                current = values[i]
                count = 1

            if count == 4:
                return current

    def check_winner(self):
        """Checks for a winner in any of the possible configurations"""
        # checks for a win in rows
        for column in range(6):
            values = self.board[:, column]
            result = self.check_four(values)

            if result:
                return result

        # checks for a win in columns
        for row in range(6):
            values = self.board[row, :]
            result = self.check_four(values)

            if result:
                return result

        # checks for any for a win in the diagonals
        # we dont need to check the corners of the grid as there are not
        # enough spaces in the corner to reach 4 in a row
        for diag in range(-3, 4):
            values = self.board.diagonal(diag)
            result = self.check_four(values)

            if result:
                return result

        for diag_reverse in range(-3, 4):
            # Used numpy diagonal to search for
            # an array containing 4 diagonal numbers
            # https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
            values = np.fliplr(self.board).diagonal(diag_reverse)
            result = self.check_four(values)

            if result:
                return result

        if 0 not in self.board:
            return 0

    def possible_moves(self):
        """Returns moves that can still be played"""
        options = []
        # check if the top column is empty
        # if so then there is a possible move
        for col in range(7):
            values = self.board[:, col]
            if values[0] == 0:
                options.append(col)
        return options
