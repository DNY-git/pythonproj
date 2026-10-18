import random

secret = random.randint(1,20)
tries = 0
while True:
    guess = int(input("your guess"))
    tries = tries + 1
    if guess == secret:
        print("correct, tries:",tries)
        break
    elif guess < secret:
        print("too low")
    else:
        print("too high")