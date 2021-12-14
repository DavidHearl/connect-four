# Connect Four in Python

Connect four is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can compete against to computer to be the first to get four counters in a row. This can vertical, horizontal or diagonal.

## How to play

Connect Four is exactly the same as the traditional game. You can read more about it on https://en.wikipedia.org/wiki/Connect_Four.

In this version, the user has to choose an input between 0 and 6.

The user's counters are marked on the board as an 'X' and the computers counters marked as an 'O'.

The player and computer then take it in turns to place their counters.

The winner is determined when a user gets 4 counters in a line.

## Features

### Existing Features

- Player can play against the computer
- Accepts user input
- Input validation and error checking:
    - User cannot select a column outside the grid
    - User must enter an integer
- Displays message if the user wins
- Allows to user to play again

### Future Features

- Allow players to add their name
- Add minor delay to computers turn so both boards don't show up immediately
- Allow the user to choose between single player and two player mode
- Keep a running total of how many games each player has won
- Leverage deep learning to create an AI to play as the computer instead of a random move

## Data Model

## Testing

Initial testing was completed by myself, this was achieved through the following methods:

- Passed the Code through the PEP8 linters and confirmed there were no issues
- Used the error terminal in GitPod which used the flake8 linter
- Gave invalid inputs to try and break the game:
    - Inputted strings when integers were required
    - Tried to input a counter in a full column
- Tested in the local terminal in GitPod
- Tested in the Code Institute Heroku terminal

The finished project was tested by two users.

- Neither user discovered any bugs and the project appears to be working correctly

## Bugs

- No bugs remaining

## Validator Testing

- PEP8 

    - No errors were returned from PEP8online.com

## Deployment

This project was deployed using the Code Institute terminal for Heroku.

Following steps for deployment:

- Clone this repository
- Create a new application on Heroku
- Set the buildbacks to Python and then NodeJS, following that order
- Create a link between the Heroku application and the repository
- Click **Deploy**

## Credits

- Wikipedia for details on how to play connect four
- Code Institute for the deployment terminal