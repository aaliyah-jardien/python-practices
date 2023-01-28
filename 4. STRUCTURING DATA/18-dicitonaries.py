car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# get method
# print the value of the "model" key of the car dictionary.
print(car.get("model"))

# changing values in a dictionary
car["year"] = 2020  # indexing which key to change
# i thought i can use the update method

# adding another key/value to the dictionary
car["color"] = "purple" # thought the add method should be used, but no
                        # so dictionaries probably doesn't require any methods
                        # just indexing and specifying like that

# nvm, it use use methods

# pop() method, removes a key/value from the dictionary
car.pop("model")

print(car)

# clear()
# this method clears the whole dictionary
car.clear()
print(car)