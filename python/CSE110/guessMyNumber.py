import random
game = "y"
play = True
while game == "y":
    number = random.randint(1, 100)
    guesses = 0
    guess = 0

    while play:
        guess = int(input("What is your guess? "))
        guesses = guesses + 1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print(f"You guessed it after {guesses} guesses!")
            print

game = input('Would you like to continue playing Y/N? ')
if game == "y":
    game = "y"
else:
    print("Thank you for playing. Goodbye.")
