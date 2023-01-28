words = ['a','abcd','abcde','ab','abc']
lengths = []

for word in words:
    if len(word) > 1:
        lengths.append(len(word))

print(lengths) #4,5,2,3