"""
PROBLEM STATEMENT 
Leaderboard Ranking

Alice is playing an arcade game and wants to climb to the top of the Leaderboard
and wants to track her ranking. The game uses dense ranking, so its leaderboard
works like:

1.  The Player with the highest score is ranked 1 on the Leaderboard.
2.  The Player who have equal scores receives the same ranking number, and the 
    next player(s) receive immediately following ranking number.

For example, the four players on the Leaderboard have high scores of 100, 90, 90
and 80. Those Players will have ranks 1, 2, 2 and 3, respectively. If Alice's
scores are 70, 80 and 105, her ranking after each game are 4th, 3rd and 1st.

CONDITIONS

SAMPLE INPUT 

SAMPLE OUTPUT 

CONSTRAINT
"""

def climbingLeaderboard(scores, alice):
    scores.sort()
    scores = list(set(scores))
    n = len(scores)
    i = 0
    result = []

    for alscore in alice:
        print("i === ", i)
        print("scores[i] == ", scores[i])
        print("alscore === ", alscore)
        while i<n and scores[i] <= alscore:
            i += 1
        result.append(n - i + 1)
    return result

scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
print(climbingLeaderboard(scores, alice))