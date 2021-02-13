import random

print("Guess the number- game")

rand=random.randint(1,9)
chances=0

print("Guess a number between 1 and 9")

while(chances<5):
    guess=int(input("Enter your guess: "))
    if(guess==rand):
        print("congrats! you won")
        break
    elif(guess<rand):
        print("hint: your guess is smaller than the actual number! try again!")
    else:
        print("hint: your guess is greater than the actual number! try again!")
    chances=chances+1

if(chances==5):
    print("Sorry! You lose!")
