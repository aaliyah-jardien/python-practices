# We can use filter() to get a list of words ending in d:
words = ['a','abcd','abcde','ab','abc']
d_words = list(filter(lambda word: word.endswith('d'), words))

print(d_words) #['abcd']