# printing hello world if a > b

"""# declaring variables
a = 50
b = 10

# if statement
if a > b:
    print("Hello World")
"""

# age limit (18 - 26)
# user input
age = (input("Enter your age: "))

# age limit using range
limit = range(18, 27, 1)

# if statement
if age == limit:
    print("Your age is suitable for the course.")
elif age > limit:
    print("Unfortunately, You are overage for this course.")
    print("Check your emails, we've sent alternative resources")
else:
    print("You are underage for the course.")
    print("Re-apply when you've reached 18 years old.")

# still not running