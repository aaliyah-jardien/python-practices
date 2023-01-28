# Write a Python function to check whether a number falls between 3 and 9
# Please use a number between 1 and 10 to test your code

# defining function
# def test_range(n):
#     for i in range(3, 10):
#         if test < 3:
#             print("The number is outside the given range.")
#             break
#         elif test >= 3:
#             print(test, "is in the range")
#             break
#         elif test > 9:
#             print("he number is outside the given range.")
#             break

# # input variable 
# test = int(input("Enter a number"))

# # calling function
# test_range(test)

# Instructor solution
def test_range(n):
    if n in range(3,10):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
        
test = int(input("Enter a number"))
test_range(test)


"""
The % symbol is used in Python with a large variety of data types and configurations.
%s specifically is used to perform concatenation of strings together. It allows us
to format a value inside a string.
"""