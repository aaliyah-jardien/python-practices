# else in while loops
# runs code once condition IS NOT true

# PRINTS IF CONDITION IS FALSE

coin = 1

# while loop
while coin < 12:
    print(coin)
    coin += 1 # increment coin by one
else: # when it's equal to 12 it makes the while false, then does the else
    print("coin is no longer less than 12")