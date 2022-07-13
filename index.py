"""
PROBLEM STATEMENT 
You are given 2 Kangaroos on a number line ready to jump in the 
positive direction (i.e towards infinity).
1.  The first kangaroo starts at location x1 and moves at
    rate v1 meters per jump.
2. The second kangaroo starts at location x2 and moves at
    rate v2 meters per jump.

We have to figure out a way to get both kangaroos at the same
location at the same time as part of the show. If possible,
return YES, otherwise return NO.

CONDITIONS

SAMPLE INPUT 
A single line of four space seperated integers denoting the
respective values of x1, v1, x2, v2

0 3 4 2

SAMPLE OUTPUT 
Print YES if they land on the same location and print No if 
they dont.

CONSTRAINT
0 <= x1 < x2 <= 10000
1 <= v1 <= 10000
1 <= v2 <= 10000
"""

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2-x1) % (v1-v2) == 0 or v1 == v2 and x2 == x1:
            return "YES"
        else:
            return "NO"


x1, v1, x2, v2= 0, 3, 4, 2

print(kangaroo(x1, v1, x2, v2))