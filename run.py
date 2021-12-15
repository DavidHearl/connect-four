"""Import numpy to for board and transpositioning"""


from models.connect_four import ConnectFour


def main():
    """Runs all program functions"""
    game = ConnectFour()
    game.print_board()
    game.play_game()

print("\nWelcome to Connect 4 !")
print("Please select a column :")
main()
