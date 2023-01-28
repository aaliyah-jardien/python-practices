"""
Use a for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

Make sure that the user entered input for variable n and k are 5 (inputs)

"""

# # wrong
# n = int(input(5))
# k = int(input(5))

# for i in range(0,6):
#     for j in range(0,-1):
#         print(j,end='0')
#         range += -1
#     print() # returns 5


n = int(input("Enter number:"))
k = int(input("Enter number: "))

for i in range(0, n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()