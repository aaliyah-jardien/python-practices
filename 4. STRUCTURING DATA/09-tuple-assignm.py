# Python supports having a tuple on the left side of an assignment statement. This allows you to assign more than one variable at a time
x = 1
y = 2
print(x, y)

x, y = y, x
print(x, y)
