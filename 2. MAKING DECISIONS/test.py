# test results
# checking if the candidate passed the test
# declaring variable to enter users test mark
result = int(input("Enter your test result: "))

# creating range
pass_mark = range(0, 101, 1)

if result <= 79:
    print("Your test mark wasn't successful. Try again next time.")
else:
    print("Well done! Your test mark was successful.")
# print positive msg
print("Keep doing your best!")

#  doesn't fully work, if i enter 1000 it says the mark was successful, should stop at 100