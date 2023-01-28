# declaring variables
# turning the score into an integer, so any other input that's not a number won't be accepted
test_score = int(input("Please enter your test score:"))

# if the condition is true
if test_score == 100:
    print("Excellent work!")
elif test_score >= 80:
    print("Well done!")
elif test_score <= 50:
    print("Good job, but there's room for improvement!")

else:
    print("You can do better next time!")
