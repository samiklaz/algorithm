"""
PROBLEM STATEMENT 
Cutting sticks

You are given a number of sticks with varying lengths, you will iteratively
cut the stick into smaller sticks, discarding the shortest pieces until there 
is no more left. At each iteration, you will determine the length of the shortest
stick remaining, cut that length from each of the longer stick and then discard 
all the pieces of the shortest length. When all the remaining sticks are the same
length, they cannot be shortened to discard them.

Given the length of n sticks, print the number of sticks that are left before each 
iteration until there are none left.

For example, there are n = 3 sticks of length arr = [1, 2, 3]. The shortest stick
length is 1, so we can cut that length from the longer two and discard the pieces of
length 1. Now our length are arr = [1, 2]. Again, the shortest stick is of length 1, so
we could cut that amount from the longer stick, and discard those pieces. There is only 
one stick left, arr = [1], so we can dsicard that stick. Our length are answers [3, 2, 1]

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

from collections import Counter

def cutTheSticks(arr):
    result = []
    n = len(arr)

    s = Counter(arr)

    for i in sorted(s.keys()):
        result.append(n)
        n -= s[i]

    return result




arr = [5, 2, 3]
print(cutTheSticks(arr))