# RECURSION EXAMPLE

# the recursion ends when the condition is not greater than 0 (when it is 0)

# defining function
def try_recur(k):   # use k variable as the data
    # if statement
    if (k > 0):
        result = k + try_recur(k - 1)   # which decrements(-1) everytime we recurse
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")

# calling function
try_recur(4)    # parameter is k...the value is 4...k = 4
                # returns 1, 3, 6, 10