"""
Write a function that converts an int num between 0-9 (inclusive) to its string equivalent (i.e., 1 -> "one").

Use an if/elif/else statement in your solution.

Sample STDIN/STDOUT
1 / one
"""

"""# defining function
def int_to_string(num):
    # Your code here
    if num == 0:
        print("zero")
    elif num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    elif num == 4:
        print("four")
    elif num == 5:
        print("five")
    elif num == 6:
        print("six")
    elif num == 7:
        print("seven")
    elif num == 8:
        print("eight")
    elif num == 9:
        print("nine")
    # elif num == 10:
    #     print(str("ten"))
    else:
        print("")
    
# Input handling, do not modify!
num = int(input())

print(int_to_string(num))"""

# IM SUPPOSED TO USE RETURN AND NOT PRINT

# so close 

def int_to_string(num):
    if num == 0:
        return "zero"
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    else:
        return ""

# Input handling, do not modify!
num = int(input())
print(int_to_string(num))

# instructor solution


# with functions, you can declare variable within the functions

# did you know...
# elif and else are both optional. The inclusion of one does not require the inclusion of the other.