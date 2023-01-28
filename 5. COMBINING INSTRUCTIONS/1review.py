"""
1.
Generate a Python list of all the even numbers between 4 to 30

Expected Output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

Generate a Python list of all the even numbers between 4 to 30

Expected Output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
"""

# range(start=4, stop,30, step=2)

# decalring variables
num1 = int(input("Enter start number"))
num2 = int(input("Enter end number"))
num3 = int(input("Enter step number"))

print(list(range(4, 30, 2)))

# i did this :)

"""
instructor solution

num1 = int(input("Enter start number"))
num2 = int(input("Enter end number"))
num3 = int(input("Enter step number"))
print(list(range(num1, num2, num3)))
"""

# i see what they did there, instead of inserting numbers as the range, you can also insert variable names
# cool