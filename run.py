import random 



def start_game():
    """
    Asks user if they are ready to start the game, with user validation and
    display the rules of the game
    """
    while True:
        user_response = input("Would you like to start the game? Y/N: ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            print("Welcome to Hangman Havoc!\n")
            break
        elif user_response == "N":
            print("Exiting Game Now...\nThank you for playing!")
            
            exit()
        else:
            print("I didn't ask for that did I?, please enter Y or N.\n")
    rules = (
        f"Here are the rules:\n"
        f"1. Insert your username\n"
        f"2. I will give you a word to guess, it is your job to guess\n"
        f"   the letters that make up that word.\n" 
        f"3. Input a letter and I will tell you if it is in the word or not\n"
        f"4. Keep guessing a letter until you either lose all your lives or"
        f"   you guess the word correctly."
        f"5. Finally, Have Fun!"
        )
    print(rules)

    # try:
    #     print(f"You chose {user_response}")
    # except ValueError:
    #     print("I didn't ask for that did I?")


def main():
    start_game()

main()