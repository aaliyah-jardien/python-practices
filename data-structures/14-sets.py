"""
{}
"""

# changing list item to a set
fruits = ["apples", "oranges", "tomatoes"]
fruits = set(fruits)

# shorter way of specifiying
veggies = set(["potaoes", "onions", "tomatoes"])
print(veggies)

# set-based operations

# checking similar items frmo both set
fruit_and_veggie = fruits.intersection(veggies)
print(fruit_and_veggie) # gets item from both sets

# checking difference from veg in fruit
pure_veggies = veggies.difference(fruits)
print(pure_veggies) # items in veggie set, that's not in fruit
