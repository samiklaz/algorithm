"""
PROBLEM STATEMENT 
Supposed you're given two arrays of integers, determine all 
integers that satisfies the following conditions

CONDITIONS
1.  The element in the first array are all factors of the 
    integer being considered.
2.  The Integer being considered is a factor of all elements
    of the second array

SAMPLE INPUT 
a = [2, 4]
b = [16, 32, 96]

SAMPLE OUTPUT 
3

EXPLANATION
2 and 4 evenly divides into 4, 6, 12, 16
4, 8, 16 divides evenly into 16, 32, 96
4, 8, 6 are the only 3 numbers for which element of a is a
factor and each is a factor of all elements of b.
"""

from functools import reduce

def getTotalX(a, b):
    def gcd(a, b):
        print("b === ", b)
        print("a ==",  a)
        if b==0:
            return a
        return gcd(b, a%b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    l = reduce(lcm, a)
    g = reduce(gcd, b)

    s = 0 
    for i in range(l, g+1, l):
        if g % i == 0:
            s+= 1
    return s

a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))