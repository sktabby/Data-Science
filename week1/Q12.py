# Q12. Create a number guessing game.

import random

secret = random.randint(1, 100)
guess = 0 


while guess != secret:
    guess = int(input("Enter the guess number: "))
    if guess<secret:
        print("Guess is too low")
    elif guess>secret:
        print("Guess is too high")
    else:
        print("Guessed number is correct")