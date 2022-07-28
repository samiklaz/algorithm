"""
PROBLEM STATEMENT 
Beautiful Days

Lily likes to play games with integers. She created a new game where she determines the 
difference between a number and its reverse. For instance, given the number 12, it's 
reverse is 21. Their difference is 9. The number 120 reversed is 21 and their difference
is 99.

She decides to apply her game to decision making. She will look at a numbered range of
days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i...j] and a number k. determine the number of days in 
the range that are beautiful. Beautiful numbers are defined as numbers where |i - reverse(i)|
is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. Print 
the number of days in the range.

SAMPLE INPUT 
20 23 6

SAMPLE OUTPUT 
2

CONSTRAINT
"""

def beautifulDays(i, j, k):
    """
    Parameters:
        i: the starting point of the number
        j: the endig point of the number
        k: the divisor
    """
    count = 0
    for num in range(i, j+1):
        reverse_num = int(str(num)[::-1])
        difference = abs(num - reverse_num)
        if difference % k == 0:
            count += 1
    return count

i = 20
j = 23 
k = 6
print(beautifulDays(i, j, k))