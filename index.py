"""
PROBLEM STATEMENT 
Circular Array Rotation

John Walton knows of an operation called a right circular rotation on an
array of numbers. One rotation operation moves the last array element to 
the first element and shifts all the remaining elements right one. To 
test Sherlock' abilities, Watson provides Sherlock with an array of 
integers. Sherlock is to perform the rotation operatiob a number of times 
then determine the value of the element of a given position.

For each array, perform a number of right circular rotations and return the
value of the element as a given index.

For example, array a = [3, 4, 5], number of rotation, k = 2 and indices to
check ; m = [1, 2]

First we perform the two rotations:
[3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]

Now return the values from zero-based indices 1 and 2 as indicated in the m
array.

a[1] = 5
a[2] = 3

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def circularArrayRotate(a, k, queries):
    """
    Parameters:
        a: array to rotate
        k: an integer, the rotation count
        queries: 
    Output:
        returns an array of integers representing
        the values at the specified indices.
    """

    result = []
    n = len(a)
    k = k % n
    for q in queries:
        result.append(a[(n - k + q) % n ])
    return result



a = [3, 4, 5]
k = 2
queries = [1, 2]

print(circularArrayRotate(a, k, queries))