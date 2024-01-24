import random
from words import list_of_words
# import 



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
    rules = (
        f"\n\nHere are the rules:\n\n"
        f"1. Insert your username.\n"
        f"2. I will give you a word, it is your job to guess the letters\n"
        f"   that make up that word.\n" 
        f"3. Guess a letter and I will tell you if it is correct or not.\n"
        f"4. Keep guessing until you either, lose all your lives or you\n"
        f"   guess the word correctly.\n"
        f"5. Finally, have fun!\n"
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
            print(f"\nOkay {username}, let's get started, here is your word!\n")
            break
        else:
            print(
                f"{username} is not a valid username, please use one without\n"
                f"numbers or special characters"
                )
    return username

def get_correct_word(list_of_words):
    """
    Get a valid random word from the list of words available and display to 
    the user
    """
    new_word = random.choice(list_of_words)

    while "-" in new_word or "" in new_word:
        new_word = random.choice(list_of_words)
        
    return new_word.upper()

# def validate_letter():
#     new_word = get_correct_word(list_of_words)
#     word_makeup = set(new_word)


def main():
    start_game()
    display_rules()
    user = input_username()
    display_word = get_correct_word(list_of_words)
    print(f"{user} your word is {display_word}")


main()
