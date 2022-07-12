"""
PROBLEM STATEMENT 
Given a time in 12 hour AM/PM format, convert it to a military (24 hour) time. 
Note: Midnight is 12:00.00am on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00.00pm on a 12-hour clock, and 12:00:00 on a 24-hour clock..

CONDITIONS

SAMPLE INPUT 
A single string containing a time in 12 hour clock format i.e 
hh:mm:ss AM or hh:mm:ss PM where 01 <= hh <= 12 and
00 <= mm, ss <= 59.

07:05:45PM

SAMPLE OUTPUT 
Convert and print in 24-hours format where 
00 <= hh <= 23

19:05:45

CONSTRAINT
All input times are valid
"""


def timeConversion(s):
    meridian = s[-2:]

    if meridian == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    elif meridian == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    
    return s[:-2]

time = "07:05:45PM"
print(timeConversion(time))