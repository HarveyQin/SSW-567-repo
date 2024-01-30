# -*- coding: utf-8 -*-
"""
@author: Hanbin Qin
"""

import unittest


def bogus_classifyTriangle(a, b, c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if a == 3 and b == 4 and c == 5:
        return 'Right'
    elif a == 3 and b == c:
        return 'Scalene'
    elif a == b == c:
        return 'Equilateral'
    else:
        return 'NotATriangle'


def classifyTriangle(a, b, c):
    # check if the inputs are all integer
    if not all(isinstance(side, int) for side in (a, b, c)):
        return "Input sides must be integers"
    # check if it is valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"

    # check if it is a equilateral triangle
    if a == b == c:
        triangle_type = "Equilateral"
    # check if it is a isosceles triangle
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    # check if it is a Scalene triangle
    else:
        triangle_type = "Scalene"

    # check if it is a right-angled triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        right_triangle = " and it is a right triangle"
    else:
        right_triangle = " and it is not a right triangle"

    return f"{triangle_type}{right_triangle}"


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c), sep="")


# The remainder of this code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(2.5, 3, 4), "Input sides must be integers")
        self.assertEqual(classifyTriangle(5, 3.2, 4), "Input sides must be integers")
        self.assertEqual(classifyTriangle(2, 3, 4.2), "Input sides must be integers")
        self.assertEqual(classifyTriangle(0, 0, 0), "Not a valid triangle")
        self.assertEqual(classifyTriangle(1, 1, 3), "Not a valid triangle")
        self.assertEqual(classifyTriangle(-2, 3, 4), "Not a valid triangle")
        self.assertEqual(classifyTriangle(999999999999999999999999999999, 3, 4), "Not a valid triangle")

    def testMyTestSet2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        # self.assertEqual(classifyTriangle(10, 15, 30), 'Scalene', 'Should be Isoceles') # bug test code
        self.assertEqual(classifyTriangle(5, 5, 5), "Equilateral and it is not a right triangle")
        self.assertEqual(classifyTriangle(3, 3, 4), "Isosceles and it is not a right triangle")
        self.assertEqual(classifyTriangle(3, 5, 6), "Scalene and it is not a right triangle")
        self.assertEqual(classifyTriangle(3, 4, 5), "Scalene and it is a right triangle")



if __name__ == '__main__':
    unittest.main(exit=False)  # this runs all of the tests - use this line if running from Spyder
    # unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line



