# this is the example of testing without any test runners...so this still works, but it's different to what you know as a unit test.
# so now you can try with the unit test style, let's go
# i was now just tired are you mad...but it's making sense you
# i'm going to master this 
def test_sum():
    # sum is a built in function that adds all the numbers in a list
    assert sum([3,3]) == 6, "Should be 6"
    
if __name__ == "__main__":
    test_sum()
    print("Everything passed")

'''
assert sum([1,1,1]) == 6, "Should be 6"
bcos i asserted, if incorrect it will return an assertion error..
and after the comma...it will display the message
this will be displayed...
AssertionError: Should be 6

if the result was true it will return the statement...
"Everything passed"
'''

# this is the simple way of checking tests, if there's more than
# one fail, test runners will be helpful

# A TEST RUNNNER IS A SPECIAL APPLICATION DESIGNED FOR RUNNING TESTS, CHECKING OUTPUT, AND GIVING TOOLS FOR DEBUGGING AND DIAGNOSING TESTS AND APPLICATIONS

# there are different test runners
'''
unittest is a build in test runner..
you also get nose or nose2 and pytest
'''

# let's try the unit test
