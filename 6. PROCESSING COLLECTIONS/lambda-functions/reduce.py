# And we can use reduce() to get a total character count for all the words in a list:
from functools import reduce

words = ['a','abcd','abcde','ab','abc']
lengths = list(map(lambda word: len(word), words))
char_count = reduce(lambda len1, len2: len1 + len2, lengths)

print(char_count) #15