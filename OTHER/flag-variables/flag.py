# flags

"""
can be a bool or int
defined with a value until a condition is met
then the value changes :)
"""

# list of numbers, squared,,,check is value is > 500
numbers = [5, 3, 6, 7, 4, 2, 4, 3]

num = 0 
square = 10

success = False # flag var

while num < len(numbers):
    if numbers[num] ** 2 > square:
        print(f"{numbers[num]}, sqaure is larger than, {square}")
        # if this condition is met then the flagged value changes
        success = True
        break
    print(f"{numbers[num]}, squared is not larger than, {square}")
    num += 1

if success:
    print(f"One of them was large enough!")

# if not success:
#   print(f"none not large enough!")