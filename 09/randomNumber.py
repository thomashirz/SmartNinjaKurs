#import random

#details könnten schon ausführlicher erklärt werden "Homework" hat schon 35min begonnen

from random import randint

secret = randint(0, 30)

winner = True

while(Winner):

    guess = int(input("Guess the number between 1-100: "))


    if secret == guess:
        print("Winner, Winner, Chicken Dinner! Here is a cookie")
        winner = False

    elif secret > guess:
        print("Oh, you guessed to low. Try again.")

    elif secret < guess:
        print("You were shooting for the stars, but that's too high. Try again.")