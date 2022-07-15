"""
PROBLEM STATEMENT 
Lily has a chocolate bar that she wans to share with Ron for his birthday. 
Each of the squares has an integer on it. She decides to share a contiguous
segment of the bar selected such that the length of the segment matches Rom's
birth month and the sum of the integers on the square is equal to his birth 
day. You must determine how many ways she can divide the chocolate.

For e.g, the chocolate bar ha an array s = [2, 2, 1, 3, 2], she wants to find 
segments summing to Rom's birthday, d= 4 with a length equaling his birth 
month m=2. In this case, there are 2 segments meeting her criteria 
[2, 2] and [1, 3]

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def birthday(s, d, m):
    count = 0 
    total = sum(s)

    print("total here == ", total)
    print("d here == ", d)

    if total == d:
        count += 1 

    # sliding window
    for i in range(m, len(s)):
        total += s[i]
        total -= s[i-m]
        if total == d:
            count += 1
    return count