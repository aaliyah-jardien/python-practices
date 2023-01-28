"""Create a program that accepts number 10 from the user and calculates the sum of all numbers between 1 and 10 (1+2+3+4+5+6+7+8+9+10) using a for loop. The output should be 55

Expected Output:

input: 10
Sum is:  55"""

"""# s: store sum of all numbers
# declare variables
s = 0 #index, starting from 0
n = int(input("Enter number: ")) #input number is 10

# run loop n times 
# stop: n+1 (because range never include stop number in result)

for i in range(0, 11):
    # add current number to sum variable
    for j in range(n+i):
        # print()
        print("Sum is: ", i+s)

    # for i in range(0, n+1):
    # for j in range(k-i,0,-1):
    #     print(j,end=' ')
    # print()"""

# declare variables
# sum: store sum of all numbers
sum = 0 # index from 0

# number input variable
# run loop num times
num = int(input("Enter number: "))

# stop: n+1 (because range never include stop number in result)

# range(0, n+1) ????

for i in range(0, num + 1):
    # add current number to sum variable
    # incremet sum
    sum += i
    # print(i) #prints from 0 until 10
    # sumb is sum of total range
    # for sumb in range(sum+i):
print("Sum is: ", sum)
