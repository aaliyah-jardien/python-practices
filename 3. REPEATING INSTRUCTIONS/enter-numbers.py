# declaring my variables
# create the variable as an interger otherwise it will be read as a string
a = int(input("Enter your first number:"))
b = int(input("Enter your first number:"))

# create if statement
if b > a:
    print("Your 2nd number is greater than your first number")

# elif statements are read first when the program runs
elif a == b:
    print("Your first number is equal to your second number")

# else statements are default to the opposite of the if statement (there's no condition needed)
# it's read last, and will undertaken  by intepretor ONLY if both the if and elif statements aren't true
else:
    print("Your first number is greater than your second number")

    
    