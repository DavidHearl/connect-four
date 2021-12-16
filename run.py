"""Main file that runs imports class and runs core functions"""


from models.connect_four import ConnectFour


def main():
    """Runs all program functions"""
    game = ConnectFour()
    game.print_board()
    game.play_game()

print("\nWelcome to Connect 4 !")
print("Please select a column :")
main()
