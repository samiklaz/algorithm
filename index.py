"""
PROBLEM STATEMENT 
Consider a staircase of size n. Write a program that prints a staircase
of size n.

CONDITIONS


SAMPLE INPUT 
A single integer, n denoting the sie of the staircase

SAMPLE OUTPUT 

CONSTRAINT
0 <= n <= 100
"""

def staircase(n):
    for i in range(1, n+1):
        s = "#" * i 
        print(s.rjust(n))

staircase(4)