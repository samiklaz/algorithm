"""
PROBLEM STATEMENT 
Square

Watson likes to challenge Sherlock's math ability. He will provide a 
starting and ending value describing a range of integers. Sherlock
must determine the number of square integers within that range, inclusive
of the endpoints

For example, the range is a = 24 and b = 49, inclusive. There are three 
square integers in the range 25, 36 and 49.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

from math import *

def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


a = 24
b = 49
print(squares(a, b))
