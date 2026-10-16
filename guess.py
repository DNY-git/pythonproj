#The game a hardcoded secret number
print("guess the number")
guess = int(input("your guess:"))
print("you guessed:", guess)
secret = 7
if guess == secret:
    print("correct")
elif guess < secret:
    print("too low")
else:
    print("too high")
