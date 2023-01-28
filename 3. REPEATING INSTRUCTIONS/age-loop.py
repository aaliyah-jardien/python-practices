# declaring my variables
my_number = 21
your_guess = 0

while(your_guess != my_number):

    your_input = input("Guess my number: ")
    your_guess = int(your_input)

    if your_guess < my_number:
        print("Guess higher!")
    elif your_guess > my_number:
        print("Guess lower")

    else:
        print("You got it!")
