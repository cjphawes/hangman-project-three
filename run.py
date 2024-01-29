import random
import os
from words import list_of_words
import string
from colorama import Fore, Style
from number_styling import (underline,
color_white, 
color_green,
color_red,
styling_end)
from emoji_dict import (waving_hand,
confused_emoji,
heart_emoji,
heart_emoji_multiplied,
green_tick,
writing,
prohibited,
cross_emoji,
shocked_face,
face_with_hearts,
winky_face)

def start_game():
    """
    Introduces the game and provides a small introduction into what the game 
    entails
    """
    print("\n\nWELCOME TO...\n")
    file = open("hangman_title.txt", "r")
    lines = file.read()
    file.close()
    print(lines)
    print("\n\nThe exciting word-guessing game where your vocabulary skills"
        " are put to the test! In this game, you have a limited number of lives"
        " to guess the hidden word correctly. With each incorrect guess, you'll"
        " lose a life. Can you figure out the word and avoid running out of"
        " lives? Challenge yourself and see how many words you can solve in a"
        " row! Let's dive in and start guessing!\n\n")

def enter_game():
    # Asks user if they are ready to start the game, with user validation
    while True:
        user_response = input(f"Would you like to start the game? {color_green}"
            f"Y{styling_end}/{color_red}N{styling_end}: ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            break
        elif user_response == "N":
            print(f"Exiting Game Now...\nThank you for playing!{waving_hand}")
            exit()
        else:
            print(f"""{confused_emoji} I didn't ask for that did I?, please 
                enter Y or N.\n""")
    return user_response

def display_rules():
    """
    Displays the rules for the game
    """
    rules = (f"\n\n{underline}Here are the rules{styling_end} {writing}\n\n"
        f"{color_white}1.{styling_end} I will give you a mystery word, it is"
        f" your job to guess the letters that make up that word.\n{color_white}"
        f"2.{styling_end} You have 8 {heart_emoji_multiplied}  lives available,"
        f" every time you get a letter incorrect, you will lose a {heart_emoji}"
        f"\n{color_white}3.{styling_end} Guess a letter and I will tell you if"
        f" it is correct or not.\n{color_white}4.{styling_end} Keep guessing"
        f" until you either, lose all your {heart_emoji} 's, or you guess the"
        f" word correctly {green_tick}\n{color_white}6.{styling_end} You will"
        f" not know the length of the word until you make your first guess!"
        f" Mysterious I know {winky_face} It could be 4 letters or upto 9!\n"
        f"{color_white}5.{styling_end} Finally, insert your username and"
        f"have fun!\n")
    print(rules)

def input_username():
    """
    Asks user for username, with user validation to make sure there are no
    invalid inputs
    """
    while True:
        username = input("What will your username be?: ").strip().capitalize()

        if username.isalpha():
            print(f"\nOkay {username}, let's get started!\n")
            break
        else:
            print(Fore.RED + 
                f"""{prohibited} {username} is an INVALID username, please use 
                one without numbers, special characters or spaces.""" +
                Style.RESET_ALL)
            # print(Style.RESET_ALL)
    return username

def get_correct_word(list_of_words):
    """
    Get a valid random word from the list of words available and display to 
    the user
    """
    new_word = random.choice(list_of_words)

    while "-" in new_word or " " in new_word:
        new_word = random.choice(list_of_words)
        
    return new_word.upper()

def guess_word():
    """
    Validates the letter chosen if it is either in or not in the word that is
    being guessed by the user
    """
    new_word = get_correct_word(list_of_words)
    word_makeup = set(new_word) #tell us the letters that make up the word
    alphabet = set(string.ascii_uppercase) #letters of alphabet in CAPS
    guessed_letters = set() #this tells us what the user has guessed
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
                print(f"""Incorrect, You lost a life! You now have
                    {lives_allowed} {heart_emoji} 's remaining.""")

        elif letter_guess in guessed_letters:
            print(f"""{cross_emoji} Whoops! You cannot guess the same letter
                twice. Please try again.""")

        else:
            print(Fore.RED + f"""{prohibited} INVALID character, please try
                again.""" + Style.RESET_ALL)
            # print(Style.RESET_ALL)

        #telling the user what letters they have guessed
        print("You have have used letters: ", ' '.join(guessed_letters))
        print("")

        #what the current word is being guessed
        word_list = [letter if letter in guessed_letters else '-' for letter in new_word]
        print("Your word is: ", ' '.join(word_list))
        print("")

    if lives_allowed == 0:
        print(f"You Lost!{shocked_face}\nThe word was" + f" {new_word}")
        play_again = input(
            "Would you like to restart the game?" + " \033[1;32mY\033[0m"
            + "/" + "\033[0;31mN\033[0m" + ": ").upper()
        if play_again == "Y":
            print("Restarting game now...")
            #Code to restart game
        elif play_again == "N": 
            print(f"Exiting Game Now...\nThank you for playing!{waving_hand}")
        else:
            print(f"""{confused_emoji} I didn't ask for that did I?, please 
                enter Y or N.\n""")
    else:
        print(f"Yay! You did it {face_with_hearts}")
        play_again = input(
            "Would you like to restart the game?" + " \033[1;32mY\033[0m"
            + "/" + "\033[0;31mN\033[0m" + ": ").upper()
        if play_again == "Y":
            print("Restarting game now...")
            #Code to restart game
        elif play_again == "N":
            print(f"Exiting Game Now...\nThank you for playing!{waving_hand}")
        else:
            print(f"""{confused_emoji} I didn't ask for that did I?, please
                enter Y or N.\n""")
    return word_makeup

def restart_game():
    """
    This function holds all the functions used to play the game after the 
    display rules function, when the user decides they want to play the game 
    again.
    """




def main():
    start_game()
    enter_game()
    display_rules()
    input_username()
    get_correct_word(list_of_words)
    guess_word()
    restart_game()

main()
