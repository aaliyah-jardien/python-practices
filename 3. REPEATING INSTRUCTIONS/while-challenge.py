# Using a while loop, print the first 10 numbers (1 to 10)
# Note: 1 should be the user input since it is the first number printed out
# Expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# #  given method
# i for input

#  i've added a string to state "please enter your number" but when i ran the code it went beyond the expected answer
i = int(input())

while i <= 10:
    print(i)
    i += 1

