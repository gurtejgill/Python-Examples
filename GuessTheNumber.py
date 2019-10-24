from random import randint

randomNumber = (randint(0,20))
userInput = input("Enter a number between 0-20>")

if(int(userInput) == randomNumber):
    print("You guessed it right")
elif(int(userInput) > randomNumber):
    print("Your guess is too high, original number is " + str(randomNumber))
else:
    print("Your guess is too low, original number is " + str(randomNumber))