"""
PROBLEM STATEMENT 
ACM Team

There are a number of people who will be attending ACM KPC world finals.
Each of them may be well versed in a number of topics. Given a list of
topics known by each attendee, you must determine the maximum number of
topics a 2 person team can know. Also find out how many ways a team can
be formed to know that many topics. Lists will be in form of bit strings, 
where each string represents an attendee and each position in that string
represents a field of knowledge, 1 if it is a known field and 0 if not.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def acmTeam(topic):
    n = len(topic)
    maxsub = 0
    count = 0 
    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1

            if sub > maxsub:
                maxsub = sub
                count = 1
            elif sub == maxsub:
                count += 1

    return [maxsub, count]


