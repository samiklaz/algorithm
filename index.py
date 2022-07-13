"""
PROBLEM STATEMENT 
HackerLand University has the following grading policy:
1.  Every Student receives a grade in the inclusive range 0f 0 to 100.
2.  Any grade less than 10 is a failing grade.

Sam is a professor and likes to round off student's grade in the 
following rules:
1.  If the difference between the grade and the next multiple of 
    5 is less than 3, round grade up to the nest multiple of 5.
2.  If the value of the grade is less than 38, no rounding occurs
    as the result will be a failing grade.


CONDITIONS

SAMPLE INPUT 
4
73
67
38
33

SAMPLE OUTPUT 
4
75
67
40
33

CONSTRAINT
"""
from array import array

def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5 
            if mod5 >= 3:
                print(f'Index position is {grade}')
                grade += (5-mod5)
        res.append(grade)
    return res
            

grades = array('i', [4, 73, 67, 38, 33])
print(gradingStudents(grades))