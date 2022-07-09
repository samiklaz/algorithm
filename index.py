"""
PROBLEM STATEMENT 
Calculate and print the sum of the elements in an array.
Keeping in mind that some integers would be long. 

CONDITIONS


SAMPLE INPUT 
5 
1000000000 10000003

SAMPLE OUTPUT 
sum of the input element

CONSTRAINT
1 <= n <= 10
0 <= ar[i] <= 10^10
"""

from array import array

def aVeryBigSum(ar):
    return sum(ar)

ar = array('i', [1000000000, 10000003, 1000000000, 10000003])

print(aVeryBigSum(ar))