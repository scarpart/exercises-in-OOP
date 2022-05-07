import os
from Board import Board

# Defining extra-class functions to be used in implementing the game
def refresh_board():
    # Always clears the board
    os.system("cls")

    # Calls the create_board method again to write it on screen
    my_board.create_board()   


flag_variable = True
while True:
    if flag_variable:
        my_board = Board(input("Welcome! Please select a word for the other player to guess: "))
        flag_variable = False

    # Always refreshes the board
    refresh_board()

    # Asks the user to input a guess then updates the board based on it
    guess = input("Try guessing a letter: ")
    while len(guess) != 1:
        guess = input("Oops, sorry, you tried guessing more than one letter. Guess again: ")
    my_board.update_guess(guess)

    # Checks if the game has ended (either user guessed correctly or got hanged (skill issue))
    game_ended, reason = my_board.has_game_ended()
    if game_ended:
        refresh_board()
        if reason == "OoT":
            print("You were hanged for guessing incorrectly!")
        elif reason == "GiR":
            print("Congratulations, you guessed the word correctly and defeated the noose!")
        
        # Checks if players want to play again and updates the flag variable
        play_again = input("Do you wish to play again? Y/N --> ")
        while play_again != "Y" and play_again != "N":
            play_again = input("Oops! What you selected is not an option. Please, try again (Y/N): ")
        
        if play_again == "Y":
            flag_variable = True
            continue
        elif play_again == "N":
            break