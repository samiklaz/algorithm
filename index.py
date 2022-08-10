"""
PROBLEM STATEMENT
Find digits
An integer d is a divisor of an integer n if the remainder of n / d = 0.
Given an integer, for each digit that makes up the integer determine 
whether it is a divisor. Count the number of divisor occuring within the
integer. 

CONDITIONS

SAMPLE INPUT 
The first line is an integer, t, indicating the number of test cases. The 
t subsequent lies each contain an integer, n

2
12
1012

SAMPLE OUTPUT 
2
3

CONSTRAINT
"""

def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            count += 1

    return count

n = 1012
print(findDigits(n))