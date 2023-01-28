# creating a sqaure pattern using an input function

# declaring variable for user input
number = int(input("Enter total rows: "))

for x in range(number):     # prints rows
    for y in range(number): # prints columns
        print("*", end=" ")
    print()  # 

