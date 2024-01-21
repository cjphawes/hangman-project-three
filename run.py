import random 



def start_game():
    """
    Asks user if they are ready to start the game, if Y then they will enter
    the game, if N they will exit the game, if Invalid input they will receive
    an error and asked for the correct input
    """
    while True:
        user_response = input("Would you like to start the game? Y/N: ").upper()

        if user_response == "Y":
            print("Entering Game Now...\n")
            print("Welcome to Hangman Havoc!\n")
        elif user_response == "N":
            print("Exiting Game Now...\n")
            break
        else:
            print("I didn't ask for that did I?, please enter Y or N.\n")

    # try:
    #     print(f"You chose {user_response}")
    # except ValueError:
    #     print("I didn't ask for that did I?")



def main():
    start_game()

main()