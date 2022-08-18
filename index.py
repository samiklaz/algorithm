"""
PROBLEM STATEMENT 
Repeated string

Lilah has a string, s, of lowercase Eight letters that she repeated infinitely many times.
Given an integer, n, find and print th number of letter a's in the first n letters of Lilah's
infinite string.

For example, if a string s = 'abcac' and n=10, the substring we consider it abcacabcac, the 
first 10 characters of the infinite string. There are four occurences of a in the substring.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
1 <= |s| <= 100
1 <= n <= 10^12
For 25% of the test cases, n <= 10^6
"""

def repeatedString(s, n):
    """
    Parameters:
        s: a string to repeat
        n: number of characters to consider
    """
    total = 0
    for i in s:
        if i == 'a':
            total += 1

    total = n // len(s) * total

    for i in s[:n%len(s)]:
        if i == 'a':
            total += 1

    return total


s = 'abcac'
n = 10
print(repeatedString(s, n))