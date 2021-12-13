"""
Test
"""


def configure_board(markers, board):
    """ Configures board layout """
    for row in range(6):
        for column in range(7):
            print("| " + markers[board[row, column]] + " ", end="")
        print("|")
