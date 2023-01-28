"""Create a program to print multiplication table of a given number between 1 and 10

Given: 2

Expected output:
2
4
6
8
10
12
14
16
18
20
"""

#use this variable to accept user input
n = int(input("Enter number: "))
                            
for i in range(1, 11):      # stop: 11 (because range never include stop number in result)
    mult = n + n
    for j in range(1):
        print(n * i)



# yass :)

""" instructor solution
n = int(input())

# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 *i (current number)
    product = n * i
    print(product)
"""