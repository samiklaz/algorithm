"""
PROBLEM STATEMENT 
Fair Ration

You are a benevolent ruler of Rackhacker castle, and today you're distributing
bread. Your subjects are in a line, and some of them already have some loaves.
Times are hard and your castle's food stocks are dwindling, so you must distribute
as few loaves a possible according to the following rules:

1.  Everytime you give a loaf of bread to some person i, yolu mut also give a loaf
    of bread to the person immediately infront or behind the, in the line.
    (i.e., persons i=1 or i-1).

2.  After all the bread is distributed, each person must have an even number of
    loaves.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def fairRations(B):
    breads = 0
    n = len(B)

    for i in range(n-1):
        if B[i] % 2 == 1:
            print("num = ", B[i])
            breads += 2
            B[i+1] += 1
    
    if B[n-1] %2 == 1:
        return "NO"
    else:
        return breads



B = [4, 5, 3, 7]
print(fairRations(B))