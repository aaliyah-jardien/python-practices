"""
Using a while loop, create a program that counts the total number of digits in a number.
Use the following numbers to test your program: 123,4567,891011, 75869

Expected output
```
123
Total digits are: 3

4567
Total digits are: 4

891011
Total digits are: 6

75869
Total digits are: 5
``"""

"""
num = int(input(75869))
count = 0
while num(len):
    print("Total digits are:", count)"""

num = int(input())

count = 0

while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10
    # increment counter by 1
    count = count + 1
print("Total digits are:", count)