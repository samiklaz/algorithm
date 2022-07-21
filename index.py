"""
PROBLEM STATEMENT 
Two cats and a mouse are at various positions on a line. You will be given their starting
positions. Your task is to determine which cat will reach the mouse first, assuming the
mouse does'nt move and the cats travel at equal speed. If the cats arrive at the same time,
the mouse will be allowed to move and it will escape if they fight.

You are given q queries in the form x, y and z representing the respective positions for 
cats A and B, and the mouse C. Complete the function catAndMouse to return the appropraite
answer to each query, which is printed on a new line. 
1.  If Cat A catches the mouse first, print Cat A.
2.  If Cat B catches the mouse first, print Cat B.
3.  if both Cats reaches the mouse at the same time, print Mouse C as the two Cats fight
    and mouse escapes.

For example, Cat A is at position x = 2 and Cat B is y = 5. If the Mouse C is at position
z = 4, it is 2 units from Cat A and 1 unit from Cat B. cat B would catch the mouse.

CONDITIONS

SAMPLE INPUT 
2 
1   2   3
1   3   2

SAMPLE OUTPUT 
Cat B
Mouse C

CONSTRAINT
"""

def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)

    if catA == catB:
        return "Mouse C"
    elif catA < catB:
        return "Cat A"
    else:
        return "Cat B"

x = 1
y = 2
z = 3

print(catAndMouse(x, y, z))