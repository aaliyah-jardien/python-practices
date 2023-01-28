# comparing variables

# declare variable for name input
name = input("Enter name:")

# declare variable for letter count
letter_count = len(name)

#  if and elif and else statements
if letter_count < 3:
    print("Minimum characters allowed 3.")
elif letter_count > 50:
    print("Maximum characters allowed 50.")
else:
    print("Name looks good!")

# when i properly learn recursion, i'll come back to this and
# loop through the if and else statement so that the user MUST
# input the right name format. yah :)