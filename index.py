"""
PROBLEM STATEMENT 
Save the Prisoner 

A Jail has a number of prisoners and a number of treats to pass out to them.
Their Jaller decides the fairest way to divide the treats is to seat the 
Prisoners around in a circular table in a sequentially numbered chairs. A
Chair number will be drawn from the hat. Beginning with the Prisoner in that 
Chair, one Candy will be handed to each prisoner sequentially around the table
until all have been distributed.

The Jaller is playing a little joke, though. The last piece of Candy looks like
all the others, but it tastes awful. Determine the Chair number occupied by the 
Prisoner that receives the Candy.

For example, there are 4 Prisoners and 6 pieces of Candy. The Prisoners arrange
themselves in seats numbered 1 to 4. Let's suppose two is drawn from the hat,
Prisoners receive candy at positions 2, 3, 4, 1, 2, 3. The Prisoners to be 
warned sits in chair number 3.

CONDITIONS

SAMPLE INPUT 
2
5   2   1
5   2   2

SAMPLE OUTPUT 
2
3

CONSTRAINT
"""


def saveThePrisoner(n, m, s):
    """
    n: no of Prisoner 
    m: no of Candy
    s: Starting number
    """

    res = s + m - 1
    print("res = ", res)
    res %= n 
    if res == 0:
        return n
    else: 
        return res

n = 5
m = 3
s = 4
print(saveThePrisoner(n, m, s))