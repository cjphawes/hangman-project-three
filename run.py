import random
# import 
# from 



def start_game():
    """
    Asks user if they are ready to start the game, with user validation and
    display the rules of the game
    """
    while True:
        user_response = input("Would you like to start the game? Y/N: ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            print("Welcome to...\n")
            file = open("hangman_title.txt", "r")
            lines = file.read().center(50)
            file.close()
            print(lines)
            break
        elif user_response == "N":
            print("Exiting Game Now...\nThank you for playing!")
            exit()
        else:
            print("I didn't ask for that did I?, please enter Y or N.\n")

    rules = (
        f"Here are the rules:\n"
        f"1. Insert your username.\n"
        f"2. I will give you a word to guess, it is your job to guess\n"
        f"   the letters that make up that word.\n" 
        f"3. Input a letter and I will tell you if it is in the word or not.\n"
        f"4. Keep guessing a letter until you either, lose all your lives or\n"
        f"   you guess the word correctly.\n"
        f"5. Finally, Have Fun!\n"
        )
    print(rules)

def input_username():
    """
    Asks user for username, with user validation to make sure there are no
    invalid inputs
    """
    while True:
        try:
            username = str(input("What will your username be?: ")).capitalize()
            break
        except ValueError:
            print(
                f"{username} is not a valid username, please use one without"
                f"numbers, special characters")

    print(f"\nOkay {username}, let's get started, here is your word!\n")



def main():
    start_game()
    input_username()

main()