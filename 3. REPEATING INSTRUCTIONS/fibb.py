#  note: zero is sometimes not mentioned

# create a fibonacci function
# the first 2 digits is 0&1...and the index is 0&1
def fibonacci(i):
    if i == 0:
        return 0

    elif i == 1:
        return 1
        
    else:
        # return sum of 2 digits that came before
        # return function with equation
        return fibonacci(i-2) + fibonacci(i-1)
        
# convert the num into string
# converted_num = str(fibonacci)

# run sequence
# calling the nth number of the sequence
# print(fibonacci(9))

# running program in for loop
for x in range(4):
    print(fibonacci(x))

    # appending?