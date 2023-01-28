# unittest
# has a testing framework and a test runner
# requires...
# put tests into classes as methods
# you use a series of special assertion methods

#IMPORT UNITTEST FROM THE STANDARD LIBRARY'''
import unittest

#CREATE A CLASS CALLED TestSum THAT INHERITS FROM THE TESTCASE CLASS'''
class test_sum(unittest.TestCase):

#CONVERT THE TEST FUNCTIONS INTO METHODS BY ADDING SELF AS A FIRST ARGUEMENT'''
    def test_sum(self):
        #CHANGE THE ASSERTIONS TO USE THE SELF.ASSERTEQUAL() METHOD ON THE TESTCADE CLASS'''
        self.assertEqual(sum([1,2,3]), 6, "Should be 6") # square brackets cos it's list

def test_sum_tuple(self):
        self.assertEqual(sum(2,2,2), 6, "Should be 6") # brackets cos it's a tuple

#CHANGE THE COMMAND-LINE entry point to call unittest.main()'''
if __name__ == "__main__":
    unittest.main()
c  