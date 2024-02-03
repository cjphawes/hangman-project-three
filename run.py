"""
All imports starting with Built-in, then 3rd party and then local
imports
"""
import string
import random
import sys
from colorama import Fore, Style
from number_styling import *
from emoji_dict import *
from rules import rules
from words import list_of_words


def start_game():
    """
    Introduces the game and provides a small introduction into what the game
    entails
    """
    print("\nWELCOME TO...\n")
    file = open("hangman_title.txt", "r")
    lines = file.read()
    file.close()
    print(lines)
    print(
        f"\n\nThe exciting word-guessing game where your vocabulary skills"
        f" are put to the\ntest! In this game, you have a limited number"
        f" of {heart_emoji}  lives to guess the hidden\nword correctly. Can"
        f" {color_white}YOU{styling_end} figure out the word and avoid running"
        f" out of lives? {color_white}Challenge{styling_end} yourself and see"
        f" how many words you can solve in a row! Dive in and start"
        f" guessing!\n\n"
        )


def enter_game():
    """Asks user if they are ready to start the game, with user validation"""
    while True:
        user_response = input(
            f"Would you like to start the game? {color_green}Y{styling_end}/"
            f"{color_red}N{styling_end}: "
            ).upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            break
        elif user_response == "N":
            while True:
                user_response_2 = input(
                    f"Are you a quitter?: {color_green}Y"
                    f"{styling_end}/{color_red}N{styling_end}: "
                    ).upper()

                if user_response_2 == "Y":
                    print(
                        f"\nBut we didn't even get to play together {sad_face}"
                        f"\nThank you for playing!{waving_hand}"
                        )
                    sys.exit()
                elif user_response_2 == "N":
                    print(f"\nI DIDN'T THINK SO {crazy_face}  LET'S GO!")
                    break
                else:
                    print(
                        f"{confused_emoji} I didn't ask for that did I?,"
                        f" please enter Y or N.\n"
                        )
        else:
            print(
                f"{confused_emoji} I didn't ask for that did I?, please"
                f" enter Y or N.\n"
                )
    return user_response


def display_rules():
    """Displays the rules for the game"""
    print(rules)


def input_username():
    """
    Asks user for username, with user validation to make sure there are no
    invalid inputs
    """
    while True:
        username = input("What will your username be?: ").strip().capitalize()

        if username.isalpha():
            print(
                f"\nAwesome username {username},"
                f" Let's Get Guessing!\n"
                )
            break
        else:
            print(
                Fore.RED + f"{prohibited} {username} is an INVALID username,"
                f" please use one without numbers, special characters or"
                f" spaces.\n" + Style.RESET_ALL)
    return username


def get_correct_word(list_of_words):
    """
    Get a valid random word from the list of words available and display to
    the user
    """
    new_word = random.choice(list_of_words)

    while any(char in new_word for char in ("-", " ")) or len(new_word) < 4:
        new_word = random.choice(list_of_words)

    return new_word.upper()


def guess_word():
    """
    Validates the letter chosen if it is either in or not in the word that is
    being guessed by the user
    """
    new_word = get_correct_word(list_of_words)
    word_makeup = set(new_word)  # Tell us the letters that make up the word
    alphabet = set(string.ascii_uppercase)  # Letters of alphabet in CAPS
    guessed_letters = set()  # This tells us what the user has guessed
    lives_allowed = 8

    """
    Grabbing the users input for a letter guess and seeing if it is a letter
    they have guessed already or not
    """
    while len(word_makeup) > 0 and lives_allowed > 0:
        letter_guess = input("Guess a letter: ").upper()

        if letter_guess in alphabet - guessed_letters:
            guessed_letters.add(letter_guess)

            if letter_guess in word_makeup:
                word_makeup.remove(letter_guess)
                print(f"You guessed correctly {green_tick}")

            else:
                lives_allowed = lives_allowed - 1
                print(
                    f"Incorrect, You lost a life! You now have {lives_allowed}"
                    f" {heart_emoji} 's remaining."
                    )

        elif letter_guess in guessed_letters:
            print(
                Fore.RED + f"{cross_emoji} Whoops! You cannot guess the same"
                f" letter twice. Please try again." + Style.RESET_ALL)

        else:
            print(
                Fore.RED + f"{prohibited} INVALID character, please try"
                f" again." + Style.RESET_ALL)

        # Telling the user what letters they have guessed
        print("You have have used letters: ", ' '.join(guessed_letters))
        print("")

        # What the current word is being guessed
        word_list = [
            letter if letter in guessed_letters else '-' for letter in new_word
            ]
        print("Your word is: ", ' '.join(word_list))
        print("")

    if lives_allowed == 0:
        print(
            f"You {color_white}LOST!{styling_end}{shocked_face}\nThe word was"
            f" {color_white}{underline}{new_word}{styling_end}\n"
            )
    else:
        print(f"Yay! You did it {face_with_hearts}\n")
    return word_makeup


def restart_game():
    """
    This function holds all the functions used to play the game after the
    display rules function, when the user decides they want to play the game
    again.
    """
    while True:
        play_again = input(
            f"Would you like to start the game again? {color_green}Y"
            f"{styling_end}/{color_red}N{styling_end}: "
            ).upper()

        if play_again == "Y":
            print(
                f"YES! I like you {crazy_face}  Let's go again!\n")
            restart_functions()
        elif play_again == "N":
            while True:
                play_again_2 = input(
                    f"Are you sure?: {color_green}Y{styling_end}/{color_red}N"
                    f"{styling_end}: "
                    ).upper()

                if play_again_2 == "Y":
                    print(
                        f"\nBut we were having so much fun {sad_face}\n"
                        f"Thank you for playing!{waving_hand}")
                    sys.exit()
                elif play_again_2 == "N":
                    print(f"\nOH REALLY {crazy_face}")
                    break
                else:
                    print(
                        f"{confused_emoji} I didn't ask for that did I?,"
                        f" please enter Y or N.\n"
                        )
            restart_game()
        else:
            print(
                f"{confused_emoji} I didn't ask for that did I?, please enter"
                f" Y or N.\n"
                )


def restart_functions():
    """
    This function holds all the functions needed to restart the game in a
    continuous loop if the user wishes to play again
    """
    get_correct_word(list_of_words)
    guess_word()


def main():
    """Holds all functions to run the game"""
    start_game()
    enter_game()
    display_rules()
    input_username()
    get_correct_word(list_of_words)
    guess_word()
    restart_game()


main()
