"""
PROBLEM STATEMENT 
Minimum Distances

We define the distance between two array values as the number of indices between 
the two values. Given a, find the minimum distance between any pair of equal
elements in the array. If no such value exists, print -1.

For example, if a = [3, 2, 1, 2, 3], there are two matching pairs of values: 3 and
2. If the indices of the 3's  are i = 0 and j = 4, so their distance is d[i, j] = |j - 1| = 4.
The indices of the 2's and i = 1 and j = 3, so their distances are d|i,j| = |j-i| = 2.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""
import sys

def minimumDistances(a):
    distance = sys.maxsize
    print("max distance == ", distance)

    for i in range(len(a)):
        for j in range(i+ 1, len(a)):
            if a[i] == a[j]:
                distance = min(distance, j - 1)
    
    if distance == sys.maxsize:
        return -1
    else:
        return distance


a = [3, 2, 1, 2, 3]
print(minimumDistances(a))