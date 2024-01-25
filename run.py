import random
from words import list_of_words
import emoji
import string



def start_game():
    """
    Asks user if they are ready to start the game, with user validation
    """
    while True:
        user_response = input("Would you like to start the game? Y/N: ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            print("Welcome to...\n")
            file = open("hangman_title.txt", "r")
            lines = file.read()
            file.close()
            print(lines)
            break
        elif user_response == "N":
            print("Exiting Game Now...\nThank you for playing!")
            exit()
        else:
            print("I didn't ask for that did I?, please enter Y or N.\n")
    return user_response

def display_rules():
    """
    Displays the rules for the game
    """
    heart_emoji = emoji.emojize("\u2764\ufe0f")
    heart_emoji_multiplied = heart_emoji * 8
    green_tick = emoji.emojize("\u2705")
    

    rules = (
        f"\n\nHere are the rules:\n\n"
        f"1. Insert your username.\n"
        f"2. I will give you a word, it is your job to guess the letters\n"
        f"   that make up that word.\n" 
        f"3. You have 8 {heart_emoji_multiplied}  lives available, every\n"
        f"   time you get a letter incorrect, you will lose a {heart_emoji}\n"
        f"4. Guess a letter and I will tell you if it is correct or not.\n"
        f"5. Keep guessing until you either, lose all your {heart_emoji} 's\n"
        f"   or you guess the word correctly.{green_tick}\n"
        f"6. Finally, have fun!\n"
        )
    print(rules)

def input_username():
    """
    Asks user for username, with user validation to make sure there are no
    invalid inputs
    """
    while True:
        username = input("What will your username be?: ").capitalize().strip()

        if username.isalpha():
            print(f"\nOkay {username}, let's get started!\n")
            break
        else:
            print(
                f"{username} is not a valid username, please use one without\n"
                f"numbers or special characters."
                )
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
    # lives_allowed = 8
    word_makeup = set(new_word) #tell us the letters that make up the word
    alphabet = set(string.ascii_uppercase) #letters of alphabet in CAPS
    guessed_letters = set() #this tells us what the user has guessed

    """
    Grabbing the users input for a letter guess and seeing if it is a letter
    they have guessed already or not
    """
    while len(word_makeup) > 0:
        letter_guess = input("Guess a letter: ").upper()
        print("")

        if letter_guess in alphabet - guessed_letters:
            guessed_letters.add(letter_guess)

            if letter_guess in word_makeup:
                word_makeup.remove(letter_guess)
        
        elif letter_guess in guessed_letters:
            print("Whoops! You cannot guess the same letter twice.\n")

        else:
            print("Invalid character, please try again.\n")

        #telling the user what letters they have guessed
        print("You have used letters: ", ' '.join(guessed_letters))
        
        #what the current word is being guessed
        word_list = [letter if letter in guessed_letters else '-' for letter in new_word]
        print("The current word is: ", ' '.join(word_list))
        print("")

    return word_makeup



def main():
    start_game()
    display_rules()
    user = input_username()
    display_word = get_correct_word(list_of_words)
    guess_word()

main()
