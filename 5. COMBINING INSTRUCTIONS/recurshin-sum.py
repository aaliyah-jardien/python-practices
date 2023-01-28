# RECURSION ....sum function

# defining variable
def sum(n):
    total = 0
    #  for loop
    for i in range(n + 1):
        total += total
    
    return total

result = sum(20)
print(result)