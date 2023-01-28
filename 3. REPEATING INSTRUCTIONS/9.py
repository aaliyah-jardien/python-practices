"""Write code that iterates through and prints unlimited lines of STDIN until ~BREAK~ is seen.

Sample STDIN
The first line
The second line
The third line
~BREAK~

Sample STDOUT
The first line
The second line
The third line"""

#  when thr program runs and sees "break" then it must stop...exit

# data = ["The first line", 
# "The second line",
# "The third line",
# "~BREAK~"]

# for i in data:
#     if i == "~BREAK~":
#         break
#     print(data)

# use while loop not if statement
# Your code here!

while True:
    data = input()
    if data == "~BREAK~":
        break
    print(data)