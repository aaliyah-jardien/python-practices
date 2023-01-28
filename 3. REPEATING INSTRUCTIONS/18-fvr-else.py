# declare variable to true
successful = True

for number in range(3):
    print("Attempt")
    if successful:      # if statement until condition is met
        print("Successful")
        break
else:   # for else statement (only executed if none of the above conditons are met)
    print("Attempted 3 times and failed")