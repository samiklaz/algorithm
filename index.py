"""
PROBLEM STATEMENT 
Encryption

An English text needs to be encrypted using the following Encryption scheme.

First the spaces are removed from the text, let L be the length of the text.

Then Characters are written into a grid, whose rows and columns has the
following constraint.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

from math import *

def encryption(s):
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    result = []

    for i in range(c):
        temp = []
        j = 0
        while i + j < n:
            temp.append(s[i+j])
            j += c
        print("temp ===  ", temp)
        result.append("".join(temp))

    return "".join(result)


s = "If man was meant to stay on the ground god would"
print(encryption(s))