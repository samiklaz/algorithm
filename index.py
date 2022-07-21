"""
PROBLEM STATEMENT
Garry is an avid hiker. He tracks his hikes meticulously, paying close attention to
small details like topography. During his lalst hike, he took exactly n steps. For 
every step he took, he noted if it was an uphill, U or downhill, D step. Gary hike
starts and ends at sea level and each step up or down represents a 1 unit change in
attitude. We define the following terms:
1.  A Mountain is a sequence of consecutive steps above sea level, starting with a 
    step up from sea level and ending with a step down to sea level. 
2.  A Valley is a sequence of consecutive steps below sea level, starting with a 
    step down from sea level and ending with a step up to sea level. 

Given Gary's sequence of up and down steps during his last hike, find and print
the number of valleys he walked through.

For exammple, if Gary's path is s = [DDUUUUDD], he first enters a valley 2 units deep.
Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level
and ends his hike.

CONDITIONS

SAMPLE INPUT 
8
UDDDUDUU

SAMPLE OUTPUT 
Print a single integer that denotes the number of valleys Gary walked through during 
his hike. 
1

CONSTRAINT
s[i] E {UD}
"""

def countingValleys(n, s):
    vallleyCount = level = 0
    d = {'U': 1, 'D': -1}

    for step in s:
        level += d[step]
        if level == 0 and step == 'U':
            vallleyCount += 1
    return vallleyCount