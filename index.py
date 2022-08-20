"""
PROBLEM STATEMENT 
Organizing Containers

David has several containers each with a number of balls in it. He has
just enough containers to sort each type of ball he has into his own
container. David wants to sort the balls using his sort method.

As an example, David has n=2 containers and 2 different types of balls, 
both of which are numbered from 0 to n-1 = 1. The distribution of ball
types per container are described by n * n matrix of integers. For e.g
consider the following diagram for M = [[1, 4], [2, 3]]Organizing Containers

David has several containers each with a number of balls in it. He has
just enough containers to sort each type of ball he has into his own
container. David wants to sort the balls using his sort method.

As an example, David has n=2 containers and 2 different types of balls, 
both of which are numbered from 0 to n-1 = 1. The distribution of ball
types per container are described by n * n matrix of integers. For e.g
consider the following diagram for M = [[1, 4], [2, 3]]

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def organizingContainers(container):
    """
    Parameters:
        container: A two dimensional array of integers
        that represents the number of balls of each 
        color in each container
    Output:
        string; either possible or impossible
    """
    n = len(container)
    row = [0] * n
    col = [0] * n

    for i in range(n):
        for j in range(n):
            row[i] += container[i][j]
            col[i] += container[j][i]

    if sorted(row) == sorted(col):
        return "Possible"
    return "Impossible"

