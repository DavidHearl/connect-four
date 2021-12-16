"""Contains function to configure and reset board"""


def configure_board(markers, board):
    """Configures board layout"""
    # Set the number of rows using the columns created below
    for row in range(6):
        # Sets the number of columns in the board
        for column in range(7):
            print("| " + markers[board[row, column]] + " ", end="")
        print("|")
