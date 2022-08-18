"""
PROBLEM STATEMENT 
Non Divisible Subset

Given a set of distinct integers, print the size of a maximal subset of
S where the sum of any 2 numbers in S^4 is not evenly dvisible by k. For 
example, the array S = [19, 10, 12, 10, 24, 25, 22] and k = 4. One of the 
array that can be created is S^4[0] = [10, 12, 25]. Another is S^4[1] = [19, 22, 24].
After testing all permutations, the maximum length solution of array has 3 elements.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def nonDivisibleSubset(k, s):
    """
    Parameters:
        k: an integer
        s: an array of Integer
    Result:
        Returns an integer representing 
        the length of the subste
    """
    remainder = [0] * k
    
    for i in s:
        remainder [i % k] += 1

    maxnum = 0
    maxnum += min(remainder[0], 1)

    if k % 2 == 0:
        maxnum += min(remainder[k//2], 1)

    for i in range(1, k//2 + 1):
        if  i != k-i:
            maxnum += max(remainder[i], remainder[k-i])
    
    return maxnum


s = [19, 10, 12, 10, 24, 25, 22]
k = len(s)
print(nonDivisibleSubset(k, s))