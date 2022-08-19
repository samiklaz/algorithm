"""
PROBLEM STATEMENT 
Jumping on Clouds

Emma is playing a new mobile game that starts with consecutively numbered
clouds. Some of the clouds are thunderheads and others are cumulus. She
can jump on any cumulus cloud having a number that is equal to the number
of the current cloud plus 1 and 2. She must avoid the thunderhead.

Determine the number of jumps it will take for Emma to jump from her starting
position to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or
1 if they must be avoided.

For example, c = [0, 1, 0, 0, 0, 1, 0] indexed from 0...6, the number on each 
cloud is its index in the list so she must avoid the cloud at indexes 1 and 5.
She could follow the following 2 paths: 0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6,
the first path tkes 3 jumps while the second takes 4.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def jumpingCloud(c):
    """
    Parameters:
        c: an array of binary integers.
    Output:
        integer representing the minimum
        number of jumps.
    """
    n = len(c)
    jump = 0
    i = 0
    while i < n-1:
        if i + 2 < n and c[i + 2] == 0:
            jump += 1
            i+= 2
        elif i+1 < n and c[i + 1] == 0:
            jump += 1
            i += 1

    return jump

c = [0, 1, 0, 0, 0, 1, 0]
print(jumpingCloud(c))