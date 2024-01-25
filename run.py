import random
from words import list_of_words
import emoji
import string
from colorama import Fore, Style



def start_game():
    """
    Asks user if they are ready to start the game, with user validation
    """
    waving_hand = emoji.emojize("\U0001F44B")
    confused_emoji = emoji.emojize("\U0001F928")

    while True:
        user_response = input(
            "Would you like to start the game?" + " \033[1;32mY\033[0m"
            + "/" + "\033[0;31mN\033[0m" + ": ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            print("Welcome to...\n")
            file = open("hangman_title.txt", "r")
            lines = file.read()
            file.close()
            print(lines)
            break
        elif user_response == "N":
            print(f"Exiting Game Now...\nThank you for playing!{waving_hand}")
            exit()
        else:
            print(f"{confused_emoji} I didn't ask for that did I?, please" 
                  " enter Y or N.\n")
    return user_response

def display_rules():
    """
    Displays the rules for the game
    """
    heart_emoji = emoji.emojize("\u2764\ufe0f")
    heart_emoji_multiplied = heart_emoji * 8
    green_tick = emoji.emojize("\u2705")
    writing = emoji.emojize("\U0001F4DD")
    

    rules = (
        f"\n\n\033[4mHere are the rules\033[0m" + f"{writing}\n\n"
        "\033[1;37m1.\033[0m" + " I will give you a word, it is your job to"
        " guess the letters that make up that word.\n" 
        f"\033[1;37m2.\033[0m" + f" You have 8 {heart_emoji_multiplied}"
        "  lives available, every time you get a letter incorrect, you" 
        f" will lose a {heart_emoji}\n"
        "\033[1;37m3.\033[0m" + " Guess a letter and I will tell you if it"
        " is correct or not.\n"
        "\033[1;37m4.\033[0m" + " Keep guessing until you either, lose"
        f" all your {heart_emoji} 's, or you guess the word correctly" 
        f" {green_tick}\n"
        "\033[1;37m5.\033[0m" + " Finally, insert your username and" 
        " have fun!\n"
        )
    print(rules)

def input_username():
    """
    Asks user for username, with user validation to make sure there are no
    invalid inputs
    """
    prohibited = emoji.emojize("\U0001F6AB")

    while True:
        username = input("What will your username be?: ").capitalize().strip()

        if username.isalpha():
            print(f"\nOkay {username}, let's get started!\n")
            break
        else:
            print(Fore.RED + 
                f"{prohibited} {username} is an INVALID username, please use one without\n"
                "numbers, special characters or spaces."
                )
            print(Style.RESET_ALL)
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
    heart_emoji = emoji.emojize("\u2764\ufe0f")
    cross_emoji = emoji.emojize("\u274C")
    green_tick = emoji.emojize("\u2705")
    prohibited = emoji.emojize("\U0001F6AB")
    shocked_face = emoji.emojize("\U0001F626")

    new_word = get_correct_word(list_of_words)
    word_makeup = set(new_word) #tell us the letters that make up the word
    alphabet = set(string.ascii_uppercase) #letters of alphabet in CAPS
    guessed_letters = set() #this tells us what the user has guessed
    lives_allowed = 8 

    """
    Grabbing the users input for a letter guess and seeing if it is a letter
    they have guessed already or not
    """    
    while len(word_makeup) > 1 and lives_allowed > 1:
        letter_guess = input("Guess a letter: ").upper()

        if letter_guess in alphabet - guessed_letters:
            guessed_letters.add(letter_guess)

            if letter_guess in word_makeup:
                word_makeup.remove(letter_guess)
                print(f"You guessed correctly {green_tick}")
        
            else:
                lives_allowed = lives_allowed - 1
                print(f"Incorrect! You have {lives_allowed} {heart_emoji} 's remaining.")

        elif letter_guess in guessed_letters:
            print(f"{cross_emoji} Whoops! You cannot guess the same letter twice. Please try again.")

        else:
            print(Fore.RED + f"{prohibited} INVALID character, please try again.")
            print(Style.RESET_ALL)

        #telling the user what letters they have guessed
        print("You have have used letters: ", ' '.join(guessed_letters))
        print("")

        #what the current word is being guessed
        word_list = [letter if letter in guessed_letters else '-' for letter in new_word]
        print("Your word is: ", ' '.join(word_list))
        print("")

    print(f"You Lost!{shocked_face}")
    print("The word was" + f" {new_word}")

    return word_makeup

# def restart_game():
#     """
#     Asks the user if they want to play another game or exit the program
#     """
#     main()

#     # waving_hand = emoji.emojize("\U0001F44B")

#     # reset_answer = input("Would you like to play again?" + " \033[1;32mY\033[0m"
#     #         + "/" + "\033[0;31mN\033[0m" + ": ").upper()
    
#     # if reset_answer == "Y":
#     #     start_game()
#     # elif reset_answer == "N":
#     #     print(f"Exiting Game Now...\nThank you for playing!{waving_hand}")
#     #     exit()



def main():
    start_game()
    display_rules()
    input_username()
    get_correct_word(list_of_words)
    guess_word()
    # restart_game()

main()
