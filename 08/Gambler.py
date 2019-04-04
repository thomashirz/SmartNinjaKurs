secret = 69
winner = True

while(winner):

    guess = int(input("Guess the number between 1-100: "))


    if secret == guess:
        print("Winner, Winner, Chicken Dinner! Here is a cookie")
        winner = False

    elif secret > guess:
        print("Oh, you guessed to low. Try again.")

    elif secret < guess:
        print("You were shooting for the stars, but that's too high. Try again.")



