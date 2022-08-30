"""
PROBLEM STATEMENT 
Service Lane

Calvin is driving his favorite vehicle on the 101 freeway. He notices that the
check engine light on the vehicle is on, and he wants to service it immediately
to avoid any risks. Luckily, a service lane runs parallel to the highway. The
service lane varies in width along its length.

You will be given an array of widths at points along the road (indices), then a 
list of indices of entry and exit points. Considering each entry and exit pair,
calculate the minimum size vehicle that can travel that segment of the service
lane safely.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""


def serviceLane(n, cases):
    result = []
    for i, j in cases:
        result.append(min(width[i : j+1]))

    return result