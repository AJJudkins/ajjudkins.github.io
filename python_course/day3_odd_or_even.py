print("This program will tell you if a number is even or odd.")
cont = True

while cont == True:

    number = int(input("What is the number you want to check? \n"))
    odd = number % 2
    if odd == 1:
        print(f"{number} is odd.")
    else:
        print(f"{number} is even.")

    continue_playing = input("Would you like to continue? [Yes or No] \n")
    if continue_playing.lower() == "yes":
        cont = True
    else:
        cont = False

print("Thanks for playing!")
