# using a while loop to create a guessing game

secret_number = 9
guess_count = 0

while guess_count < 3:
    guess = int(input("Guess: "))
    guess_count += 1    # guess will increment until it reaches the limit
    if guess == secret_number:
        print("You guessed right!")
        break
else:
    print("You guessed wrong! No tries")
    