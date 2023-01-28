# RECURSION
# recursion is a defined function calling itself

#  you can loop through data to reach a result  

"""
The developer should be very careful with recursion as it can be quite easy
to slip into writing a function which never terminates, or one that uses excess
amounts of memory or processor power. However, when written correctly recursion
can be a very efficient and mathematically-elegant approach to programming.
"""

# defining function
def count(n):
    print(n)
    # if statement
    if n == 0:
        return          # terminates recursion
    else:
        count(n - 1)    # recursion call..calls function within itself

# calling function
count(5)                # prints 5, 4, 3, 2, 1