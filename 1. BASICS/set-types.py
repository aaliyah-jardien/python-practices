# SETS
# stores multiple items in a variable
# unordered(appears in any order), unchangeable(can't change, but you can add or remove items), unindexed, no duplicate values
# appears in a different order everytime it's used
# can't be referred to by an index or key
# uses curly braces {} fancy like dictionaries

# declaring variable that contains items in a set
uh_set = {"apple", "banana", "grape", "apples"}

print(uh_set) # no duplicates - doesn't print duplicate values

# finding the length of set
print(len(uh_set))

# sets can contain any data type
# set of string values
str_set = {"apple", "banana", "orange"}

# set of integer values
num_set = {0, 9, -5, 33}

boo_set = {False, True, False}

diff_set = {"abc", 34, True, 40, "male"}

# finding data type
print(type(diff_set))

# adding to set

# declare which variable you want to add to w the add function
# add()
str_set.add("granadilla")

print(str_set)

# remove from set
#  remove()
str_set.remove("banana")
print(str_set)

# FROZEN SETS
# elements of the frozen set remain the same after creation.
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
