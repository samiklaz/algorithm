"""
PROBLEM STATEMENT 
Elecronic shop
Monica wants to buy a keyboard and a USB drive from her favorite electronic store.
The store has several models of each, Monica wants to spend as much as possible
for the 2 items given her budget.

Given the price lists for the store keyboard and USB drives, and Monica's budget,
find and print the amount of money Monica will spend. If she doesn't have enough
money to buy both a keyboard and a USB drive, print -1 instead. She will buy only 
the two required items.

For example, suppose she has b = 60 to spend. Three types of keyboards cost
keyboards = [40, 50, 60], Two USB drive cost drives = [5, 8, 12]. She could have
purchase a 40 keyboard + 12 USB drive = 52 or a 50 Keyboard + 8 USB drive = 58.
She chooses the later. She can buy more than 2 items so she can't spend exactly 60.

CONDITIONS

SAMPLE INPUT 
10  2   3
3   1
5   2   8

SAMPLE OUTPUT 
9

CONSTRAINT
"""

def getMoneySpent(keyboards, drives, b):
    maxAmount = -1

    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive  <= b:
                maxAmount = max(maxAmount, keyboard+drive)

    return maxAmount

keyboards = [3, 1]
drives = [5, 2, 8]
b = 9
getMoneySpent(keyboards, drives, b)