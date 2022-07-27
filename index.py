"""
PROBLEM STATEMENT 
Given an array of integers, find and print the maximum number of integers
you can select from the array such that the absolute difference between
any two of the chosen integers is less than or equal to 1.

For example, if your array is a = [1,1,2,2,4,4,5,5,5], you can create two
subarrays meeting the criterion; [1,1,2,2] and [4,4,5,5,5]. The maximum
subarray has 5 elements.

CONDITIONS

SAMPLE INPUT 
The first line contains a single integer n, the size of the array a.
6
4   6   5   3   3   1

SAMPLE OUTPUT 
3

CONSTRAINT
2 <= n <= 100
0 <= a[i] < 100
The answer will be >= 2
"""
from collections import Counter

def pickingNumbers(a):
    arr = Counter(a)
    maxnum = 0

    for i in range(100):
        maxnum = max(maxnum, arr[i] + arr[i+1])
    return maxnum

a = [4, 6, 6, 6, 5, 3, 3, 1,]
print(pickingNumbers(a))