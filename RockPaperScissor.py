from random import randint

options = ['r','p','s']

won = False

while won == False:
    userInput = input("Enter r for rock, p for paper or s for scissor> ")
    computer = options[randint(0,2)]

    if userInput == computer:
        print("Tie!!")
    elif userInput == 'r':
        if computer == 'p':
            print("You lost ", computer, " covers ", userInput)
        elif computer == 's':
            print("You won ", userInput, " breaks ", computer)
            won = True
            break
    elif userInput == 'p':
        if computer == 's':
            print("You lost ", computer, " cut ", userInput)
        elif computer == 'r':
            print("You won ", userInput, " covers ", computer)
            won = True
            break
    elif userInput == 's':
        if computer == 'r':
            print("You lost ", computer, " breaks ", userInput)
        elif computer == 'p':
            print("You won ", userInput, " cut ", computer)
            won = True
            break
    else:
        print("Check your spelling")
