"""
PROBLEM STATEMENT 
Given a year, y, find the date of the 256th day of the year according to
the official Russian Calendar during that year. Then print it in the 
format dd, mm, yyyy, where dd is the two-digit day, mm is the two-digit 
month, and yyyy is y.

For example, the given year = 1984, 1984 is divisible by 4, so it is a 
leap year. The 256th day of a leap year after 1918 is september 12,
so the answer is 12.09.1984.

CONDITIONS

SAMPLE INPUT 
A simple integer denoting year y.
2017

SAMPLE OUTPUT 
13.09.2017

CONSTRAINT
1700 <= y <= 2700
"""

def dayOfProgrammer(year):
    if year == "1918":
        return "26.09.1918"
    elif (year < 1917 and year % 4 == 0) and (year > 1918 and year % 400 ==0 or (year % 4 == 0 and year % 100 != 0)):
        return "12.09.%s" % year
    else:
        return "13.09.%s" % year



print(dayOfProgrammer(2017))