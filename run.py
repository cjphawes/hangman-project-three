import random 



def start_game():
    user_response = input("Would you like to start the game? Y/N: \n").upper()
    if user_response == "Y":
        print("Entering Game Now...\n")
    elif user_response == "N":
        print("Exiting Game Now...\n")
    else:
        print("Invalid input, please enter Y or N.")

    # try:
    #     print(f"You chose {user_response}")
    # except ValueError:
    #     print("I didn't ask for that did I?")



def main():
    start_game()

print("Welcome to Hangman Havoc!\n")
main()