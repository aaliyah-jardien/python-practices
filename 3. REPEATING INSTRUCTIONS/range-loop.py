# RANGE LOOP
# loops through code a specified number of times

# range() returns a sequnce of numbers starting from 0 by default
#  increments by 1, defualt
#  ends at a specific number

"""
for num in range(6):
    print(num) # prints 0, 1, 2, 3, 4, 5"""


# using the start parameter
for num in range(2, 6):
    print(num) #prints 2,3,4,5

# range(start, stop, step)

# # using step parameter, incremeting sequence by 3
# for num in range(2, 30, 3):
#     print(num) 