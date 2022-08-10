"""
PROBLEM STATEMENT 
Extra Long Factorial

The factorial of integer n, written as n! is defined as:
n! = n * (n - 1) * (n - 2) * .... * 3 * 2 * 1

Calculate and print the factorial of a given integer.

CONDITIONS

SAMPLE INPUT 
Consists of a single integer n

SAMPLE OUTPUT 

CONSTRAINT
"""

def extraLongFactorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


n = 30
print(extraLongFactorials(n))