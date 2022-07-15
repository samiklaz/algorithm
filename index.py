"""
PROBLEM STATEMENT 
Maria plays basketball and wants to go pro. Each season, she
maintains a record after play. She tabulates the number of 
times she breaks her season record for most points and 
least points in the game. Points scored in the first game
established her record for the season, and she begins
counting from there.

Assume her scores to be [12, 24, 10, 24]

Game Score Minimum Maximum Min Max
0      12     12     12     0   0  
1      24     12     24     0   1  
2      10     10     24     1   1 
3      24     10     24     1   1

CONDITIONS

SAMPLE INPUT 
9
10 5 20 20 4 5 2 25 1

SAMPLE OUTPUT 
2 4

CONSTRAINT
1 <= n <= 1000
0 <= scores[i] <= 10^5
"""


def breakingRecords(scores):
    minCount = maxCount = 0
    minScore = maxScore = scores[0]

    for i in range(1, len(scores)):
        if minScore < scores[i]:
            minScore = scores[i]
            minCount += 1
        elif maxScore > scores[i]:
            maxScore = scores[i]
            maxCount += 1

    return minCount, maxCount

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))