#  DEFAULT PARAMETER VALUE

# if we call the function without arguements, it uses the default value

#  defining function
def myfunction(country = "Your Mom"):     # country is the parameter
    print("I am from " + country)   # using default parameter

# calling functions
myfunction("Swedan")    # insert specific arguements when calling the function
myfunction("Japan")
myfunction("Dubai")
myfunction()        # does not have an arguements, uses the default parameters, arguement value
myfunction("Brazil")
