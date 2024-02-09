![Hangman Game Title](/documentation/doc-imgs/hangman_title.webp)

## Hangman Havoc

**Hello Fellow Coders!**

Welcome to Hangman Havoc, a terminal based Python game. This game is my attempt at providing humorous version of an iconic game for pleasure.

It is aimed at all ages, for anyone who wants to have some fun, laugh and try to guess words correctly!

Try to not lose all your lives! [Hangman Havoc](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

![hangman havoc on a variety of screen widths](/documentation/doc-imgs/game_on_various_screen_sizes.webp)

Am I Responsive [Webpage](https://ui.dev/amiresponsive?url=https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

---

## How to play

1. Click this [link](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/) or copy and paste: `https://hangman-havoc-5a5a826a9d8e.herokuapp.com/` into your browser's address bar.
2. If the game loads, follow the instructions, if it doesn't load, click "**RUN PROGRAM**".
3. Understand the rules, after entering the game.
4. Enter a username and start guessing!
5. Once you are tired of playing you can exit the game by inputting "**N**", when asked if you want to play the game.

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

![Once program has loaded](/documentation/doc-imgs/game_loaded.webp)

- The user will see the game title.
- Provides introduction text to explain how the game works.
- Asks the user if they want to start game.

#### After entering the game

![After entering the game](/documentation/doc-imgs/game_rules.webp)

- The user will be met with the rules of the game explaining how it works and what to look out for.
- The user is asked for their username.

#### Upon entering a username

![After entering a username](/documentation/doc-imgs/entered_a_username.webp)

- The user is prompted to make a guess for the first word they are guessing.
- The first guess is always a mystery to the user so they do not know how many letters they need to guess until after the first guess.

#### After a correct guess

![After correctly guessing](/documentation/doc-imgs/correct_guess.webp)

The user is given:

- A small message to confirm they guessed correctly.
- What letters they have used already.
- The word they need to guess with the letters they have correctly guessed shown and the others blank.

#### After an incorrect guess

![After incorrectly guessing](/documentation/doc-imgs/incorrect_guess.webp)

- The user is given:
  - A small message to confirm they guessed incorrectly.
  - What letters they have used already.
  - The word they need to guess with the letters they have correctly guessed shown and the others blank.

#### If the user wins

![User wins](/documentation/doc-imgs/user_wins.webp)

- The user will be shown the full word they guessed correctly.
- A small message congratulating them on winning.
- Prompted as to whether they want restart the game or not.

#### If the user loses

![User lost](/documentation/doc-imgs/user_lost.webp)

- The user is given a small message confirming that they lost.
- They are given the word that they were trying to guess.
- Prompted as to whether they want to restart the game or not.

#### User restarts game

![User restarts the game](/documentation/doc-imgs/restarts_game.webp)

- Once the user inputs a "**Y**", they will receive a small funny message.
- The game will restart from the point of making the first mystery letter guess.

#### User wants to quit the game

The user is met with a confirmation question at the start of the game and the end of the game, re-asking if they are sure they want to stop playing.

##### If yes (at the start of the game)

![User wants to end the game with a yes](/documentation/doc-imgs/start_of_game_confirmation_yes.webp)

The user will be given a sad message and then thanked for playing the game.

##### If yes (at the end of the game)

![User wants to end the game with a yes](/documentation/doc-imgs/end_of_game_confirmation_yes.webp)

The user is given a sad, yet funny message and thanks them for playing.

##### If no (at the start of the game)

![User wants to start the game with a yes](/documentation/doc-imgs/start_of_game_confirmation_no.webp)

The user is given a motivating and funny message encouraging them to get the game started.

##### If no (at the end of the game)

![User wants to end the game with a no](/documentation/doc-imgs/end_of_game_confirmation_no.webp)

- The user is given an excited message.
- Prompts the user once again if they would like to restart the game just in case it was a typo.

#### Invalid inputs

There is a variety of user validation involved with each question and input asked for.

##### After an invalid guess

![After an invalid guess](/documentation/doc-imgs/invalid_guess.webp)

The user is given:

- A small message confirming two types of message:
  - An invalid character.
  - Using the same letter twice.
- What letters they have already used.
- The word they need to guess with the letters they have correctly guessed shown and the others blank.

##### After an invalid input

![After an invalid input](/documentation/doc-imgs/invalid_input.webp)

- The user is shown a witty comment and told what they need to be inputting.
- Prompted to answer the question again correctly.

## Future features to implement

- A simple menu rather than an input method of choosing what to select by letter, to make it more easy to navigate.
- Allow users to have a multiple space usernames.

---

## Logic process

![Flowchart of game logic](/documentation/doc-imgs/flowchart_of_game_logic.webp)

- This flowchart represents the logical flow of the game.

---

## Technologies used

- Python [3.9.18](https://www.python.org/downloads/release/python-3918/)

#### Modules/Packages used

##### Standard library imports

- [Random](https://docs.python.org/3/library/random.html) was used to randomize the selection of a word for the user to guess.
- [String](https://docs.python.org/3/library/string.html) was used to make all letters guessed shown as capital letters.
- [Sys](https://docs.python.org/3/library/sys.html) was used for the exiting function of the program.

##### 3rd party imports

- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the text.
- [Emoji](https://pypi.org/project/emoji/) was used for generating emojis to provide the humorous and life elements.

##### Other tools

- [VSCode](https://code.visualstudio.com/) was used as the main IDE and tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the program.
- [Github](https://github.com/) was used to upload my code for collaboration purposes.
- [Heroku](https://dashboard.heroku.com/) was used for the deployment of the program.
- [Lucidchart](https://www.lucidchart.com/pages/) was used for the creation of my program logic flowchart for the README file.
- [Imageresizer](https://imageresizer.com/) was used to change from documentation images from png to webp.

---

## Testing

Please refer to the [TESTING.md](/TESTING.md) for all test-related documentation.

#### Solved bugs

- **Issue 1**: The word generated for the user to guess was including 3 letter words when I only want 4 letter or more words to guess.

  - _Solution_: I added `or len(new_word) < 4`to my while loop for iterating through the list of words variable.

    ```python
    while any(char in new_word for char in ("-", " ")) or len(new_word) < 4:
       new_word = random.choice(list_of_words)
    return new_word.upper()
    ```

- **Issue 2**: My secondary confirmation questions were not going to the correct function once chosen an input, causing an infinite loop.

  - _Solution_: To get out of the loop I added `break` on the inner loops to break out back to the outer loop.

- **Issue 3**: When entering a username, if you added a space before you typed your username, it would not capitalize the first letter as designed.
  - _Solution_: A quick fix was to simply swap around my `strip()` and `capitalize()` methods so it would always strip away the spaces first before then capitalizing the username's first letter.

#### Unsolved Bugs

None.

#### Mistakes

There were four mistakes made while committing to Github.

- **ae9195d** - "feat:adjusted formatting to conform to PEP8 standards"
  _**Supposed to be**_: "feat:adjust formatting to conform to PEP8 standards"

- **336d117** - "maint: add dependencies go my requirements.txt file"
  _**Supposed to be**_: "maint: add dependencies to my requirements.txt file"

- **1352315** - "remove parameters from functions and try/except statement"
  _**Supposed to be**_: "feat:remove parameters from functions and try/except statement"

- **ee40f58** - "add multiple 'g' just to see if app has updated"
  _**Supposed to be**_: "feat:add multiple 'g' just to see if app has updated"

---

## Deployment

- The program was deployed using [Heroku](https://dashboard.heroku.com/)
- The program can be reached by this [link](https://hangman-havoc-5a5a826a9d8e.herokuapp.com/)

### Deploy program as a local application

_Notes_:

1. This project requires you to have **Python** installed on your local device. If you have not installed it already please follow [Python download](https://www.python.org/downloads/).
2. This project will also need **PIP** installed to allow the
   installation of modules the application uses (PIP is usually installed within your Python installation, if not, follow [PIP installation](https://pip.pypa.io/en/stable/installation/) on how to set it up).

Create a local copy of the Github repository by following one of the two processes below:

1. Download ZIP file:

   - Go to the [Hangman Havoc Github repository](https://github.com/cjphawes/hangman-project-three).
   - Click on the green **Code** button and download the ZIP file containing the project.
   - Extract the ZIP file to a location of your choice on your device.

2. Clone the repository:
   1. Open a folder on your computer using the **Command Prompt** on Windows, **Terminal** on Mac or the respective on your device.
   2. Run the following command:
      - `git clone https://github.com/cjphawes/hangman-project-three.git`

**OR**

Alternatively, if using Gitpod, click below to create your own workspace using this repository.

[![Open in Gitpod](/documentation/doc-imgs/gitpod_img.svg)](https://gitpod.io/new#https://github.com/cjphawes/hangman-project-three)

- Install Python module dependencies:
  - Run the command:
    - `pip freeze > requirements.txt`
  - Create a `.venv` virtual environment, delete and create a new one.
  - Add the requirements.txt, by selecting it from the dropdown menu. This will hold all your dependencies needed to run the program.
- To access the program, run the command:
  - `python run.py`

### Deploy as a remote web application

1. Clone the repository

   1. Open a folder on your computer using the **Command Prompt** on Windows, **Terminal** on Mac or the respective on your device.
   2. Run the following command:
      - `git clone https://github.com/cjphawes/hangman-project-three.git`

2. Create your own Github repository to host the code.
3. To set the remote repository location to your repository, run the command:

   - `git remote set-url origin <YOUR GITHUB REPO PATH>`

4. _Push_ the files to your repository to host the code, running the command:
   - `git push`
5. Create a Heroku account, if you haven't already, click [Heroku sign-up](https://signup.heroku.com/).
6. Create a new application, from selecting **Create new app** from the dropdown. Follow the steps on the page and click **Create app**.

https://github.com/cjphawes/hangman-project-three/assets/105741584/563b5011-fb62-4d0a-9de5-d0fd3013de92

8. Navigate to the **Deploy** tab, opening up the Deploy section.
   ![Deploy tab navigation](/documentation/doc-imgs/deploy_tab_nav_heroku.webp)
9. Link your Github account and connect the application to the repository you just created.
   ![Linking Github account](/documentation/doc-imgs/connect_to_github_heroku.webp)
10. Navigate to the **Settings** tab, opening up the Settings section.
    ![Settings tab navigation](/documentation/doc-imgs/settings_tab_nav_heroku.webp)
11. Click **Add Buildpack**.
    ![Add buildpack button](/documentation/doc-imgs/add_buildpacks_heroku.webp)
12. Add the **Python** and **Node.js** buildpacks in the following order.
    ![Buildpacks](/documentation/doc-imgs/buildpacks_heroku.webp)
13. Click **Reveal Configs**.
    ![Reveal config var button](/documentation/doc-imgs/reveal_configs_button_heroku.webp)
14. Add **1** Config Var, provided by [Code Institute](https://codeinstitute.net/global/):
    - **KEY**: PORT
    - **VALUE**: 8000

![Config var example](/documentation/doc-imgs/config_var_heroku.webp)

15. Return back to the **Deploy** tab, opening up the Deploy section.
    ![Deploy tab navigation](/documentation/doc-imgs/deploy_tab_nav_heroku.webp)
16. At the bottom of the page, click **Deploy** Branch.
    ![Deploying branch](/documentation/doc-imgs/deploy_branch.webp)
17. Wait while Heroku is deploying your application
    ![Waiting for Heroku to deploy app](/documentation/doc-imgs/waiting_for_deployment.webp)
18. Once complete, click **View** to open the program in the web browser.
    ![View app button](/documentation/doc-imgs/view_app_button.webp)

---

## Credits

#### Content

- I used Matthew Hsu [Github repo](https://github.com/mahsu/IndexingExercise/blob/master/5000-words.txt) for gathering the words to use.
- [Chat GPT](https://chat.openai.com/) reformatted all the words in my `rules.py` file to follow PEP8 standards with the character line limit.
- [iEmoji.com](https://www.iemoji.com/view/emoji/40/symbols/) and [HTML Symbols](https://www.htmlsymbols.xyz/unicode/) is where I found the code for each emoji's used.
- The title of Hangman Havoc used [ASCII ](https://ascii.co.uk/text) text.
- I used the [ANSI Escape Sequence](https://blog.finxter.com/how-to-print-bold-text-in-python/) method for making words/numbers bold.
- I used the [Colorama](https://blog.finxter.com/how-to-print-bold-text-in-python/) package for the coloring of text, using [Replit](https://replit.com/talk/ask/How-do-you-change-text-colors-and-fonts-in-python/122041) for the different colors.

#### Media

- I used [Imageresizer](https://imageresizer.com/) for all the README.md & TESTING.md file images.
- I used [Screen Capture](https://www.screencapture.com/) for the recording for the TESTING.md file.
- I used [Chrome Capture Extension](https://chromewebstore.google.com/detail/chrome-capture-gif-screen/ggaabchcecdbomdcnbahdfddfikjmphe) for all of the documentation images in the TESTING.md & README.md files.

## Reminders

- Your dependencies must be placed in the `requirements.txt` file
