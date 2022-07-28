"""
PROBLEM STATEMENT 
Viral Advertisement

Hackerland Enterprise is adopting a new viral advertising strategy. When they launch
a new product, they advertise it to exactly 5 people on social media.

On the first day, half of those 5 people (i.e floor(5/2) = 2) like the advertisement
and each shares it with 3 of their friends. At the beginning of the second day, 
floor(5/2) * 3 = 2 * 3 = 6 people receive the advertisement.

Each day, floor(recipients/2) of the recipients like the advertisement and will share
it with 3 friends on the following day. Assuming nobody receives the advertisement
twice, determine how many people have liked the ad by the end of a given day, beginning
with launch day as day 1. 

For example, assume you want to know how many liked the ad by the end of the 5th day.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def viralAdvertising(n):
    """
    Parameters:
        n: the integer number of days
    """
    total_likes = 0
    shared = 5

    for i in range(n):
        like = shared // 2
        total_likes += like
        shared = like * 3

    return total_likes


print(viralAdvertising(5))