"""
Using the for loop, write a program to print the start pattern below
5 should be your user input in line 1 of your code
Click the image below to enlarge it
*
**
***
****
*****
****
***
**
*
"""

# declare variables
# prints number of rows
rows = int(input())

for a in range(1, rows + 1):    # a prints number of rows
    for b in range(1, 1 + a):   # b prints number of columns
        print("*", end=" ")
    print("\r")

for b in range(b, rows - 1):
    for b in range(a):
        print("*", end=" ")
    print("\r")