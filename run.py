import random 



def start_game():
        try:
            start = input("Would you like to start the game? Y/N: ")
            print(f"You chose {start}")
        except ValueError:
            print("I didn't ask for that did I?")



def main():
    start_game()

print("Welcome to Hangman Havoc!\n")
main()