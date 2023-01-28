words = ['a','abcd','abcde','ab','abc']
lengths = [len(word) for word in words if len(word)>1]

print(lengths) #[4, 5, 2, 3]

# using a loop but only in one line