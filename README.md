# Connect Four in Python

Connect four is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

https://dry-savannah-35963.herokuapp.com/

Users can compete against the computer to be the first to get four counters in a row. This can vertical, horizontal or diagonal.

## How to play

Connect Four is exactly the same as the traditional game. You can read more about it on https://en.wikipedia.org/wiki/Connect_Four.

In this version, the user has to choose an input between 0 and 6.

The user's counters are marked on the board as an 'X' and the computers counters marked as an 'O'.

The player and computer then take it in turns to place their counters.

The winner is determined when a user gets 4 counters in a line.

## Project Inception

At the start of the project I created a flow chart to set the structure for the code yet to be created and provide a guide to follow throughout the project.
![Connect Four Flow Chart](./assets/images/connect-four-flow-chart.jpg)

## Features

### Existing Features

- Accepts user input

![Enter Input](./assets/images/start-up.jpg)

- Player can play against the computer

![Show Computers Turn](./assets/images/user-enters-input.jpg)

- Input validation and error checking:
    - User cannot select a column outside the grid
    - User must enter an integer

![Error checking](./assets/images/incorrect-input.jpg)

- Displays message if the user wins

![Player wins](./assets/images/player-wins.jpg)

- Allows to user to play again

![Play again](./assets/images/play-again.jpg)

### Future Features

- Allow players to add their name
- Add minor delay to computers turn so both boards don't show up immediately
- Allow the user to choose between single player and two player mode
- Keep a running total of how many games each player has won
- Leverage deep learning to create an AI to play as the computer instead of a random move

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
- Numpy - https://numpy.org/