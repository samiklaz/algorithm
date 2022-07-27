"""
PROBLEM STATEMENT 
A discrete Mathematics Professor has a class of Students. Frustrated with their
lack of discipline, he decides to cancel class if fewer than some number of 
students are present when class starts. Arrival times go from on time 
(arrivalTime <= 0) to arrived time late (arrivalTime > 0). 

Given the arrival time of each student and a threshold number of attendees, 
determine if the class is canceled.

CONDITIONS

SAMPLE INPUT 
The first line of input contains t, the number of test cases.
Each test cases consists of two lines.

The first line has two space-seperated integer, n and k, the number of students 
(size of n) and the cancellation threshold.

The second line has two space-seperated integers (a[1], a[2]..., a[n]), describing
the arrival time for each student

2
4   3
-1  -3  4   2
4   2
0   -1  2   1

SAMPLE OUTPUT 
YES
NO

CONSTRAINT
"""

def angryProfessor(k, a):
    n = len(a)
    count = 0

    for i in a:
        if i <= 0:
            count += 1

    return "YES" if count >= k else "NO"


k = 3
a = [-1, -3, 4, 2]
print(angryProfessor(k, a))