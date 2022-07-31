"""
PROBLEM STATEMENT 
Permutation Equation

Given a sequence of n integers, p(1), p(2),...,p(n) where each element is
distinct and satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n. Find 
the integer y such that p(p(y)) <=> x and print the value of y on a new 
line.

For example, assume the sequence p = [5, 2, 1, 3, 4]. Each value of x 
between 1 and 5, the length of the sequence is analyzed as follows:
[4, 2, 5, 1, 3]

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def permutationEquation(p):
    """
    Parameters:
        p: an array of integers.
    """
    result = []
    n = len(p)
    for i in range(1, n+1):
        result.append(p.index(p.index(i) + 1) + 1)
    return result


p = [5, 2, 1, 3, 4]
print(permutationEquation(p))