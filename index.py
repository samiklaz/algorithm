"""
PROBLEM STATEMENT 
Taum Birthday

Taum is planning to celebrate the birthday of his friend, Dilska. There 
are two types of gifts that Dilsha wants from Taum: one is black and the 
other is white. To make her happy, Taum has to buy b black gifts and w 
white gifts.
    - The cost of each black gift is bc unit.
    - The cost of evry white gift is wc unit.
    - The cost of converting each black gift into white gift or vice versa
      is z units. 
Help Taum by deducing the minimum amount he needs to spend on Dilsha's gift.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def taumBday(b, w, bc, wc, z):
    """
    Parameters:
        - cost of black (b).
        - cost of white (w).
        - cost of converting black (bc).
        - cost of converting white (wc).
        - cost of converting each black to white and vice versa.
    """

    return min(b*bc + w*wc, bc*(w+b) + w+z, wc*(w+b) + b+z)