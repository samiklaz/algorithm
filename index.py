"""
PROBLEM STATEMENT 
Equalize Array

Karl has an array of integers. He wants to reduce the array until all 
remaining elements are equal. Determine the minimum number of elements
to delete to reach the goal.

For example, this array is = [1, 2, 2, 3], we see that we can delete 2
elements 1 and 3 leaving arr=[2, 2]. He could also delete both twos and 
either 1 or the 3. but would take 3 deletions. The minimum number of
deletions is 2. 

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

from collections import Counter

def equalizeArray(arr):
    """
    Parameters:
        - arr: an array of integers. 
    Output:
        - int: minimum number of
               deletions required
    """
    c = Counter(arr)
    return len(arr) - max(c.values())


arr = [1, 2, 2, 3]
print(equalizeArray(arr))