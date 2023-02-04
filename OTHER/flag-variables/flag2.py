"""
Flag variable is used as a signal in programming to let the program know that
a certain condition has met. It usually acts as a boolean variable indicating
a condition to be either true or false. 
"""

# Example 1: Check if an array has any even number.

# we initialize a flag variable as flase, then traverse the array
#  as soon as we find the element
# we set flag as true and break the loop
#  finally we return flag


# check if array has even numbers

num_list = [10, 2, 3, 5, 4, 8]

def is_even(num_list):
    flag = False

    for num in range(len(num_list)):
        if num_list[num] % 2 == 0: # use != for is even
            flag = True
            print("The list has even numbers")
            break
    print(flag)
is_even(num_list)

