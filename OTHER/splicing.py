"""
string splicing

string = sequence of characters enclosed by quotes, it is immutable

splicing is another way of indexing
(you can use this to access any char or group of chars
you can use positive indices and negative indices)
"""

# when using positive indices the first char has the zero index until the end
# this is zero based

my_string = "ChamberOfReflection"

# positive indexing
x = my_string[2]
print(x)

# negative indexing the last char of the string and moves backwards
# each index is given index 1 less than it's previous char
x = my_string[-5]
print(x)

# capture a sub string, using square brackets
# starts from any index and ends at any index
# the last index is not included, exclusive
x = my_string[0:7]
x = my_string[9:19]
print(x)

# to capture a string from the starting value, to any index, we can leave the start index empty
x = my_string[:7] # normally starts from the beginning
print(x)

# to capture a string starting at any index to end at the last index, we can leave the last index empty
x = my_string[9:]
print(x)

# capture a substring from negative indices 
x = my_string[-10:-1]
print(x)

# capture a sub sequence from python string?