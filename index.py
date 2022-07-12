"""
PROBLEM STATEMENT 
Given 5 positive integers, find the minimum and maximum values that 
can be calculated by summing exactly four of the 5 integers. Then
print the respective minimum and maximum values as a single line 
of the two space-seperated long integers.

CONDITIONS


SAMPLE INPUT 
arr = [1, 3, 5, 7, 9]

SAMPLE OUTPUT 
1 + 3 + 5 + 7 = 16
3 + 5 + 7 + 9 = 24

16 24

CONSTRAINT
1 <= arr[i] <= 10^9
"""

# First Solution
def miniMaxSum1(arr): 
    print(sum(arr) - max(arr), sum(arr) - min(arr))

# Second solution
def miniMaxSum(arr): 
    s = 0 
    minimum = 999999999999999
    maximum = 0

    for i in range(len(arr)):
        s += arr[i]
        minimum = min(minimum, arr[i])
        maximum = max(maximum, arr[i])
    print(s-maximum, s-minimum)

arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)