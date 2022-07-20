"""
PROBLEM STATEMENT 
Merchant Sock

John works at a clothing store. He has a large pile of socks that he must pair by
color for sale. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2]. There
is one pair of color 1 and one of color 2. There are three odds socks left, one
of each color. The number of pairs is 2.

CONDITIONS

SAMPLE INPUT 
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-seperated integers describing the colors ar[i]
of the socks in the pile.

9
10 20 20 10 10 30 50 10 20

SAMPLE OUTPUT 
Return the total number of matching pairs of socks that John can sell.
3

CONSTRAINT
"""

def sockMerchant(ar):
    count = 0
    d = {}

    for i in ar:
        d[i] = d.get(i, 0) + 1

    for i in d.keys():
        count += d[i] // 2

    return count

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(ar))
