#import random

#details könnten schon ausführlicher erklärt werden "Homework" hat schon 35min begonnen

from random import randint

secret = randint(0, 100)

attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Highscore: "+ str(best_score))

score_file.close()

while True:

    attempts += 1

    guess = int(input("Guess the number between 1-100: "))


    if secret == guess:
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("Winner, Winner, Chicken Dinner! Here is a cookie")
        break

    elif secret > guess:
        print("Oh, you guessed to low. Try again.")

    elif secret < guess:
        print("You were shooting for the stars, but that's too high. Try again.")


print(attempts)

print(juhu)