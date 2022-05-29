print('Welcome to Your Choice Adventure!')
input("Hit enter to begin... if you dare.")
print()

choiceOne = input("You are on an adventure in the snowy mountains and are about to start your climb to the summit.\
 Do you want to take the path to the right or to the left? (RIGHT/LEFT)")

if choiceOne.lower() == "right":
    choiceTwo = input('You start making your way up the path on the right. After some time, \
you come across a rope bridge. It is old and has been beaten down by the harsh weather. \
Do you want to continue across the bridge or do you want to look around and try to find another way across? (LOOK/CROSS)')

    if choiceTwo.lower() == "look":
        choiceThree = input('You look around, but to no avail you are not able to find another \
way to get to the other side of the bridge. Do you want to run across the bridge or try to use caution? (RUN/CAUTION) ')

        if choiceThree.lower() == "run":
            choiceFour = input("You try running across the bridge and take a step on a board that was rotten. \
You fall off the bridge and are unable to continue. Would you like to restart the game? (Y/N) ")

            if choiceFour.lower() == "y":
                print('Please open a new window')

            elif choiceFour.lower() == "n":
                print('Thank you for playing!')
            else:
                print('Invalid entry please restart.')

        elif choiceThree.lower == "caution":
            choiceFour = input('You slowly make your way across the bridge testing each board before stepping. \
After a long, slow manuver across the bridge you find that your are stuck on a the face of \
an ice wall and have nowhere to go. Would you like to restart the game? (Y/N) ')

            if choiceFour.lower() == "y":
                print('Please open a new window')

            elif choiceFour.lower() == "n":
                print('Thank you for playing!')
            else:
                print('Invalid entry please restart.')

    elif choiceTwo.lower() == "cross":
        choiceThree = input('You look around, but to no avail you are not able to find another \
way to get to the other side of the bridge. Do you want to run across the bridge or try to use caution? (RUN/CAUTION) ')

        if choiceThree.lower() == "run":
            choiceFour = input("You try running across the bridge and take a step on a board that was rotten. \
You fall off the bridge and are unable to continue. Would you like to restart the game? (Y/N) ")

            if choiceFour.lower() == "y":
                print('Please open a new window')

            elif choiceFour.lower() == "n":
                print('Thank you for playing!')
            else:
                print('Invalid entry please restart.')

        elif choiceThree.lower == "caution":
            choiceFour = input('You slowly make your way across the bridge testing each board before stepping. \
After a long, slow manuver across the bridge you find that your are stuck on a the face of \
an ice wall and have nowhere to go. Would you like to restart the game? (Y/N) ')

            if choiceFour.lower() == "y":
                print('Please open a new window')

            elif choiceFour.lower() == "n":
                print('Thank you for playing!')
            else:
                print('Invalid entry please restart.')

elif choiceOne.lower() == "left":
    choiceTwo = input('You start making your way up the path on the left. After some time, \
you come across a fork in the path do you want to go on the path that leads up or down? (UP/DOWN) ')

    if choiceTwo.lower() == "up":
        choiceThree = input('Wise choice! You want to go to the summit remember? You head down the path \
and it starts to get steep rapidly. Congratulations! You got to the summit. \
Would you like to take a picture, do a dance, or go home and sleep? (PICTURE/DANCE/HOME) ')

        if choiceThree.lower() == "picture":
            print('Thank you for playing!')

        elif choiceThree.lower() == "dance":
            print('Thank you for playing!')

        elif choiceThree.lower() == "home":
            print('Thank you for playing!')
        else:
            print('Invalid entry please restart.')

    elif choiceTwo.lower() == "down":
        choiceThree = input('Why would you want to go down? You want to go to the summit remember? \
You head down the path and eventually find a dead end. Would you like to restart the game? (Y/N) ')

        if choiceThree.lower() == "y":
            print('Please open a new window')

        elif choiceThree.lower() == "n":
            print('Thank you for playing!')
        else:
            print('Invalid entry please restart.')
else:
    print('Invalid entry please restart.')
