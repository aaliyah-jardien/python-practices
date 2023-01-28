# building options for a car game
print("Welcome to Initial Drift!")
print("Type 'help' for the game options.")

while True:     
    user_input = input("What would you like to do? ").lower()
	
    if user_input == "help":
        print('''
    Here are your options :)
    start - to start the car
    stop - to stop the car
    exit - to quit the game
    ''')
    
    elif user_input == "start":       # start command
        print("Car started...Ready to go!")
    
    elif user_input == "stop":      # stop command
        print("You stopped the car.")
    
    elif user_input == "exit":      # exit command
        print("You've exited the game.")
        break

    else:   # if the input is invalid                        
        print("I don't understand that...")
    
