#  a simple program with primitive types
# Let's use the primitive types to create a simple program that can hold information about a cylindrical teapot.
# Run the following program. You don't have to enter the text after the #. These are comments and do not get executed. The comments are given to help you understand how python is working with the types in each line.

# declaring variables
name = input("Teapot name: ")
greeting = "I'm a little teapot and my name is " + name

weight = 80
print("I weigh " + str(weight) + "when I'm empty")  # weight, the int, is converted to string

weight = weight + 400

print("I now weigh " + str(weight) + "when full")

