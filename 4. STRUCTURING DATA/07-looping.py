# List, dictionary, tuple, and set items may be accessed using a for loop
list = ["fish", "dog", "cat"]
tuple = ("fish", "dog", "cat")
dictionary = {
    'fish': 'Bubbles',
    'dog': 'Spot',
    'cat': 'Frisky',
}
set = {"fish", "dog", "cat"}

print("List:")
for item in list:
    print(item)
print()

print("Dictionary:")
for item in dictionary:
    print(item)
print()

print("Tuple:")
for item in tuple:
    print(item)
print()

print("Set:")
for item in set:
    print(item)