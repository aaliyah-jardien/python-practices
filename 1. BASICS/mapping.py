# DICTIONARIES
# stores data in key:value pairs
# ordered, changeable, no duplicates ()
# uses curly brackets, has keys and values {} fancy, has lots of specified key values of data {fancy}

# declaring variable with a dictionary collection
ay_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# calling data in the dictionary
print(ay_dict)

# printing a specific key from the dictionary
print(ay_dict["brand"])

# returning number of items in a dictionary
print(len(ay_dict))

# dictionaries can contain any data type
car = {
    "brand": "Toyota",
    "electric": False,
    "year": 2020,
    "colors": ["grey", "white", "black", "silver"]
}

# determining type of data in the collection
print(type(car))

# using get method to print the value of the "year" key of the car dictionary
print(car.get("year"))

# changing the year value from 2020 to 2019
car["year"] = 2019

print(car)