# get user input to guess the correct number

# declaring variables
secret_number = 54
user_guess = 0

while (user_guess != secret_number):
    user_guess = int(input("Guess a number: "))
    
    if user_guess > secret_number:
        print("Guess lower!")
    elif user_guess < secret_number:
        print("Guess higher!")
        
print("You guessed right! Well done =)")