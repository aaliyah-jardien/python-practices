# lists and tuples allow duplication. Dictionary and set items are unique
list = [1, 1, 1]
tuple = (1, 1, 1)
dictionary = {1: 'one', 1: 'one', 1: 'one'}
set = {1, 1, 1}

print("list:", list)
print("tuple:", tuple)
print("dictionary:", dictionary)
print("set:", set)

# Sets may be used to remove duplication found in other data structures
list = [1, 1, 1]
tuple = (1, 1, 1)

print("list:", list)
print("set:", set(list))

print("tuple:", tuple)
print("set:", set(tuple))