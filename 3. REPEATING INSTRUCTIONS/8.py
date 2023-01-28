"""
Reverse the a given integer using a while loop
Use one of the following numbers to test your code: 123,456,789

Expected output:

123
Reverse Number 321 
"""

# # declare input variable
# num = [int(input())]

# reversed_num = num.reverse()

# # while loop
# while num != 0:
#     print("Reverse Number", reversed_num)
#     break

num = [int(input())]
reverse_number = num.reverse()

while num != 0: #Type in your code here
    print("Reverse Number ", reverse_number)
    break

""" instructor solution
num = int(input())
reverse_number = 0

while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Reverse Number ", reverse_number)
"""