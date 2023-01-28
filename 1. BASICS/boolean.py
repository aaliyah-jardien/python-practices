# BOOLEANS
# comparing expressions whether they are True or False
# python returns the boolean answer

print(10>9)
print(13==13)
print(10==9)
print(10<9)

# assigning values to the variables with conditions using if statement
a = 200

b = 150

if b > a:
    print("b is greater than a")

else:
    print("a is greater than b")

# evaluating values
# bool() function allows any value to be evaluated....will always return True or False
print(bool("Hello there!"))
print(bool(15))

# declaring variables
name = "Aaliyah"
age = 0

# call variable in function you want to return
print(bool(name))

print(bool(age)) #returns false as the number is 0

# most values are true if it has content
    # empty strings are False
    # 0 as integer numbers are False
    # empty sets, dictionaries, tuples and lists are False if it's empty
    # the value None also returns false

# returning false
bool(False)

bool(None)

bool(0)

bool("")

bool(())

bool([])

bool({})

# functions can return a boolean
def myFunction():
    return True

print(myFunction())

# execute code based off boolean answer
# function and if statement

# declaring function
def theFunction():
    return True

if theFunction():
    print("YES!")

else:
    print("NO!")

# isinstance() function determines if an object belongs to a specific data type
test = 300

print(isinstance(test, int))