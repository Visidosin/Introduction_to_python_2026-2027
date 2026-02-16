import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess: "))
    guesses += 1

    if guess < number:
        print("Go up")
    elif guess > number:
        print("Go down")
    else:
        print(f"Found in {guesses} guesses")
        break