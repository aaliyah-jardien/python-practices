"""
Write a program to create a function that takes two arguments as user input, name and age, and print their value.

Test your program by using as input one of the following at a time:

John
55

To get the output:

Name:

Age:

John 55

Make sure you DO NOT have any spaces after Name: and Age:

"""

# input variables
name = input("Name:\n")     # new line, place within inverted commas
age = input("Age:\n")

# defining function
def demo(name, age):    # paramters
    print(name+" "+age)
    return

# calling function
demo(name, age)

"""
instructor solution

name = input("Name:\n")
age = int(input("Age:\n"))
def demo(name, age):
    # print value
    print(name, age)

# call function
demo(name, age)
"""