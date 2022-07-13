"""
PROBLEM STATEMENT 
Sam house has an apple and orange tree that yields an abundance of fruit.

DESCRIPTION: 
s = Starting point of my house 
t = ending point of my house
a = location of apple 
b = location of orange
m = no of apples 
n = no of oranges
d = distance from the tree to the fruit

When a fruit falls from the tree, it lands on d units of distance from the
tree of origin along the z-axis. The negative value of d means the fruit
fell d units to the tree's left, and a positive value of d means it fell
d unit to the right.

Given the value of d for m apples and n oranges, determine how many apples
and oranges would fall to sam house (i.e in the inclusive range of |s, t|)

SAMPLE INPUT 
7 11 
5 15
3 2
-2 2 1
5 -6

SAMPLE OUTPUT:
Print two integers on two different lines:
    1. The first integer: the number of apples that fall on Sam's house. 
    2. The seconf integer: the number of oranges that falls on Sam's house.

1 1

CONSTRAINT:
1 <= s,t, a, b, m, m <= 10^5

"""



def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalapples = totaloranges = 0
    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            totalapples += 1
    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            totaloranges += 1
    print(totalapples)
    print(totaloranges)

s = 7
t = 10 
a = 4 
b = 12 
apples = [2, 3, -4]
oranges = [3, -2, -4]
countApplesAndOranges(s, t, a, b, apples, oranges)