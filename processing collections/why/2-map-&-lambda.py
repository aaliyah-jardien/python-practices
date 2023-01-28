words = ['a','abcd','abcde','ab','abc']
lengths = list(map(lambda word: len(word), filter(lambda word: len(word)>1,words)))

print(lengths) #[4, 5, 2, 3]

# And it’s not just shorter, once you are more comfortable with the syntax of list 
# comprehensions and lambdas, you will realise they read a lot more like how we 
# describe collections in English.

"""
In short, the syntax can be defined as:
lambda x: x + 1
lambda var1, var2, .. : instruction that transforms var1, var2, etc
"""