"""
PROBLEM STATEMENT 
Chocolate Feast

Little Bobby loves chocolate. He frequently goes to the favorite 5 & 10 store,
Penny Aunties to buy them. They are having a promotion at Penny Aunties. If
Bobby saves enough wrappers, he can turn them in for a free chocolate.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def chocolateFeast(n, c, m):
    """
    Parameters:
        n - money to be spent on the bar
        c = cost of each bar
        m = wrappers that can be turned in to receive a bar.
    Output:
        no of bars Bobby have eaten
    """
    choco = n // c
    wraps = choco

    while wraps >= m:
        choco += wraps // m
        wraps = wraps // m + wraps % m
    
    return choco


n = 15
c = 3
m = 2
print(chocolateFeast(n, c, m))