"""
PROBLEM STATEMENT 
You are given an array of n integers.
ar = [ar[0], ar[1], ...., ar[n-1]], and a positive integer, k. Find
and print the number of (i, j) pairs where i < j and ar[i] + ar[j] 
is divisible by k.

For example, ar = [1, 2, 3, 4, 5, 6] and k=5. Our three pairs meeting
the criteria are [1, 4], [2, 3] and [4, 6]

CONDITIONS

SAMPLE INPUT 
The first line contains 2 space-seperated integers, n and k. The second 
line contains n space-seperated integers describing the values of
ar[ar[0], ar[1], ...., ar[n-1]]

SAMPLE OUTPUT 

CONSTRAINT
2 <= n <= 100

"""

def divisibleSumPairs(n, k, ar):
    count = 0 
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


ar = [1, 2, 3, 4, 5, 6]
k= 5

print(divisibleSumPairs(len(ar), k, ar))