# repeating loops
# guess my number

# declare variables
my_number = 21

your_guess = 0 #starts from 0

while True: # loop condition is always true
    # declare input variable
    # your_input = int(input("Guess my number: ")) #this does not run properly
    your_input = input("Guess my number: ")
    your_guess = int(your_input) # making sure the input is an integer

    # (your_guess != my_number):

    if your_guess == my_number:
        break # we break out the loop here...you guessed right will print, it's out of the loop

    # nested if statement
    if your_guess < my_number:
        print("Guess Higher!")

    else: 
        print("Guess lower!")

print("You guessed right!")

"""
using while statements and nested loops
goes through first if statement if true will stop (break)
if not will go through other executions until correct
kwaai
"""