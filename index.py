"""
PROBLEM STATEMENT 
Given a square matrix, calculate the absolute difference between 
the sum of its diagonals

CONDITIONS


SAMPLE INPUT 
1   2   3
4   5   6
9   8   9

SAMPLE OUTPUT 
1 + 5 + 9 = 15
3 + 5 + 9 = 17
|15 - 17| = 2

CONSTRAINT
"""

def diagonalDifference(arr, n):
    leftDiag = rightDiag = 0

    for i in range(0, n):
        leftDiag += arr[i][i]
        rightDiag += arr[i][n-1-i]
    return abs(leftDiag - rightDiag)


n = 3
arr = [
        [11, 2, 4], 
        [4, 5, 6], 
        [10, 8, 2]
      ]

print(diagonalDifference(arr, n))
