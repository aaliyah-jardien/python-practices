# BOOLEANS
# uses logical expressions
# based off conditions
# represents values whether it's True(1) or False(0)

#  multiple boolean expressions are like equations

#  uses logical operators "or" plus "and" not to combine expressions

# you ONLY want one thing to happen, if not it willperform whichever other action is applicable

# example, when applying yo wethinkcode......using application logic

'''
1. capture personal details
2. do application test
3. decisions - did you pass the test?
             - yes or no
        4. if yes (book bootcamp date)
        5. if no (re-apply next year)
the interpreter will execute whichever concept was true or false depending on the condition
'''

print(10 > 9)

print(10 == 9)

print(10 < 9)

#  printing a message when the condition is true or false
# declaring variables
a = 100
b = 50

#  if statement with condition
if b > a:
    print("B is greater than A")
elif a == b:
    print("A and B are equal")
else:
    print("A is greater than B")