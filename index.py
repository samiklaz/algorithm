"""
PROBLEM STATEMENT 
Kaprekar Numbers

A modified Kaprekpar number is a positive whose number with a special property.
If you square it, then split the number into two integers, you would have the 
same value you started with.

Given two positive integers p and q, write a program to print the modified
kaprekpar numbers in the range between p and q inclusive.
CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def KaprekarNumbers(p, q):
    result = []
    for i in range(p, q+1):
        sqr = str(i**2)
        n = len(sqr)

        print("sqr[:n//2 == ", n//2)

        if i == 1:
            result.append(i)
        elif n > 1 and i == int(sqr[:n//2]) + int(sqr[n//2:]):
            result.append(i)

    if len(result) == 0:
        print("invalid range")
    else: 
        print(*result)

KaprekarNumbers(2, 3)