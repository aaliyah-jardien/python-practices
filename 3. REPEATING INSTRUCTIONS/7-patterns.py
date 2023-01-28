"""Using the for loop, write a program to print the start pattern below
5 should be your user input in line 1 of your code
Click the image below to enlarge it"""

# declare variable
row = int(input())


for a in range(1, row + 1, 1):
    for b in range(1, a + 1):
        print("*", end=' ')
    print("\r")

for a in range(b, row-1):
    for b in range(a):
        print("*", end=' ')
    print("\r")

# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1

# # run loop 5 times
# for i in range(1, row+1, 1):

#     # Run inner loop i+1 times
#     for j in range(1, i+1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")