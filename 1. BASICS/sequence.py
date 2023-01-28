# Sequence Types: list :), tuple :), range :)
# lists
# storing mulitple items in one variable
# uses sqaure brackets [] L
# lists are ordered and changeable & allows duplicate members

# index...starts with 0, 1, 2, 3
# declaring variable called the_list
# putting strings in a list
the_list = ["apple", "banana", "cherry", "orange"]

# print the list
print(the_list)

# use length function to determine amount of items in a list
print(len(the_list)) # returns 4 items in the list

# any data type can be put in a list
num_list = [1, 5, 7, 9, 3]
# determining the data type of the list in the variable
print(type(num_list))

# a list can also contain different data types
diff_list = ["abc", 35, True, 40, "male"]

print(diff_list)
# printing total number of items in diff list
print(len(diff_list))

# calling one thing back from a list
fruits = ["apples", "bananas", "peaches", "grapes"]

print(fruits[2]) #...calls back peaches

# changing a value from apples to oranges
fruits[0] = "oranges"

# using append method to add to fruits list
fruits.append("pineapples")

# removing bananas from the list
fruits.remove("bananas")

# using insert method to add new fruit in a specific place in the list
# adding lemon as the second item in the fruit list
fruits.insert(1, "lemon")

# use negative indexing to print the last item in the list
print(fruits[-1])

print(fruits)

# declaring variable as fruit list
# Use a range of indexes to print the third, fourth, and fifth item in the list. 
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit_list[2:5]) #prints cherry, orange, kiwi

# adding multiple items from a diffrent variable to the 1st variable
fruit_salad = {"apple", "banana", "cherry"}

more_fruits = ["naartjie", "guava", "grapes"]

fruit_salad.update(more_fruits)

# removing cherry from the list
fruits.remove("cherry")

# discarding kiwi from the list
fruits.discard("kiwi")

print(fruit_salad)



# tuples
# stores multiple items in a single variable
# written with round brackets () tttt
# indexed from 0, 1, 2, 3
# ordered(can't change the order), UNchangeable(can't add or remove items) and allows duplicate values(since indexed from 0)

the_tuple = ("apple", "banana", "cherry", "orange", "apple", "banana")

print(the_tuple)

# finding the length of the tuple
print(len(the_tuple)) #returns 6

# creating a tuple with just one item
# must contain a comma ,
one_tuple = ("banana",)
print(one_tuple)

# determing type of collection items are stored in
print(type(one_tuple))

# tuples storing strings
str_tuple = ("apple", "banana", "orange")

# tuple storing integers
num_tuple = (1, -3, 5, -7, 9, 3)

# tuple storing booleans
boo_tuple = (True, False, False )

# single tuple containing different data types
diff_tuple = ("abc", 34, True, 40, "male", False)

# using tuple constructor to create tuples
this_tuple = tuple(("apple", "banana", "orange"))

print(this_tuple)

# RANGE
# returns a sequence of numbers
# starts from 0 and increments by 1 (w the previous number)

# syntax of range
# range(start, stop, step)

# start = a number specifying at which positon to start *optional
# stop = specifying at which position to stop
# step = number specifying incrementation, default is 1

# creating a sequence of number from 0 to 5
# printing each number in the sequnce
my_range = range(6)

for num in my_range:
    print(num) # print from 0 to 5

# creating sequnce of numbers from 3 to 5
# declaring variable
the_range = range(3, 6)

for num in the_range:
    print(num)

# creating sequence of number from 3 to 19, icrement by 2 instead of 1
new_range = range(3, 20, 2)

for num in new_range:
    print(num)



















