"""
PROBLEM STATEMENT 
FlatLand Space Station

Flatland is a country with a number of cities, some of which have space stations.
Cities are numbered consecutively and each has a road of 1km length connecting to 
the next city. Determine the maximum distance from any city to the nearest space
station.

For example, there are n=3 cities and m=1 of them has a space station, city 1.
They occur consecutively along a route. City 2 is 2-1=1 unit away and city 3 is
3-1=2 units away. City 1 is 0 units from its nearest space station as one is 
located there. The meximum distance is 2.

CONDITIONS

SAMPLE INPUT 
5 2
0 4

SAMPLE OUTPUT 
2

CONSTRAINT
"""

def flatLandSpaceStation(n, c):
    """
    Parameters:
        n: number of cities
        c: an integer that contains the indices of cities
           with a space station, 1 based indexing.
    Output:
        res: (int) maximum distance from space station.
    """
    answer = 0
    c.sort()

    for i in range(1, len(c)):
        answer = max(answer, (c[i]-c[i-1] // 2))

    answer = max(answer, c[0], n-1 - c[-1])
    return answer


n = 5
c = [0, 4]

print(flatLandSpaceStation(n, c))

