"""
Write a function that changes the value at given index i of a given list a_list to a given value new_value if the described conditions are met.

Modify a_list in place. No need to return anything!

Conditions

    If i is not a valid index of a_list, do nothing. If the value at a[i] is in all uppercase characters, do nothing. Otherwise, change the value at a[i] to new_value 

You answered
JUST NOW
"""

# # defining function
# def conditional_modify(a_list, i, new_value):
#     # Your code here
#     a_list, new_value = 0

#     for i in range(1, i):
#         if i in a_list != 0:
#             print("")
#         elif i in a_list.uppercase: 
#             print("")
#         else:
#             print(new_value)
        
# # Input handling, do not modify!
# a_list = input().split(" ")
# i = int(input())
# new_value = input()
# conditional_modify(a_list, i, new_value)
# print(a_list)

# imgInstructor solution
# Instructor Mbulelo Rasmeni


def conditional_modify(a_list, i, new_value):
    if i >= 0 and i < len(a_list) and not a_list[i].isupper():  # used if and statement
        a_list[i] = new_value


# Input handling, do not modify!
a_list = input().split(" ")
i = int(input())
new_value = input()
conditional_modify(a_list, i, new_value)
print(a_list)