# else in for loop
# executes bloack of code when loop is finished

# print all number from 0 to 5
# print message when loop ended

for num in range(6):
    print(num)
else:
    print("Finally finished!")

#  else won't work if the loop is stopped by a break statement

for num in range(6):
    if num == 3:
        break
    print(num)
else:
    print("Finally finished!")