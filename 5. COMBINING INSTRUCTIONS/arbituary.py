# ARBITUARY ARGUEMENTS
# arbituary - seeming to have been made or chosen by chance

# if you don't know the total number of arguements that will
# be passed through thr function you can use * before the parameter name in the function definition

# the function will receive a tuple of arguements, and access the items accordingly


# example, the number of arguements is unknown
# using * before the parameter name

# defining function
def myFunction(*kids):
    print("The youngest child is " + kids[1])   # starts from 0,1,2 ....stating which arguement to print ONLY

myFunction("Emly", "Tobias", "Leo")     # arguement values are the kids names

# Arbitrary Arguments are often shortened to *args in Python documentations.