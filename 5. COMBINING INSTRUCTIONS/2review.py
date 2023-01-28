"""
Write a function that returns "a is greater than b", "a is less than b", or "a is equal to b" depending on the values of two int input params a and b.

STDIN Format
a b (example 1 15 where a=1 and b=15)

Sample STDIN/STDOUT
1 3 / a is less than b
3 3 / a is equal to b
7 3 / a is greater than b
"""

# params is a special keyword that allows passing a variable number of parameters into a method. 

# my parameters is a and b


# defining function
def a_vs_b(a, b):   # parameters
	# your code here
	# if statement
    if a < b:
        print("a is less than b")
    elif a == b:
        print("a is equal to b")
    else:
        print("a is greater than b")

# Input handling, do not modify!
input_parts = input().split(" ")

a = int(input_parts[0])
b = int(input_parts[1])

print(a_vs_b(a, b))

"""
instructor solution

def a_vs_b(a,b):
	# your code here
	if a > b:
	    return "a is greater than b"
	elif a < b:
	    return "a is less than b"
	else:
	    return "a is equal to b"

# Input handling, do not modify!
input_parts = input().split(" ")
a = int(input_parts[0])
b = int(input_parts[1])
print(a_vs_b(a, b))
"""