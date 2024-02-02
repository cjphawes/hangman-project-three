![Hangman Game Title](/documentation-imgs/hangman_title.png)

## Hangman Havoc

**Hello Fellow Coders!**

Welcome to Hangman Havoc, a terminal based Python game. This game is my attempt at providing humorous version of an iconic game for pleasure.

It is aimed at all ages, for anyone who wants to have some fun, laugh and try to guess words correctly!

Try to not lose all your lives! [Hangman Havoc](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

![hangman havoc on a variety of screen widths](/documentation-imgs/game_on_various_screen_sizes.png)

Am I Responsive [Webpage](https://ui.dev/amiresponsive?url=https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

---

## How to play

1. Click this [link](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/) or copy and paste: `https://hangman-havoc-5a5a826a9d8e.herokuapp.com/` into your browser's address bar.
2. If the game loads, follow the instructions, if it doesn't load, click "**RUN PROGRAM**".
3. Understand the rules of the game before continuing.
4. Enter a username and start guessing!
5. Once you are tired of playing you can exit the game by telling the game you don't want to play again.

Link to the game: [https://hangman-havoc-5a5a826a9d8e.herokuapp.com/](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

---

## User Stories

#### First Time Visitor Goals

- As a first time visitor, I want to be able to navigate through the game without any problems.
- As a first time visitor, I want the game to be fun and enticing.
- As a first time visitor, I want to be able to understand the rules of how to play without any questions.

#### Frequent Visitor Goals

- As a frequent visitor, I want to be able to have a more visual depiction of my lives diminishing after an incorrect guess.
- As a frequent visitor, I would like to not have to read the rules every time I restart the game.
- As a frequent visitor, I want a difficulty level scale so I can choose whether I want to play for the hard or easy words.

---

## Features

#### Once the program has loaded

![Once program has loaded](/documentation-imgs/game_loaded.png)

- The user will see the game title.
- Provides introduction text to explain how the game works.
- Asks the user if they want to start game.

#### After entering the game

![After entering the game](/documentation-imgs/game_rules.png)

- The user will be met with the rules of the game explaining how it works and what to look out for.
- The user is asked for their username.

#### Upon entering a username

![After entering a username](/documentation-imgs/entered_a_username.png)

- The user is prompted to make a guess for the first word they are guessing.
- The first guess is always a mystery to the user so they do not know how many letters they need to guess until after the first guess.

#### After a correct guess

![After correctly guessing](/documentation-imgs/correct_guess.png)

- The user is given:
  - A small message to confirm they guessed correctly.
  - What letters they have used already.
  - The word they need to guess with the letters they have correctly guessed shown and the others blank.

#### After an incorrect guess

![After incorrectly guessing](/documentation-imgs/incorrect_guess.png)

- The user is given:
  - A small message to confirm they guessed incorrectly.
  - What letters they have used already.
  - The word they need to guess with the letters they have correctly guessed shown and the others blank.

#### If the user wins

![User wins](/documentation-imgs/user_wins.png)

- The user will be shown the full word they guessed correctly.
- A small message congratulating them on winning.
- Prompted as to whether they want restart the game or not.

#### If the user loses

![User lost](/documentation-imgs/user_lost.png)

- The user is given a small message confirming that they lost.
- They are given the word that they were trying to guess.
- Prompted as to whether they want to restart the game or not.

#### User restarts game

![User restarts the game](/documentation-imgs/restarts_game.png)

- Once the user inputs a "**Y**", they will receive a small funny message.
- The game will restart from the point of making the first mystery letter guess.

#### User wants to end the game

- The user is met with a confirmation question at the start of the game and the end of the game, re-asking if they are sure they want to stop playing.

##### If yes (start of game)

![User wants to end the game with a yes](/documentation-imgs/start_of_game_confirmation_yes.png)

- The user will be given a sad message and then thanked for playing the game.

##### If yes (end of game)

![User wants to end the game with a yes](/documentation-imgs/end_of_game_confirmation_yes.png)

- The user is given a sad, yet funny message and thanks them for playing.

##### If no (start of game)

![User wants to start the game with a yes](/documentation-imgs/start_of_game_confirmation_no.png)

- The user is given a motivating and funny message encouraging them to get the game started.

##### If no (end of game)

![User wants to end the game with a no](/documentation-imgs/end_of_game_confirmation_no.png)

- The user is given an excited message.
- Prompts the user once again if they would like to restart the game just in case it was a typo.

#### Invalid inputs

- There is a variety of user validation involved with each question and input asked for.

##### After an invalid guess

![After an invalid guess](/documentation-imgs/invalid_guess.png)

- The user is given:
  - A small message confirming two types of message:
    - An invalid character.
    - Using the same letter twice.
  - What letters they have already used.
  - The word they need to guess with the letters they have correctly guessed shown and the others blank.

##### After an invalid input

![After an invalid input](/documentation-imgs/invalid_input.png)

- The user is shown a witty comment and told what they need to be inputting.
- Prompted to answer the question again correctly.

---

## Logic process

![Flowchart of game logic](/documentation-imgs/flowchart_of_game_logic.png)

- This flowchart represents the logical flow of the game.

---

## Technologies used

- Python [3.9.18](https://www.python.org/downloads/release/python-3918/)

#### Modules/Packages used

##### Standard library imports

- [Random](https://docs.python.org/3/library/random.html) was used to randomize the selection of a word for the user to guess.
- [String](https://docs.python.org/3/library/string.html) was used to make all letters guessed shown as capital letters.

##### 3rd Party imports

- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the text.
- [Emoji](https://pypi.org/project/emoji/) was used for generating emojis to provide the humorous and life elements.

##### Local imports

- []()

##### Other tools

- [VSCode]() was used as the main IDE and tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the program.
- [Github](https://github.com/) was used to upload my code for collaboration purposes.
- [Heroku](https://dashboard.heroku.com/) was used for the deployment of the program.
- [Lucidchart](https://www.lucidchart.com/pages/) was used for the creation of my program logic flowchart for the README file.
- [ImageResizer](https://imageresizer.com/) was used to change from documentation images from png to webp.

---

## Bugs

## Reminders

- Your dependencies must be placed in the `requirements.txt` file
