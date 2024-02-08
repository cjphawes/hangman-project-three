Click [README.md](/README.md) to return back.

---

## Testing

The program was tested constantly throughout the development process. I had multiple users try out my game to spot bugs or grammatical mistakes which they found and I corrected.

## Validation

I used the [Code Institute Python Linter](https://pep8ci.herokuapp.com/#) to ensure sure the source code throughout was [PEP8](https://legacy.python.org/dev/peps/pep-0008/) compliant.

No errors were found in all .py files.

- run.py

![CI Linter PEP8 test for run.py](/documentation/doc-imgs/ci_linter_validation_run.py.webp)

- rules.py

![CI Linter PEP8 test for rules.py](/documentation/doc-imgs/ci_linter_validation_rules.py.webp)

- words.py

![CI Linter PEP8 test for words.py](/documentation/doc-imgs/ci_linter_validation_words.py.webp)

- number_styling.py

![CI Linter PEP8 test for number_styling.py](/documentation/doc-imgs/ci_linter_validation_number_styling.py.webp)

- emoji_dict.py

![CI Linter PEP8 test for emoji_dict.py](/documentation/doc-imgs/ci_linter_validation_emoji_dict.py.webp)

### Issues with validating code

In Github, the final line of whitespace is removed in all my files, here is evidence at the bottom of my code displaying the last line for validation purposes.

- run.py
  ![run.py last line evidence](/documentation/doc-imgs/run.py_validation_evidence.webp)

- rules.py
  ![rules.py last line evidence](/documentation/doc-imgs/rules.py_validation_evidence.webp)

- number_styling.py
  ![number_styling.py last line evidence](/documentation/doc-imgs/number_styling.py_validation_evidence.webp)

- emoji_dict.py
  ![emoji_dict.py last line evidence](/documentation/doc-imgs/emoji_dict.py_validation_evidence.webp)

- words.py
  ![words.py last line evidence](/documentation/doc-imgs/words.py_validation_evidence.webp)

---

## Manual Testing

| Action                                                 | Testing                                                  | Result                                                                                                                                                                                                       | Evidence              |
| ------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| Input "**Y**" to start the game                        | Inputs "**Y**"                                           | The game started by displaying the rules.                                                                                                                                                                    | **Insert Video here** |
| Input "**N**" to end the game                          | Inputs "**N**"                                           | A confirmation question is displayed.                                                                                                                                                                        | **Insert Video here** |
| Inputs "**Y**" or "**N**" to the confirmation question | Input "**Y**" or "**N**"                                 | "**Y**" - A goodbye message is displayed. "**N**" - Redirects the user back to the start question.                                                                                                           | **Insert Video here** |
| Input invalid characters                               | Inputs "**0**", "**@**" or "(space)"                     | The user will receive a witty comment asking them to input the valid characters.                                                                                                                             | **Insert Video here** |
| Input a valid username                                 | Inputs a word                                            | The usernames first letter will become capitalized and a starting message will show.                                                                                                                         | **Insert Video here** |
| Input an invalid username                              | Inputs any number/symbol/space in-between                | The user will receive an invalid username error and told what they cannot input as a username and asked to input a valid one.                                                                                | **Insert Video here** |
| Input a correct letter                                 | Inputs a correct letter                                  | The user will be told they guessed correctly and shown where in the word the letter is placed, plus the letters they have used so far.                                                                       | **Insert Video here** |
| Input a incorrect letter                               | Inputs a incorrect letter                                | The user will be told the guess was incorrect and that they lost a life, displaying how many lives they have left. Plus, the word they are trying to guess and the letters they have used.                   | **Insert Video here** |
| Input an invalid character / same letter               | Inputs a number/symbol/empty space/a letter already used | **Invalid character** - The user will be told the input is invalid and o try again. **Same letter** - User is displayed a witty message, told you cannot input the same letter twice and asked to try again. | **Insert Video here** |
| If word is guessed correctly                           | User guesses word correctly                              | The user is shown the word they guessed, a congratulations message and asked if they want to play again.                                                                                                     | **Insert Video here** |
| If word is guessed incorrectly                         | User guesses word incorrectly                            | The user is show the word they didn't guess, a small unlucky message and asked if they would like to play again.                                                                                             | **Insert Video here** |
| Input "**Y**" to play again                            | Inputs "**Y**"                                           | The user will be given a funny motivating message and immediately given the chance to guess a letter for the next word to guess.                                                                             | **Insert Video here** |
| Input "**N**" to play again                            | Inputs "**N**"                                           | The user will be given a confirmation question to answer                                                                                                                                                     | **Insert Video here** |
| Input "**Y**" or "**N**" to confirmation question      | Inputs "**Y**" or "**N**"                                | "**Y**" - A goodbye message is displayed. "**N**" - Redirects the user back to the play again question with a witty message added.                                                                           | **Insert Video here** |

---

#### Compatibility testing

Testing was completed on Google Chrome, Microsoft Edge, Firefox web browsers. As you go through the videos you will also see all of the user validation works correctly and the inputs the user makes create the correct response as per the code.

- Google Chrome

https://github.com/cjphawes/hangman-project-three/assets/105741584/2d1d9a60-9a93-43a4-8515-846fb222b82e

- Microsoft Edge

https://github.com/cjphawes/hangman-project-three/assets/105741584/5343ba47-4b2c-4ee1-9816-04f2748d45de

- Firefox

https://github.com/cjphawes/hangman-project-three/assets/105741584/9c5e492c-7688-4039-a7b3-eb7926f80c18

#### Compatibility issues

- The heart emoji is a different size and color depending on the browser the user is using.
- On the Firefox web browser the emoji's displayed half of the emoji.
- From user testing, I found on Safari web browsers the game does not allow you to input a "**Y**" or ""**N**" to start or end the game.
