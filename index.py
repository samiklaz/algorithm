"""
PROBLEM STATEMENT 
Hurdle Race

Dan is playing a video game in which the character competes in a hurdle race. Hurdles are
of varying heights, and Dan has a maximum height he can jump. There is a magic portion he
can take that will increase his maximum height by 1 unit for each dose. How many doses of
portion must he take to be able to jump all the hurdles.

Given an array of hurdles heights height, and an initial maximum height Dan can jump, k, 
determine the minimum number of doses Dan must take to be able to clear all the hurdles
in the race. 

For example, if height = [1, 2, 3, 3, 2] and Dan can jump 1 unit high naturally, he must 
take 3-2=1 doses of portion to be able to jump all the hurdles.

CONDITIONS

SAMPLE INPUT 
5   4
1   6   3   5   2

SAMPLE OUTPUT 
2

CONSTRAINT
"""

"""
My Solution
def hurdleRace(k, height):
    max_height = max(height)
    if max_height> k:
        dose = max_height - k
    else:
        dose = 0
    return dose
"""

def hurdleRace(k, height):
    max_height = max(height)
    return max(max_height-k, 0)

k = 4
height = [1, 6, 3, 5, 2]
print(hurdleRace(k, height))