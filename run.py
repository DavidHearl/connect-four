# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Board:
    """
    Main board class. Creates fresh board for the game to be played on.
    """
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    def create_board(self):
        print("+---+---+---+---+---+---+---+")
        print("|   |   |   |   |   |   |   |")
        print("|   |   |   |   |   |   |   |")
        print("|   |   |   |   |   |   |   |")
        print("|   |   |   |   |   |   |   |")
        print("|   |   |   |   |   |   |   |")
        print("|   |   |   |   |   |   |   |")
        print("+---+---+---+---+---+---+---+")
        

size = Board(7, 6)
print(size.columns)
print(size.create_board())