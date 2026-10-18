import random

secret = random.randint(1,20)
tries = 0
while True:
    try:
        guess = int(input("your guess:"))
    except ValueError:
        print("please enter a valid number")
        continue
    tries = tries + 1
    if guess == secret:
        print("correct, tries:",tries)
        break
    elif guess < secret:
        print("too low")
    else:
        print("too high")