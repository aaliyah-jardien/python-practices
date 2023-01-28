#  PASSIING A LIST AS AN ARGUEMENT

# you can make an arguement in any form of data type
# arguements in a function can be a string, number, list, dictionary
#  and it will be treated as the same data type inside the function

# so if you send a list as an arguements in a function...
#  it will still be a list when it reaches the function

#  defining function
def myfunction(food):   # food is what you eat, it' the parameter here
    for x in food:      # for loop in function
        print(x)

# creating a list
# the parameter is fruits, it's a type of food
fruits = ["apple", "banana", "grapes"]

myfunction(fruits)      # prints under each other
myfunction([fruits])    # prints in a line

# YOU CAN CALL A FUNCTION AS MANY TIMES AS YOU WANT
