# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# ARCITUARY KEYWORD ARGUEMENTS
#  **kwargs

#  if you don't know how many keywords arguements will pass through your function, then add ** before the parameter name

# the function will receive a dictionary of arguements, then access the items accordingly

#  defining function
def myfunction(**kid):
    print("His last name is " + kid["lname"])

#  calling function
myfunction(fname = "Tobias", lname = "Bond")

# a parameter is a placeholder/variable for the arguements (holds the object, items VALUE)

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.