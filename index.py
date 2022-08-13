"""
PROBLEM STATEMENT 
Library Fine

Your Local library needs your help! Given the expected and actual return dates
for a library book, create a program that calculates the fine (if any). The fee
structure is below:

1.  If the book is returned on or before the expected return date, no fine will
    be charged (i.e fine = 0).
2.  If the book is returned after the expected return day but still within the
    same calendar month and year as the expected return.
    fine = 15 Hackos * (no of days late).
3.  If the book is returned after the expected return month but still within the
    same calendar year as the expected return date, 
    fine = 500 Hackos * (no of months late).
4.  If the book is returned after the calendar year in which it was expected, there
    is a fixed fee of 10000 Hackos.
CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    total = 0
    if y1 > y2:
        total += 10000
    elif y1 == y2 and m1 > m2:
        total += 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        total += 15 * (d1 - d2)
    
    return total

