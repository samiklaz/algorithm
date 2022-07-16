"""
PROBLEM STATEMENT 
You have been asked to study the population of birds migrating across 
the continent. Each type of bird you are interested in will be 
identified by an integer value. Each time a particular kind of bird 
is spotted, its ID number will be added to the array of sightings.

You would like to be able to find out which type of bird is most
common given a list of sightings. Your task is to print the type 
number of that bird and if two birds are equally common, choose 
the type with the smallest ID number. 

For example, assume your bird sightings are of types
arr = [1, 1, 2, 2, 3], there are two each of types 1 and 2, and
one sighting of type 3. Pick the lower of the two types seen twice:
type 1.

CONDITIONS

SAMPLE INPUT 
6
1 4 4 4 5 3

SAMPLE OUTPUT 
4

CONSTRAINT
5 <= n <= 2 * 10^5
It is guaranteed that each type is 1 2 3 4 or 5
"""

def migratoryBirds(arr):
    l = [0] * len(arr)

    for i in range(len(arr)):
        l[arr[i]] += 1
    return l.index(max(l))

arr = [1, 1, 2, 2, 3]
print(migratoryBirds(arr))