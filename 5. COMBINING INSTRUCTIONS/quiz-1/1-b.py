# #Write a Python function to find the Max of three numbers.
# Use the following as test input in STDIN

# Input:

# 1
# 8
# 6

# output
# Please enter num1
# Please enter num2
# Please enter num3
# The max of the three numbers is: ....

# You missed this question.
# You answered

# defining function
# def max_of_three( x, y, z ):
#     if num1 > num2:
#         print(num1)
#     elif num2 > num1:
#         print(num2)
#     elif num1 > num3:
#         print(num1)
#     elif num3 > num1:
#         print(num3)
#     elif num2 > num3:
#         print(num2)
#     elif num3 > num2:
#         print(num3)
        
    
# num1 = int(input("Please enter num1"))
# num2 = int(input("Please enter num2"))
# num3 = int(input("Please enter num3"))

# print("The max of the three numbers is:",max_of_three(num1, num2, num3))


# Instructor solution

# function finding biggest number between first 2 numbers
def max_of_two( x, y ): # x and y are the parameters
    if x > y:
        return x
    return y

# function finding biggest number between previous functions answer with the third number
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
    
num1 = int(input("Please enter num1"))
num2 = int(input("Please enter num2"))
num3 = int(input("Please enter num3"))

print("The max of the three numbers is:",max_of_three(num1, num2, num3))

# you can run a function that can be used in another function
# especially when it can be broken into steps...with a flow
