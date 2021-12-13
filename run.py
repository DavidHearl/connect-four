"""
Import numpy to for board and transpositioning
"""


import numpy as np
from utilities import configure_board


class ConnectFour:
    """
    Main class, contains the play_game function,
    move and validation functions
    """
    def __init__(self):
        """
        Defines the board using numpy.
        Sets 'winner' and 'to_play' as none/false.
        Creates the markers that will be used to replace 0, 1 and 2
        """
        self.board = np.zeros(shape=(6, 7), dtype=int)
        self.winner = None
        self.to_play = None
        self.markers = [" ", "X", "O"]

    def print_board(self):
        """
        Creates the opening and close of the connect four table.
        Creates the inner grid of rows and columns
        """
        print("+---+---+---+---+---+---+---+")
        configure_board(self.markers, self.board)
        print("+---+---+---+---+---+---+---+")
        print("  0   1   2   3   4   5   6  ")

    def move(self, column):
        """
        Places the counter at the bottom of the grid
        the grid starts at 0,0 so it needs to count backwards
        Sets the next turn as either X or O (1 or 2)
        """
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

    def play_game(self):
        """
        Sets the user to X and winner to none
        Checks the user is using the correct formatting (int)
        Generates a random move for the computer
        Tells the user who has won and asks if they would like to play again
        """
        self.to_play = 1
        win = None
        prev_input = None
        while win is None:
            if self.to_play == 1:
                incorrect_format = True
                while incorrect_format:
                    user_input = input("Enter Column: ")
                    try:
                        int(user_input)
                    except ValueError:
                        print("You have not entered an integer")
                    else:
                        user_input = int(user_input)
                    if user_input not in range(7):
                        print("Number is not between 0 and 6")
                    elif user_input not in self.possible_moves():
                        print("This column is already full")
                    else:
                        incorrect_format = False
                self.move(user_input)
                prev_input = user_input
            else:
                desirable_moves = [prev_input - 1, prev_input, prev_input + 1]
                possible_moves = []
                for col in desirable_moves:
                    if col in self.possible_moves():
                        possible_moves.append(col)

                if len(possible_moves) == 0:
                    self.move(np.random.choice(self.possible_moves()))
                else:
                    self.move(np.random.choice(possible_moves))

            self.print_board()
            win = self.check_winner()

        print(f"Player {self.markers[win]} has won the game")
        play_again = input("Would you like to play again Y/N: ")
        play_again = play_again.lower()

        if play_again == "y":
            # Run file again if user types "Y"
            self.board = np.zeros(shape=(6, 7), dtype=int)
            return self.play_game()

    def check_four(self, values):
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

            if values[i] == current:
                count += 1
            else:
                current = values[i]
                count = 1

            if count == 4:
                return current

    def check_winner(self):
        """
        Checks columns for win
        Checks rows for win
        Check left and right diagonal for wins
        """
        for column in range(6):
            values = self.board[:, column]
            result = self.check_four(values)

            if result:
                return result

        for row in range(6):
            values = self.board[row, :]
            result = self.check_four(values)

            if result:
                return result

        # We dont need to check the corners of the grid as there are not
        # enough spaces in the corner to reach 4 in a row
        for diag in range(-3, 4):
            values = self.board.diagonal(diag)
            result = self.check_four(values)

            if result:
                return result

        for diag_reverse in range(-3, 4):
            values = np.fliplr(self.board).diagonal(diag_reverse)
            result = self.check_four(values)

            if result:
                return result

        if 0 not in self.board:
            return 0

    def possible_moves(self):
        """
        Returns moves that can still be played
        """
        options = []
        for col in range(7):
            values = self.board[:, col]
            if values[0] == 0:
                options.append(col)
        return options


def main():
    """
    Runs all program functions
    """
    game = ConnectFour()
    game.print_board()
    game.play_game()


print("\nWelcome to Connect 4 !")
print("Please select a column :")
main()

# To Do List

# Write comments to explain code
# Write read me file
# Deploy Project
