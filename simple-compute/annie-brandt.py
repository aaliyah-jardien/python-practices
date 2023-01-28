#  STEP 1 Add Function
# Is this function doing just one thing?
# Is the name given to the function clear? If not, why do you think?
def operation(a,b,c):
    sum = a + b
    result = sum * c

# STEP 2: Break it down
"""
define a add function that does the a+b part, and a multiply function that multiples 2 parameters
"""
global a, b
a = input("1st number: ")
b = input("2nd number: ")

def sum(a, b):
    sum = a + b
    print(sum) 


def multiply(a, b):
    result = a * b
    c = result
    print(c)


sum(a, b) # when calling a function you should include the parameters as arguements, since it has value now
multiply(a, b)

# STEP 3: Use the functions
'''
We will use these two simpler functions in operation, so that operation does one thing: combine the results of two other functions.
'''
def operation(a,b,c):
    answer = a + b + c
    print(answer)
