my_number = 42

while True: # The loop condition is always true
    your_input = input("Guess my number: ")
    your_guess = int(your_input)

    if your_guess == my_number:
        break # and we break out of the loop here

    if your_guess < my_number:
        print("guess higher!")

    else:
        print("guess lower!")
        
print("You got it!")