"""
Create a program where after the for loop has completed printing from 0 to any given number between 1 and 5,
it displays the message "Done" using the else block

For example, after a user enters 4 as input, the output should be the following:

0
1
2
3
4
Done!

"""

# # declaring variable
# num = 0 # index starting from 1

# # for loop
# for num in range(0, 5):
#     print(num)
# print("Done!")

# # got em

# declare variable
n = int(input())

for i in range(n+1):
    print(i)
else:
    print("Done!")