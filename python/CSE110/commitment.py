
word = "commitment"

favorite = input("What is your favorite letter? ")

for letter in word:
    if letter.lower() == favorite.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == favorite.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

play = "yes"

while play == "yes":
    number = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")

    # This puts a newline at the end of the list of quote
    print()

    play = input("Would you like to enter another number? (yes/no)")

print("Goodbye")
