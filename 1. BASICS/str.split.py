txt = "hello* my name is Peter* I am* 26 years old"

x = txt.split("* ")

print(x)

# separates items in a list into a separate strings

# Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 2, will return a list with 3 elements!
x = txt.split("#", 2)

print(x) 