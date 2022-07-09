"""
PROBLEM STATEMENT 
Alice and Bob each created one problem for Hackerank. A reviewer rates
the two challenges awarding price on a scale from 1 to 100 for three
categories: problem clarity, originality and difficulty.

Rating for Alice Challenge -- a = (a[0], a[1], a[2])
Rating for Bob Challenge   -- b = (b[0], b[1], b[2])

CONDITIONS
if a[i] > b[i], then Alice is rewarded with a point 
if a[i] < b[i], then Bob is rewarded with a point 
if a[i] = b[i], then neither of them receives a point 

SAMPLE INPUT 
a = [1 2 3]
b = [3 2 1]

SAMPLE OUTPUT 
result = [1 1]

CONSTRAINT
"""

from array import array

def compareTriplets(a, b):
    alice = bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob

a = array('i', [1, 2, 3])
b = array('i', [3, 2, 1])

print(compareTriplets(a, b))