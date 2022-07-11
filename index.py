"""
PROBLEM STATEMENT 
Given an array of integers, calculate the fraction of its element that are 
positive, negative and are zeros. Print the decimal value of each fraction
on a new line.

CONSTRAINT 
0 < n <= 100 
-100 <= arr[i] <= 100

SAMPLE INPUT 
6
arr = [-4, 3, -9, 0, 4, 1]

SAMPLE OUTPUT 


Note
This introduces a precision problem but test cases are scaled to six decimal
place, though answers with absolute error of up to 10^-4 are accepted
"""

from array import array


def plusMinus(arr, n):
    pos = neg = zero = 0 
    for i in range(n):
        if arr[i] > 0:
            pos +=1 
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))

        


arr = array('i', [-4, 3, -9, 0, 4, 1])
plusMinus(arr, len(arr))