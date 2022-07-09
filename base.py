""" 
PROBLEM STATEMENT
Given an array of Integers, find the sum of its elements

SAMPLE INPUT 
Size of the array - 6
Array number      - 1 2 3 4 10 11

SAMPLE OUTPUT
31

CONSTRAINT
0 < n, ar[i] <= 1000
"""

from array import array

def simpleArraySum(ar):
    sum = 0
    for x in ar:
        sum += x 
    return sum

base_size = 6
arr = array('i', [])
size = int(input("Enter the size of the array: "))

if(size <= base_size):
    for x in range(0, size):
        num1 = int(input('Add number: '))
        arr.append(num1)
        print("Array sum = ", simpleArraySum(arr))
else:
    print(f"size must not be greater than {base_size}")

