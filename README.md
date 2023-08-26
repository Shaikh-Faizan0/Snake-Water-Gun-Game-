Snake, Water, Gun Game Documentation
====================================

Introduction:
--------------
This Python script implements a simple game of "Snake, Water, Gun" where a user plays against the computer. The user and the computer each choose one of the three options: snake, water, or gun. The game is played for a fixed number of chances, and points are awarded based on the game's rules.

Usage:
-------
1. Run the script using a Python interpreter.
2. The user will be prompted to input their choice: 's' for snake, 'w' for water, or 'g' for gun.
3. The computer will randomly choose one of the options.
4. The game outcome is displayed, and points are awarded accordingly.
5. Repeat steps 2-4 until the total number of chances is exhausted.
6. At the end of the game, the winner is declared based on the points earned.

Rules:
-------
- Snake defeats Water
- Water defeats Gun
- Gun defeats Snake

Components:
------------
1. `computer`: A list containing the possible choices for the computer: ['s', 'w', 'g'].
2. `chances`: The total number of chances for the game (default: 10).
3. `no_of_chances`: Keeps track of the current chance number.
4. `computer_point`: Accumulates computer's points.
5. `human_point`: Accumulates user's points.

Execution:
----------
1. The game begins with an introduction and instructions on how to choose options.
2. Inside a loop, the user's input is read and compared with the computer's random choice.
3. Points are awarded based on the game rules.
4. The loop continues until all chances are exhausted.
5. At the end of the game, the winner or a tie is determined based on the points earned.

Functions and Logic:
---------------------
1. A while loop is used to execute the game logic until the total chances are used up.
2. The user's choice and the computer's random choice are compared using conditional statements.
3. Points are awarded to the user and the computer based on the game rules.
4. Remaining chances are displayed after each round.

Output:
-------
- Game messages are displayed to inform the user about the game progress, choices, and points.
- At the end of the game, the final result (win/lose/tie) is displayed along with the points earned.

Improvements and Notes:
------------------------
- The code has been organized for clarity, but further improvements such as using functions can enhance readability.
- Input validation could be added to ensure the user only inputs 's', 'w', or 'g'.

Usage Example:
---------------
1. User input: 's'
2. Computer input: 'w'
3. Output: "Your guess s and computer's guess w\nHuman wins 1 point."

Author:
-------
This code was authored by [Your Name]. It is intended for educational and illustrative purposes.
