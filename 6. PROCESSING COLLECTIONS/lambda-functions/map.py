# As an example, we can use map() to get a list of the lengths of words from a list of words:
words = ['a','abcd','abcde','ab','abc']
lengths = list(map(lambda word: len(word), words))

print(lengths) #[1,4,5,2,3]