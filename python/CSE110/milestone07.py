import random

game = True
play = True

while game is True:

    guesses = 0
    guess = 0
    secret_word = "meridian"

    while play is True:
        guess = input("What is your guess? ")
        guesses = guesses + 1
        if guess != secret_word:
            print("That is not the secret word")
        elif guess == secret_word:
            print(f"You guessed it after {guesses} guesses!")
            game = False
            play = False
        else:
            print("Please guess again.")

game_play = input('Would you like to play again? (Y/N)')

if game_play.lower() == "y":
    game = True
else:
    game = False
