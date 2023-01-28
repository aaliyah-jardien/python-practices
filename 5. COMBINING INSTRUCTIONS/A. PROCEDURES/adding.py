# program adding numbers using functions

operation = input("(Plus,Minus,Multiply,Divide)\nWhich operation would you like?").lower

num1 = int(input("first number:")) # i called this in the function, but it was reading the parameters first, but the parameters didn't have a value, so i moved it out the function, so it can get a value first and then the parameters will also have values and execute the code
num2 = int(input("second number: "))


# step 1 : add two numbers
def add_numbers(num1, num2): # a, b are the parameters
    print(num1 + num2)

# step 2 : minus two numbers
def minus_numbers(num1, num2):
    print(num1 - num2)

# step 3 : multiply two numbers
def multiply_numbers(num1, num2):
    print(num1 * num2)

# step 4 : divide two numbers
def divide_numbers(num1, num2):
    print(num1 / num2)


def ask_operation():
    if operation == "plus":
        add_numbers(num1, num2) # when you call the function, you must include the parameters in the brackets, you can't pass through empty brackets
    elif operation == "minus":
        minus_numbers(num1, num2)
    elif operation == "multiply":
        multiply_numbers(num1, num2)
    elif operation == "divide":
        divide_numbers(num1, num2)

ask_operation(operation)